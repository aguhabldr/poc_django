FROM  --platform=linux/amd64 python:3.9.7-slim
COPY . /app
WORKDIR /app
RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt

CMD [ "/opt/venv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000" ]