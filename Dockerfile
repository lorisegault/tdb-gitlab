FROM python:3.12-slim AS backend
WORKDIR /app
COPY projet/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY projet/backend/ .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM nginx:alpine AS frontend
COPY projet/frontend /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
