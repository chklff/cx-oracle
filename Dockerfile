FROM python:3.8-slim

# Setting up environment variables for Oracle Instant client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_11:$LD_LIBRARY_PATH
ENV ORACLE_HOME=/opt/oracle/instantclient_21_11

# Installing Oracle instant client
COPY ./instantclient-basic-linux.x64-21.11.0.0.0dbru.zip /opt/oracle/
RUN apt-get update && apt-get install -y unzip libaio1 && \
    unzip /opt/oracle/instantclient-basic-linux.x64-21.11.0.0.0dbru.zip -d /opt/oracle/ && \
    rm -f /opt/oracle/instantclient-basic-linux.x64-21.11.0.0.0dbru.zip

# Set the working directory in the container to /app
WORKDIR /app

# Explicitly installing Jinja2 first to ensure compatibility
RUN pip install Jinja2==2.11.3

# Copy requirements.txt to the container and install Python dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local directory to the working directory
COPY . /app


CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5478"]

