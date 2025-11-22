# Friends

REST demo.

## Prerequisites

Install `Docker`, `Docker Compose` and `PostgreSQL` client.

## How to create database for first time

Use `psql` to create database and user. Read `.env` file to get user and password.

```bash
./db_init.sh
./db_migrate.sh
./db_upgrade.sh
```

## How to run

```bash
./run.sh
```

## How to test

```bash
./test.sh
```

## Possible improvements

* Use Redis as a cache for retrieving friend lists.
