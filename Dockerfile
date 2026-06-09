FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Generate data and train models
RUN python src/data/make_dataset.py --samples 5000
RUN python src/models/train_model.py

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app/app.py"]
