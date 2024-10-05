& .venv/Scripts/activate
# powershell -ExecutionPolicy ByPass -File "f:\Code\ParkMeter\.venv\Scripts\activate.ps1"
echo "Starting server..."
Get-Command python

Set-Location .\parking_ticket_system
# python manage.py makemigrations
# python manage.py migrate
python manage.py runserver
