# The Molino Suite of Galaxy Mock Catalogs
Molino contains 75,000 galaxy mock catalogs designed to quantify the information content of any cosmological observable for a redshift-space galaxy sample. The galaxy catalogs are constructed from the Quijote N-body simulations ([Villaescusa-Navarro _et al._ 2020](https://ui.adsabs.harvard.edu/abs/2020ApJS..250....2V/abstract)) using the standard [Zheng *et al.* (2007)](https://ui.adsabs.harvard.edu/abs/2007ApJ...667..760Z/abstract) Halo Occupation Distribution (HOD) model. 

The [fiducial HOD parameters](#halo-occupation-distribution) are based on the SDSS high luminosity samples. The suite includes: 

- 15,000 mocks at the fiducial cosmological and HOD parameters for covariance matrix estimation
- (500 N-body realizations) x (5 HOD realizations)=2,500 mocks at 24 other parameter values to estimate the derivative of the observable with respect to six cosmological parameters (Omega_m, Omega_b, h, n_s, sigma_8, and M_nu) and five HOD parameters (logMmin, sigma_logM, log M_0, alpha, and log M_1). 

Using the covariance matrix and derivatives calculated from Molino, you can derive [Fisher matrix forecasts](#fisher-forecasts) on the cosmological parameters marginalized over HOD parameters.

## Data

The Molino galaxy catalogs are stored in Princeton's `dataspace`: https://dataspace.princeton.edu/

- /z=0/ 
  - fiducial/
  - Om_p/
  - Om_m/ 
  - Ob_p/
  - Ob_m/ 
  - h_p/
  - h_m/ 
  - ns_p/
  - ns_m/ 
  - s8_p/ 
  - s8_m/ 
  - Mnu_p/
  - Mnu_pp/
  - Mnu_ppp/
  - fiducial_ZA/ 
  - logMmin_p/
  - logMmin_m/
  - sigma_logM_p/
  - sigma_logM_m/
  - logM0_p/
  - logM0_m/
  - alpha_p/
  - alpha_m/
  - logM1_p/
  - logM1_m/

Each mock catalog is an HDF5 file that contains the position, velocity, and extra information of ~150,000 galaxies. 

## Installation



## Halo Occupation Distribution



## Fisher Forecasts



## Team 
- ChangHoon Hahn (Princeton) 
- Francisco Villaescusa-Navarro (FlatironPrinceton)
