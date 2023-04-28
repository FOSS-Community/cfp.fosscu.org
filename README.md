# cfp-portal
A Universal portal where a user can submit there ideas and as a Organisation, they can review them.



# Tech Stack
- Django
- Html, CSS, Javascript, TailwindCSS
- PSQL

# Docker instructions

RUN the following command to migrate user model in users app

$ docker-compose run cfp python manage.py migrate users

Now, apply rest of migrations using.

$ docker-compose run cfp python manage.py migrate

Create a superuser using

$ docker-compose run cfp python manage.py createsuperuser

RUN the server using

$ docker-compose up 
