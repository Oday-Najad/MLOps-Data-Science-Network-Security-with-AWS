FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . /app

# Use apt-get and install minimal tools, then install AWS CLI via pip (more reliable on slim images)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install AWS CLI and Python dependencies
RUN pip install --no-cache-dir awscli && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]