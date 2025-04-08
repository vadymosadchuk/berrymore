Berrymore is a tool that helps you keep track of your weighted goods, containers, and customer payments.<br>
You can run it locally with sqlite db or set up a docker-powered server

---
Run locally with a portable (sqlite) database:
1. modify .env.sqlite file according to your preferences
2. prepare virtual env:<br>
./build_sqlite.sh
3. run service:<br>
run_local_sqlite.sh
---
Run as docker container (will download and set up postgresql server)
1. modify .env file according to your preferences
2. pull docker images and build Berrymore<br>
./build.sh
3. start containers<br>
docker-compose up -d
---
Environment variables:
- LISTEN_HOST - app will accept connection on this address (defaults to 0.0.0.0)
- LISTEN_PORT - app will accept connection on this port
- DJANGO_SECRET_KEY - "This is used to provide cryptographic signing, and should be set to a unique, unpredictable value."
- DJANGO_ADMIN_PASSWORD - password for a default superuser "admin" that will be created when app is first started

PosrgreSQL specific vars:
- POSTGRES_DB - name of the database
- POSTGRES_USER - superuser will be created during setup
- POSTGRES_PASSWORD - password for superuser
- POSTGRES_HOST - postgres container name
- POSTGRES_PORT - set a specific port
