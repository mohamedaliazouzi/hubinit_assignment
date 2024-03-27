# Full Stack Assignment (HTML/CSS, Bootstrap, JavaScript, Django)

<p align="center" border="none">
  <img alt="Hubinit" src="./hubinit.png" align="center">
</p>

## Requirements

This assignment is provided by Hubinit, a company headquartered in Amsterdam, Netherlands. The project aims to create a basic CRUD application using Django for managing a data object named "blog" within the Django admin interface. Alongside the front end, the application should allow users to search blog items, perform CRUD operations, and customize "__localhost:your_port/__". The provided HTML template, found in the "carousel" folder, can serve as a reference for the application's frontend design (HTML Template).

## Demo

https://github.com/RabiiAlaouiLamharzi/hubinit_assignment/assets/103124512/f76ca2f9-d97e-4218-940f-bfd89029232e

## To Use, you Need to:

- Download and install the latest stable version of Python from the [official Python website](https://www.python.org/downloads/).
- install Django using pip (or pip3 for mac and linux). Open your terminal or command prompt and run the following command:
   ```bash
   pip install django
- Clone the repository to your local machine:
   ```bash
   git clone https://github.com/RabiiAlaouiLamharzi/hubinit_assignment
- Navigate into the project directory:
   ```bash
   cd hubinitex
- Install the project dependencies using pip (or pip3 for mac and linux):
   ```bash
   pip install -r requirements.txt
- Migrate the database:
  ```bash
  python manage.py migrate
- Create a superuser (for accessing the admin interface):
  ```bash
  python manage.py createsuperuser
- Run the development server:
  ```bash
  python manage.py runserver
