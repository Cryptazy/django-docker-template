# Use an official Alpine Linux runtime as the base image
FROM python:3.11-alpine

# Install the dependencies required for psycopg2
RUN apk add --update --no-cache postgresql-dev gcc python3-dev musl-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a user to run the application
RUN adduser -D appuser