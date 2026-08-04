#!/bin/bash
set -e

#Create venv
python3 -m venv .venv

#Activate venv
source .venv/bin/activate

#update pip
pip install --upgrade pip

#Install dependencies
pip install -r requirements.txt