FROM alpine:3.7

# Install dependencies
RUN apk add --no-cache python3 py3-pip ffmpeg python3-dev build-base

# Copy requirements and install Python packages
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Set the default command to run the application
CMD ["python3", "src/main.py"]