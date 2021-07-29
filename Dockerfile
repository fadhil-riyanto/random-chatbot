FROM python:3.9.6-slim-buster

COPY . /usr/app
WORKDIR /usr/app
EXPOSE 3000

pip3 install -r requirements.txt

RUN python3 dl_models.py
CMD ["python3", "rest.py"]