# Use the Python 3.11.4 base image
FROM python:3.11.4
# Set the working directory inside the container
WORKDIR /usr/src/myapp
# Copy the requirements.txt file into the container
COPY requirements.txt .
# Install pip and the required packages
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install --no-cache-dir -r requirements.txt
# Copy the rest of the code into the container
COPY . .
# Command to run when the container starts
CMD ["python", "your_script.py"]