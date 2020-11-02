import os, h5py 
import numpy as np 

try: 
    os.environ['MOLINO_DIR']
except KeyError: 
    print("please set environment variable `MOLINO_DIR`. See README.md for details") 


def GalaxyCatalog(cosmo, i_nbody=1, i_hod=1, z=0, apply_rsd=False, columns=['x', 'y', 'z']): 
    ''' Read a galaxy catalog(s) from the Molino suite

    Parameters
    ----------
    cosmo : string 
        cosmology of the galaxy catalog. see
        https://changhoonhahn.github.io/molino/ for details 


    i_nbody : int or array_like[inbody,]
        The number of N-body realization. The Molino mocks are generated using
        Quijote N-body simulations. This specifies which N-body
        realization(s) to read. (Default: 1) 

    i_hod : int or array_like[ihod,]
        The number of HOD realization. For some of the cosmologies, the mocks
        are generated using multiple HOD realizations. This specifies which HOD
        realization(s) to read. (Default: 1) 

    z : float
        redshift

    apply_rsd : bool or string
        If False, don't apply redshift-space distortions. Otherwise, specify
        which direction ('x', 'y', 'z') you want the RSD to be applied.
        (Default: False) 

    columns : array_like[icol,]
        Specify which properties of the galaxy you want included. The following
        properties are available: 
            - positions [Mpc/h]: 'x', 'y', 'z'
            - velocities [km/s]: 'vx', 'vy', 'vz'
            - galaxy type*: 'gal_type' 
            - host halo positions [Mpc/h]: 'x_halo', 'y_halo', 'z_halo'
            - host halo velocities [km/s]: 'vx_halo', 'vy_halo', 'vz_halo'
            - halo virial mass [Msun/h]: 'm_halo'
            - halo virial radius : 'r_halo'

        * 0:central, 1:satellite


    Returns 
    -------
    catalogs : array_like 
    '''
    # parse inputs 
    cosmo_list = ['Om_p', 'Ob2_p', 'h_p', 'ns_p', 's8_p', 'Om_m',  'Ob2_m',
            'h_m', 'ns_m', 's8_m', 'Mnu_p', 'Mnu_pp', 'Mnu_ppp', 'logMmin_m',
            'logMmin_p', 'sigma_logM_m', 'sigma_logM_p', 'logM0_m', 'logM0_p',
            'alpha_m', 'alpha_p', 'logM1_m', 'logM1_p', 'fiducial_ZA', 'fiducial']
    if cosmo not in cosmo_list: 
        msg = '\n'.join([
            'please choose among one of the following cosmologies:', 
            ', '.join(cosmo_list)
            ]) 
        raise ValueError(msg)
    
    try: 
        i_nbody = [int(i_nbody)]
    except TypeError:
        i_nbody = [int(_i) for _i in i_nbody] 

    try: 
        i_hod = [int(i_hod)]
    except TypeError: 
        i_hod = [int(_i) for _i in i_hod]

    if z not in [0.]: 
        raise ValueError('z=%f is not yet supported' % z) 

    if apply_rsd: 
        assert apply_rsd in ['x', 'y', 'z'], "Which direction do you want to apply the RSD?"
    
    catalogs = [] 
    # loop through n-body realizations 
    for inbody in i_nbody: 

        # loop through HOD realizations 
        for ihod in i_hod: 
            # read catalog at `cosmo` cosmology with `_i_nbody`th n-body
            # realization and `_i_hod` HOD realization. 
            catalog = _read_catalog(cosmo, inbody, ihod, z, columns, apply_rsd)
            catalogs.append(catalog)

    if len(catalogs) == 1: 
        return catalogs[0] 
    else: 
        return catalogs


def _read_catalog(cosmo, i_nbody, i_hod, z, columns, apply_rsd): 
    ''' read a single galaxy catalog 
    '''
    z_str = {'0.0': '0', '0.5': '0.5', '1.0': '1'}['%.1f' % z]

    fgal = os.path.join(os.environ['MOLINO_DIR'], 'z=%s' % z_str, cosmo, 
            'molino.z%.1f.%s.nbody%i.hod%i.hdf5' % (z, cosmo, i_nbody, i_hod))
    gals = h5py.File(fgal, 'r') 

    xyz = gals['pos'][...]
    
    if ('vx' in columns) or ('vy' in columns) or ('vz' in columns): 
        vxyz = gals['vel'][...]
    
    if ('x_halo' in columns) or ('y_halo' in columns) or ('z_halo' in columns): 
        xyz_h = gals['halo_pos'][...]

    if ('vx_halo' in columns) or ('vy_halo' in columns) or ('vz_halo' in columns): 
        vxyz_h = gals['halo_vel'][...]

    # apply redshift-space distoritons 
    if apply_rsd:
        vel_offset = gals['vel_offset'][...] # velocity offsets

        # line-of-sight
        LOS = {'x': [1, 0, 0], 'y': [0, 1, 0], 'z': [0, 0, 1]}[apply_rsd] 
        i_rsd = np.arange(3)[np.array(LOS).astype(bool)][0]

        xyz += vel_offset * LOS
        # impose periodic boundary conditions for particles outside the box 
        _rsd = xyz[:,i_rsd] % 1000.  
        xyz[:,i_rsd] = np.array(_rsd)

    
    cat = [] 
    for col in columns:
        if col == 'x': cat.append(xyz[:,0])
        if col == 'y': cat.append(xyz[:,1])
        if col == 'z': cat.append(xyz[:,2])
        if col == 'vx': cat.append(vxyz[:,0])
        if col == 'vy': cat.append(vxyz[:,1])
        if col == 'vz': cat.append(vxyz[:,2])
        if col == 'x_halo': cat.append(xyz_h[:,0])
        if col == 'y_halo': cat.append(xyz_h[:,1])
        if col == 'z_halo': cat.append(xyz_h[:,2])
        if col == 'vx_halo': cat.append(vxyz_h[:,0])
        if col == 'vy_halo': cat.append(vxyz_h[:,1])
        if col == 'vz_halo': cat.append(vxyz_h[:,2])
        if col == 'gal_type': cat.append(gals['gal_type'][...])
        if col == 'm_halo': cat.append(gals['m_halo'][...]) 
        if col == 'r_halo': cat.append(gals['r_halo'][...]) 
    
    return np.array(cat).T
