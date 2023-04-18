### Make sure you have python installed

1. Extract this project and cd into it

2. Create a virtual environment

    $ python3 -m venv myvenv


3. Activate the virtual environment

    $ source myvenv/bin/activate

4. Install the dependencies

    $ pip3 install -r requirements.txt

5. Run the server

    $ python3 manage.py runserver

6. You can visit the admin page (http://localhost/admin) with the credentials (username=admin, password= @qwerty123)

### Optional

You can create your own superuser from the terminal

    $ python3 manage.py createsuperuser


