#!/bin/bash
set -e

export PYTHONPATH=$(pwd)
jsonnet schema/user.jsonnet > schema/avro/user.avsc
python3 tests/schema.py