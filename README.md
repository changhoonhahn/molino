# The Molino Suite of Galaxy Mock Catalogs
Molino contains 75,000 galaxy mock catalogs designed to quantify the information content of any cosmological observable for a redshift-space galaxy sample. They are constructed from the Quijote N-body simulations using the standard Zheng et al. (2007) Halo Occupation Distribution (HOD) model. The fiducial HOD parameters are based on the SDSS high luminosity samples. The suite contains 15,000 mocks at the fiducial cosmology and HOD parameters for covariance matrix estimation. It also includes (500 N-body realizations) x (5 HOD realizations)=2,500 mocks at 24 other parameter values to estimate the derivative of the observable with respect to six cosmological parameters (Omega_m, Omega_b, h, n_s, sigma_8, and M_nu) and five HOD parameters (logMmin, sigma_logM, log M_0, alpha, and log M_1). Using the covariance matrix and derivatives calculated from Molino, one can derive Fisher matrix forecasts on the cosmological parameters marginalized over HOD parameters.


## General Information

1. Title of Dataset: The Molino Suite of Galaxy Mock Catalogs

2. Author Information
	A. Principal Investigator Contact Information
		Name: ChangHoon Hahn
		Institution: Princeton University
		Address: 4 Ivy Lane Princeton, NJ 08544
		Email: changhoon.hahn@princeton.edu


## Sharing/Access Information

1. Licenses/restrictions placed on the data: 
None 

2. Links to publications that cite or use the data: 
There is currently a paper in preparation. I will be coordinating the submission of the paper with the public release of this data set. 

3. Links to other publicly accessible locations of the data: 
None 

## Data & File Overview

1. File List: 

folder structure
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


/z=0/fiducial/ contains 15,000 galaxy mock catalogs

the rest /z=0/../ contain 2,500 galaxy mock catalogs  

Each mock catalog is an HDF5 file that contains the position, velocity, and
extra information of ~150,000 galaxies. 

2. Relationship between files, if important: 
Not important 

3. Additional related data collected that was not included in the current data package: 
None

4. Are there multiple versions of the dataset?
No 


### Methodological Information

1. Description of methods used for collection/generation of data: 

The Molino suite is constructed from the Quijote N-body simulations
(Villaescusa-Navarro et al. 2020) using the standard Zheng et al. (2007) 
Halo Occupation Distribution (HOD) model.

- Villaescusa-Navarro, F., Hahn, C., Massara, E., et al. 2020, The Astrophysical Journal Supplement Series, 250, 2
- Zheng, Z., Coil, A. L., & Zehavi, I. 2007, The Astrophysical Journal, 667, 760

2. Methods for processing the data: 
<describe how the submitted data were generated from the raw or collected data>

3. Instrument- or software-specific information needed to interpret the data: 
In conjunction with the data I will be releasing a python package 
(https://github.com/changhoonhahn/molino), which will provide a convenient
interface for reading the data and running standard calculations. 

4. Standards and calibration information, if appropriate: 
N/A

5. Environmental/experimental conditions: 
N/A

6. Describe any quality-assurance procedures performed on the data: 
N/A

7. People involved with sample collection, processing, analysis and/or submission: 
Francisco Villaescusa-Navarro (Princeton University)
