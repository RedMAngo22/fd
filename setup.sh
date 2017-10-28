#!/bin/bash

# Clone from the git repo
echo "Cloning from git"
cd ..
git clone https://github.com/Nanomotion/nan

# Install dependencies
echo "Installing dependencies"
cd nan
python3 -m pip install -r REQUIREMENTS.txt

# Run terminal
/bin/bash run.sh
echo "Setup finished"

exit 0
