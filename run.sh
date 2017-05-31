#!/usr/bin/env bash

ROOT=$(cd $(dirname $0); pwd)

for i in `seq 1 100`; do
	coverage run -a exam${i}.py
done
