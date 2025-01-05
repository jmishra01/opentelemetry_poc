FROM python:3.11.7
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["opentelemetry-instrument", "python", "app.py"]
