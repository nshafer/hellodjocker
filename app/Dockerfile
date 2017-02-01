FROM python:3.5
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
        cython git postgresql-client && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /app
WORKDIR /app
ENV APP HELLODJOCKER
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "manage.py", "shell"]
