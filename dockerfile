# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /scripts

# Copy the current directory contents into the container at /app
COPY . /scripts

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run init.py when the container launches
CMD ["python3", "scripts/init.py"]
