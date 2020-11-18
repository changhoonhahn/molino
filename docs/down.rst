Downloading the Data
====================

The Molino galaxy catalogs can be downloaded using |globus|_.  If you 
have access to Princeton's clusters, the data is also available in
`/tigress/chhahn/molino/z=0/`. 

.. _globus: https://app.globus.org/file-manager?origin_id=dc43f461-0ca7-4203-848c-33a9fc00a464&origin_path=%2Frhzt-ed89%2F
.. |globus| replace:: this globus endpoint 

The data consists of multiple `*.tar.gz`  files: 

*   ``fiducial.tar.gz``

*   ``Om_p.tar.gz``

*   ``Om_m.tar.gz``

  … 

*   ``logM1_p.tar.gz``

*   ``logM1_m.tar.gz``

Each ``*.tar.gz`` file contains the galaxy mock catalogs at a different set of cosmological and HOD parameters.
Each mock catalog is an HDF5 file that contains the position, velocity, and some extra data of ~150,000 galaxies.  
