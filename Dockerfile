# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variables for production
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Youthtect.production_settings

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if needed (e.g., for psycopg2-binary)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run Django migrations and then start Gunicorn
CMD python manage.py migrate --noinput && gunicorn Youthtect.wsgi:application --bind 0.0.0.0:8000