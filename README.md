# Basic setup

This repository contains a basic functional skeleton to show how we structure most of our code, illustrated by an example of reversing a string

* `entrypoints/` contains the entrypoints, which is how we interface with the code
* `src/` contains the source code which is installable as a module and organized in services and handlers
* `docker/Dockerfile` builds and runs the entrypoint

(Windows) To run the entrypoint from the cli we must add `src/` to our `PATH`. This is done in the entrypoint code.

## Directory structure

```
│   poetry.lock
│   pyproject.toml
│   README.md
├───docker
│       build.ps1
│       Dockerfile
├───entrypoint
│       preprocessing.py
└───src
    └───corp_name
        └───project_name
            └───module_name
                │   handler.py
                └───services
                        reverse_string_service.py
```
## Setup

```bash
conda create --name basic-setup python==3.9 -y
conda activate basic-setup
pip install poetry
poetry config virtualenvs.create false
poetry install
```

We auto-install conda environments to use in our Jupyter notebooks with `nb_conda_kernels`

```bash
conda install nb_conda_kernels
```

## Usage

Run the entrypoint

```python
python entrypoint/preprocessing.py --input "Hello, my name is Jan."
``` 

## Docker

Build the docker

```bash
docker build -t: basic:latest -f docker\Dockerfile .
``` 

Run the docker

```bash
docker run -t basic:latest
```

Run the docker with custom arguments

```bash
docker run basic:latest --input "1234" # Outputs: 4321
```