import os

os.system('sudo apt-get install python3-venv')
os.system('python3 -m pip install --user --upgrade pip')
os.system('python3 -m venv env')

os.system('source env/bin/activate')

os.system('python3 -m pip install -r controllers/requirements.txt')

os.system('source env/bin/activate')