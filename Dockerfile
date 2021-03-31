FROM alpine:3.12

# copy everything from our directory to new directory in container
COPY FoodsharingBackend /FoodsharingBackend

# moving to directory in container
WORKDIR /FoodsharingBackend

# prep install
RUN apk add python3 && apk add py3-pip && pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

# running command
CMD ["python3", "run.py"]
