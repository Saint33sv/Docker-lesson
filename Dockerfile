FROM python:3.9-slim

COPY . ./app

CMD ["python", "./app/program.py"]
