FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN mkdir /root/.ssh/
COPY ./knownhosts/* /root/.ssh/
RUN chmod 400 /root/.ssh/id_rsa
