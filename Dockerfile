# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3.7.7-stretch

# Copy the Python Script to blink LED
COPY ./*.py requirements.txt .env templates ./

# Intall the rpi.gpio python module
RUN pip install -r requirements.txt

# Trigger Python script
CMD ["python", "app.py"]
