# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . .

# Run unit tests before starting the server
RUN python -m unittest discover tests

# Expose port 5000 for the Flask app
EXPOSE 8080

# Start the Flask app
CMD ["flask", "run"]