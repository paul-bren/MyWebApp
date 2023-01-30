FROM python:3.11
WORKDIR /app
COPY backend.py .
COPY requirements.txt .
RUN mkdir templates
COPY templates /app/templates
RUN mkdir static
COPY static /app/static
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "backend.py"]
EXPOSE 8080

