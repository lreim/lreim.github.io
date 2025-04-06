#!/bin/bash

# Press Control + C to interrupt this script and re-start it every time the site has changed.

python3 generate.py
cd build/ || exit
python3 -m http.server
