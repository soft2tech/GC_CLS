#!/bin/sh
echo "Installing selenium"

pip install -r requerments.txt

echo "installing Drivers For FireFox"

mkdir ~/tmp

cd ~/app-tmp

wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux32.tar.gz

tar xf geckodriver-v0.29.0-linux32.tar.gz

sudo cp geckodriver /usr/bin/

cd ..

rm -rf app-tmp

sudo mkdir /opt/GC_CLS

sudo cp app.py /opt/GC_CLS/

sudo cp db.yaml /opt/GC_CLS

sudo gedit /opt/GC_CLS/db.yaml
