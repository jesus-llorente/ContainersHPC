FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pipeline.py .
COPY data/ data/
CMD ["python", "pipeline.py"]
