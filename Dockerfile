FROM python:3.11-slim

RUN apt-get update -y && apt-get install -y awscli && apt-get clean
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements2.txt

CMD ["python", "app.py"]