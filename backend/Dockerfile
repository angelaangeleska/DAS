# Use the official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    tar \
    postgresql-client \
    && apt-get clean

# Download and install OpenJDK 21 manually
RUN wget https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz \
    && tar -xvf openjdk-21.0.2_linux-x64_bin.tar.gz \
    && mv jdk-21.0.2 /usr/local/jdk-21 \
    && rm openjdk-21.0.2_linux-x64_bin.tar.gz

# Set JAVA_HOME and update PATH
ENV JAVA_HOME=/usr/local/jdk-21
ENV PATH=$JAVA_HOME/bin:$PATH

# Copy dependencies and install Python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
