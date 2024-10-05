import os
import subprocess


# Commands to run
commands = [
    "pip install virtualenv==20.25.1",
    "virtualenv venv",
    # "source venv/bin/activate",
    r".venv\Scripts\activate",  # Activate for 'venv' named environment
    "pip install -r requirements.txt",
]

# Run the commands
for command in commands[1 : len(commands)]:
    print("<--- ", command, " --->")
    subprocess.run(command, shell=True)
