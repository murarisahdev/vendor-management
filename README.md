## Vendor Management System

Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

### Local Setup
- `git clone url`
- create a .env file in the root directory
- copy example.env to .env
- `docker compose up --build`
- to run the test cases, use this command: `docker exec -it vendor-web python manage.py test`
- to access the admin panel, create a superuser using this command: `docker exec -it vendor-web python manage.py createsuperuser`

### Check the admin interface
[Admin Panel](http://0.0.0.0:8000/admin)

### Check the Swagger documentation
[Swagger Documentation](http://0.0.0.0:8000/api/schema/swagger-ui/)

### API Endpoints


**Vendor Profile Management**

- Create a new vendor
    ```bash
    POST /api/vendors/

- List all vendors:

    `GET /api/vendors/`
- Retrieve a specific vendor's details:
    ```bash
    GET /api/vendors/{vendor_id}/
- Update a vendor's details:
    ```bash
    PUT /api/vendors/{vendor_id}/
- Delete a vendor:
    ```bash
    DELETE /api/vendors/{vendor_id}/

**Purchase Order Management**
 - Create a purchase order:
    ```bash
    POST /api/purchase-order/
- List all purchase orders:
    ```bash
    GET /api/purchase-order/
- Retrieve details of a specific purchase order:
    ```bash
    GET /api/purchase-order/{id}/
- Update a purchase order:
    ```bash
    PUT /api/purchase-order/{id}/
- Delete a purchase order:
    ```bash
    DELETE /api/purchase-order/{id}/

**Purchase order Acknowledge**
- acknowledge purchase order:
    ```bash
    POST /api/purchase-order/{PO_id}/acknowledge/
**Vendor Performance Evaluation**
- Retrieve a vendor's performance metrics:
    ```bash
    GET /api/vendors/{vendor_id}/performance/


### Tech Stack
- Python
- Django REST Framework (DRF)
- PostgreSQL
- Docker
- JSON Web Token (JWT)
