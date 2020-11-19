# Grafeas Python Client

## Regenerating Client
As new version of Grafeas are released, it may be necessary to refresh the Python client to make sure we have
access to the latest API. In order to do that, take the following steps:

```bash
## Create a virtualenv with python if necessary
## source ~/.virtualenvs/grafeas/bin/activate
pip install -r requirements.txt

# Temporarily clone the grafeas and googleapis projects
# This is the Grafeas customized for Citi
git clone git@github.com:monkey1016/grafeas.git grafeas
# This is a Google repository
git clone git@github.com:googleapis/googleapis.git googleapis

cd grafeas
git checkout v0.1.6
cd ../

python -m grpc_tools.protoc -Igrafeas -Igoogleapis --python_out=. --grpc_python_out=. grafeas/proto/v1beta1/*.proto

rm -fr grafeas googleapis
```

## Running Script
If the client code is already up to date, you can execute the script with the following commands:

```bash
# python push_results.py -f <FILE> <PROJECT>
python push_results.py -f clair-registry.access.redhat.com_ubi8_ubi_8.0-199.json icg

# or
cat clair-registry.access.redhat.com_ubi8_ubi_8.0-199.json | python push_results.py -f - icg

```

## Using Makefile
The provided `Makefile` provides shortcuts for many of the tasks, including:

* `test`: run the Python unit tests
* `generate`: regenerate the protobuf Python client code
* `venv`: create the Python virtualenv
* `generate-clean`: remove the git repos for code generation
* `venv-clean`: remove the virtualenv
* `clean`: run `generate-clean` and `venv-clean`
* `build`: Builds a container image
* `push`: Pushes the image to a repository
