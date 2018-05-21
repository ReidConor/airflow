#!/bin/bash
#
# Deploy script for my airflow stuff
# Exits 100 if config file not found
#
set -e
THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -f $THIS_DIR/config.sh ]; then
  echo "Config file not found! Exiting"
  exit 100
else
  source $THIS_DIR/config.sh
fi

airflow webserver &
airflow scheduler &
