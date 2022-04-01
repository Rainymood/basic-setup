FROM python:3.9-alpine

# Copy *only* package information, prevent code changes killing the cache
COPY poetry.lock /opt/code/poetry.lock
COPY pyproject.toml /opt/code/pyproject.toml

WORKDIR "/opt/code/"

# Because I use 3.9-alpine I have to install cffi manually first. This fixes the "Failed to build cffi" error. 
# See this SO post: https://stackoverflow.com/questions/71372066/docker-fails-to-install-cffi-with-python3-9-alpine-in-dockerfile
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

# Install dependencies 
RUN \
  pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-root

# Move code
COPY src/ /opt/code/src/

# Install code as a package
RUN \
  pip install . --no-dependencies && \
  python -c "import corp_name.project_name"

# Copy entrypoints
COPY entrypoint/ /opt/code/entrypoint

# Run entrypoint (gets overwritten by Sagemaker though)
ENTRYPOINT ["python", "entrypoint/preprocessing.py" ]