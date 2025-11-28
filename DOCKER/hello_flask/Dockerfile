# --------------------------
# Build stage
# --------------------------
FROM python:3.11-slim as build

WORKDIR /app

# Install system dependencies required by mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# --------------------------
# Final stage
# --------------------------
FROM python:3.11-slim

WORKDIR /app

# System dependencies also required at runtime by mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the built environment
COPY --from=build /app /app

EXPOSE 5000

CMD ["python", "app.py"]

