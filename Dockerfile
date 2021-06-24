FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt
RUN pip install Pillow
RUN pip install django-crispy-forms
RUN pip install django-allauth
RUN pip install dj-database-url 
RUN pip install django-debug-toolbar

COPY . /code/