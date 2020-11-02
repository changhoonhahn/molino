__all__ = ['test_download', 'test_galaxycatalog']

import pytest
# --- molino --- 
from molino import GalaxyCatalog


@pytest.mark.parametrize("cosmo", ('Om_p', 'Ob2_p', 'h_p', 'ns_p', 's8_p', 'Om_m',  'Ob2_m',
            'h_m', 'ns_m', 's8_m', 'Mnu_p', 'Mnu_pp', 'Mnu_ppp', 'logMmin_m',
            'logMmin_p', 'sigma_logM_m', 'sigma_logM_p', 'logM0_m', 'logM0_p',
            'alpha_m', 'alpha_p', 'logM1_m', 'logM1_p', 'fiducial_ZA',
            'fiducial')) 
def test_download(cosmo, redshift=0): 
    ''' check the downloads 
    '''
    import os
    import glob 

    molino_dir = os.path.join(os.environ['MOLINO_DIR'], 
            'z=%.f' % redshift, cosmo) 
    fmocks = glob.glob(os.path.join(molino_dir, '*.hdf5'))

    if cosmo == 'fiducial': 
        Nmock = 150000
    else: 
        Nmock = 2500
    
    msg = "see README.md for download details" 
    assert len(fmocks) == Nmock, ("%s: missing %i files, %s" % (cosmo, Nmock - len(fmocks), msg))

    return None 


@pytest.mark.parametrize("cosmo", ('Om_p', 'Ob2_p', 'h_p', 'ns_p', 's8_p', 'Om_m',  'Ob2_m', 'h_m', 'ns_m', 's8_m', 'Mnu_p', 'Mnu_pp', 'Mnu_ppp', 'logMmin_m', 'logMmin_p', 'sigma_logM_m', 'sigma_logM_p', 'logM0_m', 'logM0_p', 'alpha_m', 'alpha_p', 'logM1_m', 'logM1_p', 'fiducial_ZA', 'fiducial')) 
def test_galaxycatalog(cosmo): 

    for rsd in [False, 'x', 'y', 'z']: 

        xyz = GalaxyCatalog(cosmo, i_nbody=1, i_hod=1, z=0, apply_rsd=rsd,
                columns=['x', 'y', 'z'])
        assert xyz.shape[1] == 3
    
        xyzs = GalaxyCatalog(cosmo, i_nbody=range(5), i_hod=range(5), z=0,
                apply_rsd=rsd, columns=['x', 'y', 'z'])
        assert len(xyzs) == 25 
        assert xyzs[0].shape[1] == 3 
