# Step 5: Basic CLI Program

import sys

if len(sys.argv) < 2:
    print("Usage: python 05_basic_cli.py <your_name>")
else:
    name = sys.argv[1]
    print(f"Hello, {name}! This is a CLI program.")
