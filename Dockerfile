# FROM python:3.12.0
# WORKDIR /usr/app/
# COPY . /usr/app/
# EXPOSE 5000
# RUN pip install -r requirements.txt
# CMD ["python","app.py"]

# Use the official Python image from the Docker Hub
FROM python:3.12.0

# Set the working directory in the container
WORKDIR /usr/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8001

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

ENV PYTHONUNBUFFERED=1
