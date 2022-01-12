FROM python:3.8
LABEL maintainer="Artem I Benda"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]