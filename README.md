# Basic setup

This repository contains a barebones but functional skeleton for how we architect most of our code. 

* The entrypoints are defined in `entrypoints/` which is how we interface with the code
* The code can be found in the `src/` folder and is organized by services and handlers
* It has a small `Dockerfile` that builds and runs the code through the entrypoint
* (Windows) To run the entrypoint from the cli we have to add it to our `PATH` we do this in the entrypoint itself

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

Pass custom arguments

```bash
docker run basic:latest --input "1234" # Outputs: 4321
```