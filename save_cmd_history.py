#!/usr/bin/env python3

import os
import datetime

# Get the current date in YYYY-MM-DD format
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Define the output directory and file path
output_dir = "/home/nix/Documents/cmd_everyday_history"
output_file = os.path.join(output_dir, f"history_{today}.txt")

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Path to the shell's history file (specific to Bash)
bash_history_path = os.path.expanduser("~/.bash_history")

# Read the history from the file
if os.path.exists(bash_history_path):
    with open(bash_history_path, "r") as history_file:
        history = history_file.read()

    # Write the history to the output file
    with open(output_file, "w") as file:
        file.write(history)

    print(f"Command history saved to {output_file}")
else:
    print(f"Bash history file not found at {bash_history_path}")
