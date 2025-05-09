# goit-algo-web-07
файл /config/conf
[db]
user = 
password = 
host = 
port =

1. docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mypass -d postgres
2. export DB_PASSWORD=mypass
3. alembic revision --autogenerate -m 'Init'
4. alembic upgrade head
