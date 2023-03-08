set -o errexit

python3 -m pip install jupyterlab
pip install --upgrade pip
pip install -r requirements.txt