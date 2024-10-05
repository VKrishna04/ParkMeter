import os
import subprocess


# Commands to run
commands = ["CTRL + Break","Deactivate"]

# Run the commands
for command in commands[1 : len(commands)]:
    print("<--- ", command, " --->")
    subprocess.run(command, shell=True)
