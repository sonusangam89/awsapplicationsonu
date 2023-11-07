sudo pkill -f runserver

cd /home/ubuntu/aws_cicd/

python3 -m venv venv

source venv/bin/activate

pip install -r /home/ubuntu/aws_cicd/requirements.txt

screen -d -m python3 myapp.py

