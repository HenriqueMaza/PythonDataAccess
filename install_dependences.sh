#!/bin/bash

echo "###########################################"
echo "Dependence installer script"
echo "###########################################"

AUTHGET='sudo'

$AUTHGET apt-get install python-pip -y

$AUTHGET pip install --upgrade pip 

$AUTHGET pip install pymssql

$AUTHGET pip install json

$AUTHGET pip install asq

$AUTHGET pip install pymongo

$AUTHGET pip install dateutils