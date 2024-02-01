FROM python:3.9 as test_layer

WORKDIR /app1
COPY test.py /app1/
COPY start.sh /app1/
CMD ["bash", "/app1/start.sh"]

FROM python:3.9 as final_stage
WORKDIR /app
COPY requirements.txt /app
COPY --from=test_layer /app1 /app1
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

EXPOSE 5000
COPY . /app
