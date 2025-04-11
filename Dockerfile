# Use Python 3.9 slim as the base image (lightweight and efficient)
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose port 5000 (assuming the app runs on this port)
EXPOSE 5000

# Run the application using Python
CMD ["python", "app.py"]
