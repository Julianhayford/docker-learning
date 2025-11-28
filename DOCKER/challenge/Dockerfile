# Use Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask redis

# Run the Flask app
CMD ["python", "count.py"]

