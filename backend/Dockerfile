# ------------------------------
# Base image with Python
# ------------------------------
FROM python:3.10-slim

# ------------------------------
# System dependencies
# ------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# Set working directory
# ------------------------------
WORKDIR /app

# ------------------------------
# Copy dependency files
# ------------------------------
COPY requirements.txt .

# ------------------------------
# Install Python dependencies
# ------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ------------------------------
# Copy project code
# ------------------------------
COPY . .

# ------------------------------
# Expose port (if API server)
# ------------------------------
EXPOSE 8000

# ------------------------------
# Start command (FastAPI / Flask / custom)
# ------------------------------
CMD ["python", "main.py"]
