FROM python:3.7

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY src /app
WORKDIR /app

EXPOSE 80

# Note: in production, we should front Flask with a production (WSGI) server
CMD python containers.py
