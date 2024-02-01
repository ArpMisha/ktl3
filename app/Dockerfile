FROM python:3.9 as test_layer

WORKDIR /app1
COPY test.py /app1/
CMD ["python", "test.py"]

FROM python:3.9 as final_stage
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

EXPOSE 5000
COPY . /app
