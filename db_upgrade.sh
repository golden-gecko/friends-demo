#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 manage.py db upgrade
