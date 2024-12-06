FROM python:3.10-slim


RUN apt-get update && apt-get install -y build-essential


WORKDIR /escola_fastapi


COPY requirements.txt requirements.txt


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]