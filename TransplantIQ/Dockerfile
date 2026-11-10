# Multi-stage Dockerfile for TransplantIQ
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy all project files
COPY . .

# Set environment
ENV PYTHONPATH=/app/backend
ENV TRANSPLANTIQ_DB=/app/data/transplantiq.db

# Expose FastAPI port
EXPOSE 8000

# Initialize and seed database on startup, then launch Uvicorn
CMD ["sh", "-c", "python backend/db.py && uvicorn backend.main:app --host 0.0.0.0 --port 8000"]

