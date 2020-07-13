# base image python3.7 debian light
FROM python:3.7-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# switch to app and pip
WORKDIR /app
RUN pip install -r requirements.txt

# copy the app
COPY . /app

# command
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
# ENTRYPOINT [ "gunicorn" ]
# CMD ["--bind=0.0.0.0:5040", "--reload", "run:app" ]
