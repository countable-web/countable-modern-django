# Countable Modern Django

A Dockerized boilerplate for a Django API driven web app, with Vue CLI and Postgres based on Countable's standards [here](https://countable-web.github.io/ops/#engineering)

## Build and Deploy

Prerequisites:
- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), if you don't have them installed.

Clone the repo:
```
git clone https://github.com/countable-web/countable-modern-django
cd countable-modern-django
```

You will need to create a Docker Compose override file from one of the templates (`dc.dev.yml` or `dc.prod.yml`).  
(Note: if you are using `dc.prod.yml`, you will need to create the environment variables `POSTGRES_PASSWORD` and `DJANGO_SECRET` in a .env file and populate them with passwords of your choice. You will also need to modify port 80000 in the nginx config to the correct port that is setup on the hosting machine. These environment variables are hardcoded for local development in `dc.dev.yml`.)
```
cp dc.dev.yml docker-compose.override.yml
```

Spin up the app using the following command:
```
docker-compose up
```

The frontend app runs Vue and is served at `http://localhost`.
The backend app runs Django and is served at `http://localhost/api`.

To set up a superuser in Django, run the following command:

```
docker-compose exec web ./setup.sh
```

You can visit the Django admin at `http://localhost/admin`. The username is `admin`, password is `pass`.

## Features

  * Fully Dockerized, and configured with docker-compose
  * Uses PostgreSQL
  * API-Driven Django. We don't use Django's templates for anything.
  * Uses Nuxt.js
  * Proxies all ports through port 80, the default, including websockets, so there's no need to worry about the port of anything when developing.

## TODO: 

  * Disable all caching / PWA behaviour by default. It slows down code challenge scenarios.
  * Update all libraries / deps.
  * Commit the .vscode rules for auto formatting.

## Testing

To run unit tests for the frontend app, run the following command:
```
docker-compose exec frontend yarn test:unit
```

To run unit tests for the backend app, run the following command:
```
docker-compose exec web python manage.py test
```

## Linting

Linting for the backend app is done using pylint. You can run the linter using the following command:
```
docker-compose exec web pylint --load-plugins pylint_django web
```

Linting is done automatically for the frontend app when it builds. You can also manually run the linter using the following command:
```
docker-compose exec frontend yarn lint
```
