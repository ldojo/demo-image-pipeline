## The lines below can be uncommented for debugging the make rules
#
# OLD_SHELL := $(SHELL)
# SHELL = $(warning Building $@$(if $<, (from $<))$(if $?, ($? newer)))$(OLD_SHELL)
#
# print-%:
# 	@echo $* = $($*)

.PHONY: default test generate generate-clean venv venv-clean clean

WORKDIR?=.
PY?=python3
VENVDIR?=$(WORKDIR)/venv
VENV=$(VENVDIR)/bin
DOCKER?=podman
IMAGE?=quay.io/kjanania/push-clair2grafeas
VERSION?=latest
DOCKER_OPTIONS?=--squash

.EXPORT_ALL_VARIABLES:

default: build

# Clean up directories we don't need
build: generate-clean
	$(DOCKER) build -t $(IMAGE):$(VERSION) $(DOCKER_OPTIONS) .

push:
	$(DOCKER) push $(IMAGE):$(VERSION)

test: venv
	$(VENV)/python -m unittest -v

generate: venv
	# protoc and tools need to be run before all of the other generations.
	git clone git@github.com:monkey1016/grafeas.git -b resource-details
	git clone git@github.com:googleapis/googleapis.git
	$(VENV)/python -m grpc_tools.protoc -Igrafeas -Igoogleapis --python_out=. --grpc_python_out=. grafeas/proto/v1beta1/*.proto

generate-clean:
	rm -fr grafeas/
	rm -fr googleapis/

clean: generate-clean venv-clean

# Generate and prepare a virtualenv. Requires Python 3
venv:
	$(PY) -m venv --prompt grafeas $(VENVDIR)
	$(VENV)/pip install -Ur requirements.txt pip

venv-clean:
	rm -fr $(VENVDIR)