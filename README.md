# The Molino Suite of Mock Galaxy Catalogs
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/changhoonhahn/molino/blob/main/LICENSE)
[![DOI ark](http://img.shields.io/badge/DOI-10.34770/rhzt-blue.svg?style=flat)](http://arks.princeton.edu/ark:/88435/dsp012v23vx458)

`molino` is a python package for easily utilizing the mock galaxy catalogs in
the Molino Suite. 

Molino suite contains 75,000 galaxy mock catalogs designed to quantify
the information content of any cosmological observable for a 
redshift-space galaxy sample. The galaxy catalogs are constructed 
from the Quijote N-body simulations 
([Villaescusa-Navarro *et al.* 2020](https://ui.adsabs.harvard.edu/abs/2020ApJS..250....2V/abstract/))
using the standard 
[Zheng *et al.* (2007)](https://ui.adsabs.harvard.edu/abs/2007ApJ...667..760Z/abstract/)
Halo Occupation Distribution (HOD) model. The suite 
contains the galaxy catalogs necessary to conduct a Fisher matrix
forecast over a full set of cosmological and HOD parameters for 
any cosmological observable for a redshift-space galaxy sample:
- 15,000 mocks at the fiducial cosmological and HOD parameters for covariance matrix estimation
- 60,000 mocks at  24 other parameter values (2,500 mocks each) to estimate the 
  derivative of observables with respect to all six cosmological parameters 
  (`Omega_m`, `Omega_b`, `h`, `n_s`, `sigma_8`, and `M_nu`) and five HOD parameters 
  (`logMmin`, `sigma_logM`, `logM0`, `alpha`, and `logM1`). 

Using the covariance matrix and derivatives calculated from Molino, 
you can derive [Fisher matrix forecasts](#fisher-forecasts) on the
cosmological parameters marginalized over HOD parameters. This python 
package provides an easy way to access the galaxy mock catalogs.
For more details on the catalogs see the  
[website](https://changhoonhahn.github.io/molino/current/). 

## Installation
### Downloading the Data
The Molino galaxy catalogs can be downloaded using 
[this globus endpoint](https://app.globus.org/file-manager?origin_id=dc43f461-0ca7-4203-848c-33a9fc00a464&origin_path=%2Frhzt-ed89%2F).  
If you have access to Princeton's clusters, the data is also available in
`/tigress/chhahn/molino/z=0/`. 

The data consists of multiple `*.tar.gz`  files: 

- `fiducial.tar.gz`

- `Om_p.tar.gz`

-  `Om_m.tar.gz`

  … 

- `logM1_p.tar.gz`

- `logM1_m.tar.gz`

Each `*.tar.gz` file contains the galaxy mock catalogs at a different set of cosmological and HOD parameters. Each mock catalog is an HDF5 file that contains the position, velocity, and extra information of ~150,000 galaxies. 

### Installing `molino`

#### setting up the environment

First, add the following to your `~/.bash_profile`, `~/.bashrc`, or `~/.bashrc.ext` : 

```bash
export HDF5_USE_FILE_LOCKING=FALSE
export MOLINO_DIR="\DIRECTORY_WITH_MOLINO_FILES\" 
```
This allows the package to find where the downloaded `molino` data is located. Don't forget to run `source ~/.bashrc` or `source ~/.bash_profile` on the command line so  that the changes take effect.

#### install the `molino` package

```bash
# clone the repo
git clone https://github.com/changhoonhahn/molino.git

# go to repo directory
cd molino

# install the package
pip install -e . 
```

#### uncompressing the data

The data is available in a compressed form to save space. Before you can use the galaxy catalogs, you'll first have to uncompress the data. You can use the following script in the `molino` package to do this: 

```bash
cd "\DIRECTORY_WHERE_YOU_CLONED_THE_MOLINO_REPO\"
sh bin/uncompress.sh
```

Uncompressing the data can take a couple of minutes so plan accordingly. 

***You're all set!*** Check out some examples to see how you can use `molino`  to easily: *e.g.* [read in the galaxy mocks](), calculate the [redshift-space galaxy power spectrum](), or calculate the [redshift-space galaxy bispectrum](). 

## Halo Occupation Distribution

We use the Halo Occupation Distribution (HOD) framework to construct the Molino galaxy mocks. HODs statistically populate galaxies in dark matter halos by specifying the probability of a given halo hosting N galaxies  based on its halo mass --- P(N|M_h). We use the standard Zheng _et al._ (2007) HOD model. 

For the fiducial HOD parameters, we use the following values

- `log Mmin = 13.65`
- `sigma_logM = 0.2`
- `log M0 = 14.0`
- `alpha = 1.1`
- `log M1 = 14.0`

These values are based on the best-fit HOD parameters for the SDSS high luminosity samples (Mr < -21.5 and <-22), modified to accommodate the halo mass limit of the Quijote simulations.

## Fisher Forecasts
The Molino suite provides all the ingredients to conduct a Fisher forecast of
any cosmological observable. The Fisher matrix can be calculated for some
observable `B` using 

<img src="docs/fisher.png" alt="fisher" width="300" />

`C` is the covariance matrix, which can be derived from the 15,000 fiducial
galaxy catalogs. The derivatives of `B` can be calculated using the rest of the
catalogs with finite difference. 

## Team 
- ChangHoon Hahn (Princeton) 
- Francisco Villaescusa-Navarro (Flatiron/Princeton)


## Contact
If you have any questions or need help using the data, feel free to 
raise a github issue or contact me at changhoon.hahn@princeton.edu 
