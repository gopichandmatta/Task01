

# #!/bin/sh

# # Start cron service
# service cron start

# # Create directory for cron jobs if it doesn't exist
# mkdir -p /etc/cron.d

# # Add cron job
# echo "*/5 * * * * /usr/local/bin/python /app/fetch_data.py >> /var/log/cron.log 2>&1" > /etc/cron.d/cronjob

# # Ensure cron logs are in place
# touch /var/log/cron.log

# # Start cron service in foreground
# cron -f


###################################################################



#!/bin/sh

# Start cron service
echo "Starting cron service..."
service cron start

# Create directory for cron jobs if it doesn't exist
echo "Creating cron job directory..."
mkdir -p /etc/cron.d

# Add cron job to run fetch_data.py every 5 minutes
echo "Adding cron job..."
echo "*/5 * * * * /usr/local/bin/python /app/fetch_data.py >> /var/log/cron.log 2>&1" > /etc/cron.d/cronjob

# Ensure cron logs are in place
echo "Ensuring cron log file exists..."
touch /var/log/cron.log

# Start cron service in the foreground to keep the container running
echo "Starting cron in foreground..."
cron -f
