# Base image
FROM python:3.12.4

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy app files
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Start the app
CMD ["python", "app.py"]
