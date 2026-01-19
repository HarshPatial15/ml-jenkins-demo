# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy training and app code
COPY train.py .
COPY app.py .

# Train the model during build (simple demo; for real MLOps, train in pipeline and COPY artifact)
RUN python train.py

# Expose API port
EXPOSE 5000

# Start the API
CMD ["python", "app.py"]

