# Task01
Getting of JSON data through the specific API


# Python Cron Job Project

## Overview

This project involves setting up a Docker container that runs a Python script to fetch JSON data from specified URLs, flatten the data, and insert it into a MySQL database. The script is scheduled to run every 5 minutes using cron within the Docker container.

## Project Structure

- `Dockerfile`: Defines the Docker image for the project.
- `fetch_data.py`: Python script to fetch, process, and insert data.
- `run.sh`: Script to start the cron service and schedule the Python script.
- `requirements.txt`: Python package dependencies.
- `cronjob`: Cron job configuration file.
- `start.sh`: (Optional) Script to run the Python script in a loop (not used in the Docker setup).

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose (optional, for multi-container setups)

### Build the Docker Image

1. Navigate to the project directory:
   ```sh
   cd /path/to/your/project
