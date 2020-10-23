## The Molino Galaxy Mock Catalogs
75,000 galaxy mock catalogs designed to quantify the information content of any cosmological observable for a redshift-space galaxy sample.  
They are constructed from the [Quijote N-body simulations](https://github.com/franciscovillaescusa/Quijote-simulations)
using the standard [Zheng et al. (2007)](https://ui.adsabs.harvard.edu/abs/2007ApJ...667..760Z/abstract) Halo Occupation 
Distribution (HOD) model. 

The fiducial HOD parameters are based on the SDSS high luminosity samples. The suite contains: 
- 15,000 mocks at the fiducial cosmology and HOD parameters for covariance matrix estimation 
- (500 N-body realizations) x (5 HOD realizations)=2,500 mocks at 24 other parameter values to
  estimate the derivative of the observable with respect to six cosmological parameters 
  (Omega_m, Omega_b, h, n_s, sigma_8, and M_nu) and five HOD parameters (logMmin, sigma_logM, log M_0, alpha, and log M_1).

Using the covariance matrix and derivatives calculated from Molino, one can derive Fisher matrix forecasts on the cosmological parameters marginalized over HOD parameters.


### cosmologies
