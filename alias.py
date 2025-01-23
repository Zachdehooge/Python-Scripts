import subprocess

print(
    r"""
______________________________________________________________________      
    ___     __     ____ ___    _____
   /   |   / /    /  _//   |  / ___/
  / /| |  / /     / / / /| |  \__ \ 
 / ___ | / /___ _/ / / ___ | ___/ / 
/_/  |_|/_____//___//_/  |_|/____/  
                                    
A simple python script to automate adding an alias to the .bashrc file
______________________________________________________________________
"""
)

cmd = "grep -R 'bashrc' /home | head -1"

subprocess.run(["grep -R 'bashrc' /home | head -1"], shell=True)


bashrc = input("\nCopy and paste the FULL PATH to the .bashrc file in /home above: ")
path = input("Enter a path to the program: ")
alias = input("Enter the alias: ")


with open(bashrc, "a") as myfile:
    myfile.write("alias " + alias + "=" + "'" + path + "'\n")

myfile.close

input("PRESS ANY KEY TO RESTART SHELL")

subprocess.run(["source ~/.bashrc"], shell=True)
