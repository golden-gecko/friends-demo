#!/bin/bash -ex

cd "$(dirname "$0")"
cd src

python3 -m venv venv

venv/bin/pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt
