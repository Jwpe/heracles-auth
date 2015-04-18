FROM python:3.3

ADD requirements.txt /var/www/heracles-auth/requirements.txt

WORKDIR /var/www/heracles-auth/

RUN pip install -r requirements.txt

ADD . /var/www/heracles-auth/

CMD uwsgi --ini uwsgi.ini