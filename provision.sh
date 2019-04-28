# install nginx
apt-get -y update
apt-get -y install nginx
# install conda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
rm Miniconda3-latest-Linux-x86_64.sh
# create python 3.6 environment
/opt/conda/bin/conda create --name=speedrunner python=3.6
/opt/conda/envs/speedrunner/bin/pip install -r /vagrant/requirements.txt
/opt/conda/envs/speedrunner/bin/pip install gunicorn
# configure web service
cp /vagrant/server/api.service /etc/systemd/system/
systemctl start api.service
# configure web server
systemctl stop nginx
cp /vagrant/server/nginx_conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/nginx_conf /etc/nginx/sites-enabled
rm /etc/nginx/sites-enabled/default
systemctl start nginx