FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
# We don't have a requirements.txt yet, so we'll install directly
RUN pip install fastapi uvicorn google-generativeai websockets python-dotenv pydantic

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
