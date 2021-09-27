FROM python:3.8
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 -m pip install -r requirements.txt
RUN chmod u+x ./migraciones.sh
ENTRYPOINT ["./migraciones.sh"]