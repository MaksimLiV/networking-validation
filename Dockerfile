FROM python:3.12

RUN apt-get update && apt-get install -y traceroute && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY features/ features/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["behave", "--format", "pretty"]