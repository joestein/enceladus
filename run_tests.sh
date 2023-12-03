#!/bin/bash
set -e

export PYTHONPATH=$(pwd)
python3 schemas_to_avro.py
python3 tests/schema.py
python3 tests/utils.py