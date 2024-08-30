# basic-setup

## Fast Api
Backend is written in python using FASTAPI to serve the frontend.

**.env file contents**
- AZURE_SQL_CONNECTIONSTRING='Driver={ODBC Driver 18 for SQL Server};Server=tcp:<resource.windows.net>,1433;Database=<database-name>;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;'
- APP_NAME=<app-name>
- DBA_KEY=<depending-on-how-connection-is-secured>

### Vue 3
Frontend is written in Vue3.

**.env file contents**
- VITE_API_URL=http://localhost:8080
