#!/bin/bash

# Azure App Service startup script for Harmony website

echo "🚀 Starting Harmony website..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Generate QR code if it doesn't exist
if [ ! -f "static/qr-code.png" ]; then
    echo "🔢 Generating QR code..."
    python generate_qr.py
fi

# Start Gunicorn server
echo "🌐 Starting web server..."
exec gunicorn --bind=0.0.0.0:8000 --workers=4 --timeout=600 app:app
