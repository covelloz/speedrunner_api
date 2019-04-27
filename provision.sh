# install nginx
apt-get -y update
apt-get -y install nginx
systemctl start nginx
# install conda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
rm Miniconda3-latest-Linux-x86_64.sh
# create python 3.6 environment
/opt/conda/bin/conda create --name=speedrunner python=3.6
/opt/conda/bin/pip install -r /vagrant/requirements.txt