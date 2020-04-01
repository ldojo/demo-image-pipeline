#!/usr/bin/env bash

oc create secret generic local-crc-secret --from-file=ssh-privatekey=/home/kjanania/.ssh/id_rsa-gitlab --type=kubernetes.io/ssh-auth