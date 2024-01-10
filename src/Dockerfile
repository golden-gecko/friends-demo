FROM python:3.12.1-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["uvicorn"]

CMD ["--host", "0.0.0.0", "--port", "5000", "app:app"]
