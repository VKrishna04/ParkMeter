import os
import subprocess


# Commands to run
commands = [
    "venv\\Scripts\\activate",
    "cd parking_ticket_system",
    # "python manage.py makemigrations", # Only run this command if you have made changes to the models
    # "python manage.py migrate",      # Only run this command if you have made changes to the models
    "python manage.py runserver",
]

# Run the commands
print("<--- ", commands[0], " --->")
subprocess.run(commands[0], shell=True)
os.chdir("parking_ticket_system")

for command in commands[1 : len(commands)]:
    print("<--- ", command, " --->")
    subprocess.run(command, shell=True)
