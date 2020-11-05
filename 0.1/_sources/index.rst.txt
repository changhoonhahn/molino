.. molino documentation master file, created by
   sphinx-quickstart on Wed Nov  4 15:39:30 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The Molino Suite of Mock Galaxy Catalogs
========================================
Molino contains 75,000 galaxy mock catalogs designed to quantify
the information content of any cosmological observable for a 
redshift-space galaxy sample. The galaxy catalogs are constructed 
from the Quijote N-body simulations (|text1|_) using the standard 
|zheng|_ Halo Occupation Distribution (HOD) model. 

.. _text1: https://ui.adsabs.harvard.edu/abs/2020ApJS..250....2V/abstract/
.. |text1| replace:: Villaescusa-Navarro *et al.* 2020

.. _zheng: https://ui.adsabs.harvard.edu/abs/2007ApJ...667..760Z/abstract/
.. |zheng| replace:: Zheng *et al.* (2007)

The fiducial HOD parameters are based on the SDSS high luminosity samples. The suite includes: 

*   ``15,000 mocks`` at the fiducial cosmological and HOD parameters for covariance 
    matrix estimation
*   ``60,000 mocks`` = (500 N-body realizations) x (5 HOD realizations) x (24 other parameter values) 
    to estimate the derivative of the observable with respect to six cosmological parameters 
    (``Omega_m``, ``Omega_b``, ``h``, ``n_s``, ``sigma_8``, and ``M_nu``) and five HOD parameters 
    (``logMmin``, ``sigma_logM``, ``logM0``, ``alpha``, and ``logM1``). 

Using the covariance matrix and derivatives calculated from Molino, 
you can derive Fisher matrix forecasts on the cosmological parameters 
marginalized over HOD parameters. The ``molino`` python package 
provides an easy way to access the galaxy mock catalogs.  


.. toctree::
   :maxdepth: 2

   install
   hod 
