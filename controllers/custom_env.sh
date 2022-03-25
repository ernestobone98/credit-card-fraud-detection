sudo apt-get install python3-venv
python3 -m pip install --user --upgrade pip
python3 -m venv .gitignore/env
python3 -m pip install --force-reinstall -r controllers/requirements.txt

source .gitignore/env/bin/activate