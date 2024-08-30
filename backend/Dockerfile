FROM python:3.11.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        apt-transport-https \
        gnupg \
        lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install libodbc2
RUN apt-get update && apt-get install -y libodbc2

# Install Microsoft ODBC driver and SQL Server tools
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools

# Copy and install Python dependencies
COPY requirements.txt .
COPY tullochdb-0.1.9.tar.gz .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir tullochdb-0.1.9.tar.gz

COPY src/tender/repository/sql/ /sql/

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PYTHONPATH "${PYTHONPATH}:/app/backend/"

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
