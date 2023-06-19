FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app 

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

ENTRYPOINT python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000