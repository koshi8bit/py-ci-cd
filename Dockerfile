FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY ./src /usr/src/app/
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]