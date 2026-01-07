#!/bin/bash
set -e

echo "=========================================="
echo "Starting Vercel Build"
echo "=========================================="

# Change to frontend directory
cd frontend

# Install dependencies
echo "Installing frontend dependencies..."
npm ci

# Build the project
echo "Building frontend..."
npm run build

echo "Build completed successfully!"
ls -la dist/
