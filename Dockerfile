FROM python:3.9-slim
WORKDIR /rain_bot
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]