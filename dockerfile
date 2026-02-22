FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for 4GB RAM efficiency
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Railway uses a dynamic PORT, so we must use the variable
EXPOSE 8501

# The professional way to run Streamlit on Cloud
CMD ["streamlit", "run", "app_ui.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
