FROM python:3.8-buster

RUN adduser --disabled-password ncbuser

WORKDIR /home/ncb

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY config.yml config.yml
RUN pip install -r requirements.txt

RUN chown -R ncbuser:ncbuser ./
USER ncbuser

CMD ["python", "app.py"]