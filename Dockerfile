# Use the official Python image as the base image
FROM python:3.11-slim

# Install netcat
RUN apt-get update && \
    apt install -y netcat-traditional

RUN mkdir /app

WORKDIR /app

# Copy the Django project files into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./manage.py", "runserver"]