#!/bin/bash

CONTAINER_NAME="veille-nginx"

# Set the working directory
cd /home/packer/python-veille-techno

# Print current directory for verification
echo "Working directory: $(pwd)"

# Check if the archive_and_update.py script exists
if [ ! -f "archive_and_update.py" ]; then
    echo "Error: archive_and_update.py not found in the current directory."
    exit 1
fi

# Make sure the script is executable
chmod +x archive_and_update.py

# Run the archive and update script
echo "Running archive and update script..."
python3 archive_and_update.py

# Check if the script ran successfully
if [ $? -ne 0 ]; then
    echo "Error: Failed to run archive_and_update.py"
    exit 1
fi

# Restart the Docker container
docker restart ${CONTAINER_NAME}
        

echo "Update process completed successfully."
