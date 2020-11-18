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
|zheng|_ Halo Occupation Distribution (HOD) model. The suite 
contains the galaxy catalogs necessary to conduct a Fisher matrix
forecast over a full set of cosmological and HOD parameters for 
any cosmological observable for a redshift-space galaxy sample:

.. _text1: https://ui.adsabs.harvard.edu/abs/2020ApJS..250....2V/abstract/
.. |text1| replace:: Villaescusa-Navarro *et al.* 2020

.. _zheng: https://ui.adsabs.harvard.edu/abs/2007ApJ...667..760Z/abstract/
.. |zheng| replace:: Zheng *et al.* (2007)

*   ``15,000 mocks`` at the fiducial cosmological and HOD parameters for covariance 
    matrix estimation
*   ``60,000 mocks`` at 24 other parameter values (2,500 mocks each) to estimate the 
    derivative of observables with respect to all six cosmological parameters 
    (``Omega_m``, ``Omega_b``, ``h``, ``n_s``, ``sigma_8``, and ``M_nu``) and five 
    HOD parameters 
    (``logMmin``, ``sigma_logM``, ``logM0``, ``alpha``, and ``logM1``). 

The fiducial cosmological parameter values are ``Omega_m=0.3175``, ``Omega_b=0.049``,
``h=0.6711``, ``n_s=0.9624``, ``sigma_8=0.834``, and ``M_nu = 0.0 eV``. The fiducial 
HOD parameters are based on the high luminosity samples of the Sloan Digital Sky Survey 
(``M_r < -21.5`` and ``M_r < 22`` samples): 
``log Mmin=13.65``, ``sigma_logM=0.2``, ``log M0=14.0``, ``alpha=1.1``, ``log M_0=14.0``. 
The other 24 non-fiducial parameter values are set by adjusting a single parameter 
either a step above or below the fiducial value. Since ``M_nu`` cannot be negative, 
the ``M_\nu`` steps are at 0.1, 0.2, 0.4 eV. At the fiducial parameters, the galaxy 
catalogs have number density ``n_g ~ 1.63x10^-4 h^3 Mpc^-3``. Each galaxy catalog 
has a volume ``(1 Gpc/h)^3``.

To easily access the galaxy mock catalogs and compute cosmological obseravbles,
check out the |molino|_.


.. _molino: https://github.com/changhoonhahn/molino/
.. |molino| replace:: ``molino`` python package


.. toctree::
   :maxdepth: 2

   down
   install
