---
title: "The Molino Suite of Mock Galaxy Catalogs"
tags:
  - Python
  - cosmology: cosmological parameters
  - cosmology: large-scale sturcture of the Universe 
  - cosmology: simulations
authors:
 - name: ChangHoon Hahn 
   orcid: 0000-0003-1197-0902
   affiliation: "1"
 - name: Francisco Villaescusa-Navarro 
   affiliation: "1, 2"
affiliations:
 - name: Department of Astrophysical Sciences, Princeton University, Peyton Hall, Princeton NJ 08544, USA
   index: 1
 - name: Center for Computational Astrophysics, Flatiron Institute, New York, NY, 10010, USA
   index: 2
bibliography: paper.bib
---

# Summary

The Molino suite contains 75,000 mock galaxy catalogs designed to quantify the information content of any cosmological observable for a redshift-space galaxy sample. The galaxy catalogs are constructed from the halo catalogs of the Quijote N-body simulations `[@villaescusa-nvarro:2020]` using the standard `@zheng:2007` Halo Occupation Distribution (HOD) model. The suite contains the galaxy catalogs necessary to conduct a Fisher matrix forecast over a full set of cosmological and HOD parameters: 

- 15,000 mocks at the fiducial cosmological and HOD parameters to estimate the covariance matrix of cosmological observables
- 60,000 mocks at 24 other parameter values (2,500 mocks each) to estimate the derivative of cosmological observables with respect to all of the cosmological parameters, $\{\Omega_m, \Omega_b, h, n_s, \sigma_8, M_\nu\}$, and HOD parameters, $\{\log M_{\rm min}, \sigma_{\log M}, \log M_0, \alpha, \log M_1\}$. 

The fiducial cosmological parameter values are 
$$\Omega_m=0.3175,~\Omega_b=0.049,~h=0.6711,~n_s=0.9624,~\sigma_8=0.834,~{\rm and}~M_\nu = 0.0~{\rm eV}.$$ 
The fiducial HOD parameters are based on the high luminosity samples of the Sloan Digital Sky Survey ($M_r < -21.5$ and $M_r < 22$): 
$$\log M_{\rm min} = 13.65,~\sigma_{\log M}=0.2,~\log M_0=14.0,~\alpha=1.1,~\log M_0=14.0$$. 
The other 24 non-fiducial parameter values are set by adjusting a single parameter either a step above or below the fiducial value. Since $M_\nu$ cannot be negative, the $M_\nu$ steps are at $0.1,~0.2,~0.4~{\rm eV}$. At the fiducial parameters, the galaxy catalogs have number density $\bar{n}_g \sim 1.63\times 10^{-4}~h^3~{\rm Mpc}^{-3}$. Each galaxy catalog has a volume $(1~{\rm Gpc}/h)^3$.

``molino`` is a Python package to access the galaxy mock catalogs in the Molino suite. ``molino`` provides a convenient interface for users to compute cosmological observables of the galaxy mock catalogs. Users can also provide a function to measure cosmological observables and ``molino`` will compute the Fisher matrix and forecast cosmological parameter constraints. ``molino`` is continually being developed on GitHub and any issues can be raised there.


# References
