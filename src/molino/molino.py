import os, h5py 

try: 
    os.environ['MOLINO_DIR']
except KeyError: 
    print("please set environment variable `MOLINO_DIR`. See README.md for details") 


cosmo_list = []


def GalaxyCatalog(cosmo, i_nbody=1, i_hod=1, apply_rsd=False, columns=['x', 'y', 'z']): 
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
    if cosmo is not in cosmo_list: 
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

    if apply_rsd: 
        assert apply_rsd in ['x', 'y', 'z'], "Which direction do you want to apply the RSD?"
    
    
    catalogs = [] 
    # loop through n-body realizations 
    for inbody in i_nbody: 

        # loop through HOD realizations 
        for ihod in i_hod: 
            # read catalog at `cosmo` cosmology with `_i_nbody`th n-body
            # realization and `_i_hod` HOD realization. 
            catalog = _read_catalog(cosmo, inbody, ihod, colums)
            catalogs.append(catalog)




    if len(catalogs) == 1: 
        return catalogs[0] 
    else: 
        return catalogs 



def _read_catalog(cosmo, i_nbody, i_hod, columns): 
    ''' read a single galaxy catalog 
    '''
    
    gals = h5py.File(fgal, 'r') 

    if ('x' in columns) or ('y' in columns) or ('z' in columns): 
        xyz = gals['pos'][...]
    
    if ('vx' in columns) or ('vy' in columns) or ('vz' in columns): 
        vxyz = gals['vel'][...]
    
    if ('x_halo' in columns) or ('y_halo' in columns) or ('z_halo' in columns): 
        xyz_h = gals['halo_pos'][...]

    if ('vx_halo' in columns) or ('vy_halo' in columns) or ('vz_halo' in columns): 
        vxyz_h = gals['halo_vel'][...]
    
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
    
    return np.array(cat) 



def cosmo_lookup(cosmo): 
    '''
    '''
