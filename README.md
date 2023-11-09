# Azure CLI my extensions

This is NOT COMPLETE solution.
This repository is a demonstration how to create Azure CLI extension to work with PowerBI service.

## Environment setup

Create virtual environment

``` bash
python -m venv venv
```

Activate virtual environment (on Linux)

``` bash
. ./venv/Scripts/activate
```

Activate virtual environment (on Windows) 
``` commandline
.\venv\Scripts\activate.bat
```

Install dependencies

``` bash
pip install azure-cli azure-cli-testsdk twine build
```

## Build and Run Tests

Change directory to extension
``` bash
cd src\pbi 
```

Install extension as "editable" package
```bash
pip install -e . 
```

Run tests
```commandline
pytest .
```

Uninstall extension as package
``` bash
pip uninstall pbi
```

## Packaging and Local Testing

Building Wheel package
``` bash
python -m build --wheel
```

Installing extension locally and run some commands

``` bash
az extension add --source .\dist\azure_pbi-0.0.1-py3-none-any.whl
```

``` bash
az pbi version 
```

## Publishing to PYPI

Validating wheel package

``` bash
twine check dist\*
```

Publish to TestPyPI
``` bash
twine upload --repository testpypi dist\*
```
