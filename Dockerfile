FROM python:3.8
WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src /app/
CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:8000"]