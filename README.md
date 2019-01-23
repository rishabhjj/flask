pip install -r requirements.txt 
https://stackoverflow.com/questions/27669927/how-do-i-install-python3-on-an-aws-ec2-instance


Environment:
sudo apt install python3-venv
python3 -m venv myprojectenv
source myprojectenv/bin/activate



sudo nano /etc/systemd/system/myproject.service

Description=Gunicorn instance to serve myproject
After=network.target

User=rishabhjain
Group=www-data
PIDFile=/run/gunicorn/pid
WorkingDirectory=/home/rishabhjain/flask
Environment="way=/home/rishabhjain/flask/myprojectenv/bin"
ExecStart=/home/rishabhjain/flask/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:application
WantedBy=multi-user.target

**Note: Please check the working directory of your app and also the environment that u have created and then change the location.