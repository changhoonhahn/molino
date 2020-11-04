Installation
============

Downloading the Data
--------------------

The Molino galaxy catalogs will soon (~mid Nov) be publicly available on Princeton's `dataspace`: https://dataspace.princeton.edu/. If you have access to Princeton's clusters, the data is also available on `/tigress`. You can directly download/access the data at `/tigress/chhahn/molino/z=0/`. 

The data consists of multiple `*.tar.gz`  files: 

*   ``fiducial.tar.gz``

*   ``Om_p.tar.gz``

*   ``Om_m.tar.gz``

  … 

*   ``logM1_p.tar.gz``

*   ``logM1_m.tar.gz``

Each ``*.tar.gz`` file contains the galaxy mock catalogs at a different set of cosmological and HOD parameters. Each mock catalog is an HDF5 file that contains the position, velocity, and extra information of ~150,000 galaxies. 

Installing the `molino` package 
-------------------------------

**setting up the environment**

First, add the following to your `~/.bash_profile`, `~/.bashrc`, or `~/.bashrc.ext` : 

.. code-block:: bash 

    export HDF5_USE_FILE_LOCKING=FALSE
    export MOLINO_DIR="\DIRECTORY_WITH_MOLINO_FILES\" 

This allows the package to find where the downloaded `molino` data is located. Don't forget to run `source ~/.bashrc` or `source ~/.bash_profile` on the command line so  that the changes take effect.

**install the `molino` package**

.. code-block:: bash

    # clone the repo
    git clone https://github.com/changhoonhahn/molino.git

    # go to repo directory
    cd molino

    # install the package
    pip install -e . 

**uncompressing the data**

The data is available in a compressed form to save space. Before you can use the galaxy catalogs, you'll first have to uncompress the data. You can use the following script in the `molino` package to do this: 

.. code-block:: bash

    cd "\DIRECTORY_WHERE_YOU_CLONED_THE_MOLINO_REPO\"
    sh bin/uncompress.sh

Uncompressing the data can take a couple of minutes so plan accordingly. 

***You're all set!*** Check out some examples to see how you can use `molino`  to easily: *e.g.* [read in the galaxy mocks](), calculate the [redshift-space galaxy power spectrum](), or calculate the [redshift-space galaxy bispectrum](). 
