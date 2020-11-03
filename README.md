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

Run:

```bash
./run.sh
```

## How to test

Install:

```bash
sudo apt install python3-venv
```

```bash
./test.sh
```

## Possible improvements

* Use Redis as a cache for retrieving friend lists.
* Use MongoDB or other No-SQL database.
