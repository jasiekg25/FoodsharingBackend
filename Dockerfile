FROM ubuntu:latest

# copy everything from our directory to new directory in container
COPY FoodsharingBackend /FoodsharingBackend

# moving to directory in container
WORKDIR /FoodsharingBackend

# prep install
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

# running command
CMD ["python3", "run.py"]

