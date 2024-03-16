import os
import subprocess
import sys


def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)


# Check if the platform is Windows
is_windows = sys.platform == "win32"


# Commands to run
commands = [
    "venv\\Scripts\\activate",
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver",
]

# Run the commands
subprocess.run(commands[0], shell=True)
os.chdir(os.path.join(os.getcwd(), "/parking_ticket_system"))
run_commands(commands[1:-1])
