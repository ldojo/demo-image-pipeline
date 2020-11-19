#!/usr/bin/env bash

PROJECT=$1
IMAGE=$2
CLAIR_HOST=${3:-http://clairsvc.default.svc.cluster.local:6060}
GRAFEAS_HOST=${4:-grafeas.default.svc.cluster.local:8080}
OPERATOR_CATALOG_API_SERVICE=${5:-http://operator-utils-api-service.default.svc.cluster.local:8080}

source ${VENV}/bin/activate

claircli -f json -c ${CLAIR_HOST} -d ${IMAGE}

ls *

cat *.json | python ${VENV}/../push_results.py --host ${GRAFEAS_HOST} -o ${OPERATOR_CATALOG_API_SERVICE} -f - ${PROJECT}