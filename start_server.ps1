venv\Scripts\activate
Set-Location .\parking_ticket_system
python manage.py makemigrations
python manage.py migrate
python manage.py runserver