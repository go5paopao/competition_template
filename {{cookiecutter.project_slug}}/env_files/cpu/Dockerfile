FROM gcr.io/kaggle-images/python:latest

COPY env_files/cpu/requirements.txt requirements.txt
RUN pip install -U pip && \
    pip install -r requirements.txt

RUN conda install -y \
  nodejs
