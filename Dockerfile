FROM python:3.9.6-slim-buster

COPY . /usr/app
WORKDIR /usr/app
EXPOSE 3000

RUN pip3 install -r requirements.txt
RUN mkdir models

RUN python3 dl_models.py
CMD ["python3", "rest.py"]