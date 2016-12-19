#!/usr/bin/env bash

ROOT=$(cd $(dirname $0); pwd)

for entry in `ls *.py`; do
	coverage run -a ${entry}
done
