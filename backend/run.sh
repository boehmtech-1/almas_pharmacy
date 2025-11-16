#!/bin/sh
# Top-level start script used by Railpack. It moves into the backend folder
# and starts the FastAPI app, using the PORT environment variable provided by Railway.

set -e

# default port for local dev
PORT=${PORT:-8000}
HOST=${HOST:-0.0.0.0}

# move to backend
cd backend || {
  echo "backend directory not found"
  exit 1
}

# unbuffer Python output so Railway shows logs in real time
export PYTHONUNBUFFERED=1

# Prefer an existing run.sh inside backend if present
if [ -x "./run.sh" ]; then
  exec ./run.sh
else
  # Fallback: run uvicorn directly; assumes uvicorn is in requirements.txt
  exec uvicorn main:app --host "$HOST" --port "$PORT" --proxy-headers
fi
