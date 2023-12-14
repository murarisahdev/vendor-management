# Vendor Management System

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

# Local Setup-

- `git clone url`
- create a .env file in root directory
- copy example.env in .env
- `docker compose up --build`
- to run the test cases, use this command `docker exec -it vendor-web python manage.py test`
- to access the admin panel, create a superuser using this command `docker exec -it vendor-web python manage.py createsuperuser`

# Check the admin interface-

    http://0.0.0.0:8000/admin

# Check the swagger documentation-

    http://0.0.0.0:8000/api/schema/swagger-ui/

# Tech Stack

- python
- DRF
- PostgreSQL
- docker
- JWT
