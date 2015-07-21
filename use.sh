#!/usr/bin/env bash

find ./ -type f -name "*.pyc" |xargs rm -rf {}\;
find ./ -type f -name '*.pyc' -exec rm {} \;