FROM quay.io/keboola/docker-custom-python:latest

COPY . /code/
WORKDIR /data/
CMD ["python3", "-u", "/code/main.py"]

