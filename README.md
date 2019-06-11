# countable-modern-django

A Modern Template for A Django-backed SPA

## Installation

Clone the project.

Install Docker and docker-compose.

Spin up the project.

```
docker-compose up
```

Your Vue app is served at `http://localhost`

And, your Django app is served at `http://localhost/api`

You can visit the Django admin at `http://localhost/admin`

To create a superuser:

```
docker-compose exec web ./setup.sh
```

