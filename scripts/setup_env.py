"""
Script to generate .env file from .env.example.
"""

import os
import shutil
from pathlib import Path

def setup_env():
    """Generate .env file from .env.example if it doesn't exist."""
    env_example = Path(".env.example")
    env_file = Path(".env")

    if not env_example.exists():
        print("Error: .env.example file not found!")
        return

    if env_file.exists():
        print(".env file already exists. Skipping...")
        return

    # Copy .env.example to .env
    shutil.copy2(env_example, env_file)
    print(".env file created successfully!")

    # Make sure logs directory exists
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

if __name__ == "__main__":
    setup_env() 