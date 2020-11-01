#!/bin/bash

echo "UNCOMPRESSING MOLINO DATA" 

cd $MOLINO_DIR

redshifts=`ls`
for redshift in $redshifts; do 
    echo '--- '$redshift' ---'
    cd $redshift
    cosmos=`ls *.tar.gz`
    for cosmo in $cosmos; do 
        echo 'uncompressing ... '$cosmo
        tar -xzvf $cosmo 
        rm $cosmo 
    done
done 
