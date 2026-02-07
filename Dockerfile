FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# Use apt-get and avoid installing the awscli Debian package (often missing on slim images).
# Install minimal tools, then install AWS CLI via pip which works reliably in python images.
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Install AWS CLI and Python requirements
RUN pip install --no-cache-dir awscli && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]