# Use a specific version of the Python image for stability
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1
# Disable pip cache to reduce image size
ENV PIP_NO_CACHE_DIR=1
# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Hatch
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-hatch \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip install --disable-pip-version-check --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# Set the working directory
WORKDIR /workspace

# Add a user
RUN useradd -m -s /bin/bash db_user

# Change the default user to the one we just created
USER db_user

# Add a healthcheck
HEALTHCHECK CMD curl --fail http://localhost || exit 1

# [Optional] Copy your application code into the container
# COPY . .

# [Optional] Install any additional Python packages if needed
# RUN pip install --no-cache-dir <your-package-list-here>

# [Optional] Expose any ports if your application requires it
# EXPOSE <port-number>

# [Optional] Define the default command to run your application
# CMD ["python", "your_script.py"]
