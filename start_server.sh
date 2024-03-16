source venv/bin/activate
cd parking_ticket_system
python manage.py makemigrations
python manage.py migrate
python manage.py runserver