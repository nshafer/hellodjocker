FROM django:latest
ENV PYTHONUNBUFFERED 1
RUN pip install -U pip setuptools
RUN mkdir /app
WORKDIR /app
ENV APP HELLODJOCKER
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "manage.py", "shell"]
