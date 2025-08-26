FROM python:latest

WOKRDIR /app
COPY webserver.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "backend.py"]