#!/bin/sh

set -eux

git add .
git commit -m - || :
git push || :

pytest
pre-commit
