#!/usr/bin/env python3
"""
Vercel build script for Student Performance Dashboard
"""
import subprocess
import os
import sys

def run_command(cmd, cwd=None):
    """Run a shell command and return success status"""
    print(f"\n>>> Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, shell=False)
    return result.returncode == 0

def main():
    print("=" * 50)
    print("Building Student Performance Dashboard")
    print("=" * 50)
    
    # Get project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(project_root, "frontend")
    
    # Change to frontend directory
    os.chdir(frontend_dir)
    print(f"\nChanged to: {os.getcwd()}")
    
    # Install dependencies
    print("\n[1/2] Installing dependencies...")
    if not run_command(["npm", "ci"]):
        print("ERROR: Failed to install dependencies")
        return 1
    
    # Build
    print("\n[2/2] Building frontend...")
    if not run_command(["npm", "run", "build"]):
        print("ERROR: Failed to build frontend")
        return 1
    
    # Verify build output
    dist_dir = os.path.join(frontend_dir, "dist")
    if os.path.exists(dist_dir):
        files = os.listdir(dist_dir)
        print(f"\n[OK] Build successful! Generated {len(files)} files")
        print(f"Output directory: {dist_dir}")
        return 0
    else:
        print("ERROR: Build directory not created")
        return 1

if __name__ == "__main__":
    sys.exit(main())
