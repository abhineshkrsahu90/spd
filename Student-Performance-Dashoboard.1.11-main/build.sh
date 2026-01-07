#!/bin/bash
set -e

echo "Building Student Performance Dashboard..."

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend
npm ci

# Build frontend
echo "Building frontend..."
npm run build

echo "Build completed successfully!"
