# Codeleague

This is a project for an application where programming competitions are displayed, so that everyone would be able to see all the competitions, but only the users who have signed up could participate.

When a registered user want to participate in a competition, if they do not have a team, they would have to create a new one. But, if they want to be in a team which already exists, they would have to provide the id of the team, in order to be part of it.
The teams would be between one and four participants, and every team would be exclusive of a competition.

The day of the competition, all the necessary documents for the participants will be showed on the page. Finally, at the end of the competition, the teams will be able to submit all their work, and the server will replay them with a punctuation for the ranking. Finally, the competition will show a ranking of the teams.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Docker and docker-compose have to be installed. Click [here](https://docs.docker.com/engine/install/). Be careful with docker daemon.

### Run locally with Docker

In order to build the project is necessary to be logged on docker. Even though, you must use the template of .env.file in order to create your own environment.

```
$ cp .env.sample .env
```

```
$ docker-compose up --build
```
Also, it is needed to do all the migrations if it is needed and migrate in order to create the database.
```
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```
Further more, it is a good practice to create a super user if it is needed a greater manage administration.
```
$ docker-compose exec web python manage.py createsuperuser
```
In addition, if you want to have a database with predefined information, it can be used the following command:
```
$ docker-compose exec web python manage.py createdb
```
### Configuration

The server will be set up by default on port 8000

You can access to the database using the default postgres user. Eventhough, you also can create a new user in postgres. To do that you have to run the following commands:

```
$ psql

# CREATE USER <name-user> WITH PASSWORD '<password>'
```

Copy '.env.sample' to a file named '.env'. You will only have to change the variable DJANGO_SECRET_KEY for a value you will have to generate.

So, the contents you should have in .env file are:

```
#------------------------------------------------------------------------------#
#---------------------------- Django configuration ----------------------------#
#------------------------------------------------------------------------------#
DJANGO_PORT=8000

DJANGO_SECRET_KEY=<your secret key>
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]

DJANGO_SQL_POSTGRES_ENGINE=django.db.backends.postgresql

DJANGO_ADMIN_USERNAME=admin
DJANGO_ADMIN_PASSWORD=admin
DJANGO_ADMIN_EMAIL=admin@example.com

AWS_KEY=<AWS_KEY>
AWS_SECRET=<AWS_SECRET>
AWS_BUCKET=<AWS_BUCKET>
#------------------------------------------------------------------------------#
#--------------------------- Postgres configuration ---------------------------#
#------------------------------------------------------------------------------#
POSTGRES_DB=codeleaguedb
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password

AWS_KEY=[Your AWS Key]
AWS_SECRET=[Your AWS Secret Key]
AWS_BUCKET=[Your AWS Bucket Name]
```

## Built and deployed with

* [GitHub](http://www.github.com) - Software development platform
* [Django](https://www.djangoproject.com) - Web framework used in the project
* [Travis](https://travis-ci.org) - Test CI
* [Docker](https://www.docker.com) - Container management
* [Heroku](https://www.heroku.com) - Cloud Application Platform
* [PostgreSQL](https://www.postgresql.org) - Open Source Database
* [AWS](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Amazon Web Services
* [Google Charts API](https://developers.google.com/chart/) - Ranking Charts

## Authors

* **Oriol Alàs Cercós** 
* **Marta Albets Mitjaneta**
* **Paula Gallucci Zurita**
* **Genís Graus Qui**
* **Adrian Lorenzo Plaza**

## License

This project is licensed under the GPLv3 License - see the [LICENSE](https://github.com/Oriolac/codeleague/blob/readme-branch/LICENSE) file for details.
