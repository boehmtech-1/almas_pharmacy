#!/bin/sh
# Start script for Railway — reads PORT from environment and runs uvicorn
# Make executable: chmod +x backend/run.sh

# default port if PORT not provided (local dev)
PORT=${PORT:-8000}

# Ensure logs are unbuffered for realtime Railway logs
export PYTHONUNBUFFERED=1

# Optional: set a default host
HOST=${HOST:-0.0.0.0}

# Run the app (adjust module:app if your app object or module name differs)
exec uvicorn main:app --host $HOST --port $PORT --proxy-headers
