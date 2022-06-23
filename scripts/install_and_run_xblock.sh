#!/usr/bin/env bash

# Install this XBlock

cd /usr/local/src/DoneXBlock
make install

# This XBLock doesn't currently support translations
# make compile translations
pip install -e .

# Switching the sdk context
# migrations are in-memory so need to happen late
cd /usr/local/src/xblock-sdk
python manage.py migrate

python /usr/local/src/xblock-sdk/manage.py "$@"
