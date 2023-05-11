# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=MainScores.py

# Run the Flask application when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]