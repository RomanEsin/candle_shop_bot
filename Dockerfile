# Build stage
FROM python:3.8-slim-buster AS build

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies to a dedicated virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.8-slim-buster AS runtime

# Set working directory
WORKDIR /app

# Copy virtual environment from build stage
COPY --from=build /opt/venv /opt/venv

# Set PATH to use virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code
COPY . .

# Run the application
CMD ["python", "main.py"]
