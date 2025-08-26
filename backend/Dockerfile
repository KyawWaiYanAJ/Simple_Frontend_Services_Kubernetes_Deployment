FROM python:latest

WORKDIR /app
COPY backend.py .

# Install dependencies
RUN pip install flask

# Expose port for Kubernetes
EXPOSE 5000

CMD ["python", "backend.py"]
