#!/bin/sh

set -eux

pre-commit install
git commit -a -m - || :
git status
