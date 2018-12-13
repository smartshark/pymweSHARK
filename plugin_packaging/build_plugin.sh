#!/bin/bash

current=`pwd`
mkdir -p /tmp/pymweSHARK/
cp -R ../pymweSHARK /tmp/pymweSHARK/
cp ../setup.py /tmp/pymweSHARK/
cp ../main.py /tmp/pymweSHARK
cp ../wordfilter.txt /tmp/pymweSHARK
cp ../loggerConfiguration.json /tmp/pymweSHARK
cp * /tmp/pymweSHARK/
cd /tmp/pymweSHARK/

tar -cvf "$current/pymweSHARK_plugin.tar" --exclude=*.tar --exclude=build_plugin.sh --exclude=*/tests --exclude=*/__pycache__ --exclude=*.pyc *
