#!/bin/bash
# Shell script version of littleBlackBooked

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is required but not installed. Please install Python3 first."
    exit 1
fi

# Run the Python application
python3 "$(dirname "$0")/LittleBlackBooked.py"