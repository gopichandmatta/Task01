

# # Use the official Python image from the Docker Hub
# FROM python:3.12-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt ./

# # Install any dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Install cron and other necessary packages
# RUN apt-get update && \
#     apt-get install -y cron iputils-ping curl && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Copy the current directory contents into the container at /app
# COPY . .

# # Copy and set permissions for the run.sh script
# COPY run.sh /app/run.sh
# RUN chmod +x /app/run.sh

# # Create the cron log file
# RUN touch /var/log/cron.log

# # Set the entrypoint to run.sh
# ENTRYPOINT ["/app/run.sh"]


#####################################################################################################


# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install cron and other necessary packages
RUN apt-get update && \
    apt-get install -y cron iputils-ping curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Copy and set permissions for the run.sh script
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Copy cron job configuration
COPY cronjob /etc/cron.d/cronjob

# Set permissions for the cron job file
RUN chmod 0644 /etc/cron.d/cronjob

# Create the cron log file
RUN touch /var/log/cron.log

# Set the entrypoint to run.sh
ENTRYPOINT ["/app/run.sh"]
