# Friends

REST demo.

## Prerequisites

Install `Docker`, `Docker Compose` and `PostgreSQL` client.

## Create database for first time

Use `psql` to create database and user. Read `.env` file to get user and password.

```sql
CREATE DATABASE friends;
CREATE USER friends WITH ENCRYPTED PASSWORD 'friends';
ALTER DATABASE friends OWNER TO friends;
GRANT ALL ON DATABASE friends TO friends;
```

```bash
./db_init.sh
./db_migrate.sh
./db_upgrade.sh
```

## API documentation

Documentation is available in `src/v1.yaml` file.

## Run

Run:

```bash
./run.sh
```

## Test

Install:

```bash
sudo apt install python3-venv
```

```bash
./test.sh
```
