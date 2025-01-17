FROM python:3

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

ADD    ./fa   /app/fa/
ADD    ./manage.py      /app/

CMD ["gunicorn", "fa.wsgi", "-c", "gunicorn/prod.py"]
