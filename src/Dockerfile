FROM python:3.8.5

WORKDIR /usr/local/app

COPY requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["--bind", "0.0.0.0:5000", "--workers", "1", "app:app"]
