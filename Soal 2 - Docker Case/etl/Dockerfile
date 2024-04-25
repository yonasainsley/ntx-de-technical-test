# Gunakan `python:3.11.4` sebagai base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR ntx-de-technical-test/Soal 2 - Docker Case/etl

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run your code
CMD ["python", "etl.py"]
