FROM alpine:3.12
WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add python3 && apk add py3-pip
RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
