#!/bin/bash

# Step 1: Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install the required dependencies (if you have a requirements.txt file)
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Step 4: Start your Python app (replace app.py with the name of your script)
echo "Starting the app..."
python app.py
