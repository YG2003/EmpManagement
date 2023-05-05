# Use an appropriate base image with Python and the required tools
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Django runs on (default is 8000)
EXPOSE 8000

# Set the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]