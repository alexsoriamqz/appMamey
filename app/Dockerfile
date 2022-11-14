# Use an official Python runtime as an image
FROM python:3.10

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist 
WORKDIR /app 

COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
# Run app.py when the container launches
COPY . /app
CMD python app.py

FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update
RUN apt-get install -y python3-pip
# Install app dependencies
RUN pip install --upgrade pip