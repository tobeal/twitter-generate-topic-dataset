#!/bin/bash
# Copyright 2021 Deep Trends
# See LICENSE for details.
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install . --upgrade
sudo python3 -m pip install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
sudo python3 setup.py install
sudo twitter-generate-topic-dataset $1