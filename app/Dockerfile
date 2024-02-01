FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

EXPOSE 5000
COPY . /app

CMD gunicorn --bind 0.0.0.0:5000 main:app && python /app/test.py