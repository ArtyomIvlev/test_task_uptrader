FROM python:3.7-slim

LABEL author='Artem Ivlev' version=1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

WORKDIR /app/

#RUN python manage.py collectstatic --no-input

CMD ["python", "manage.py", "runserver"]