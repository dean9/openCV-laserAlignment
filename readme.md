Explanation here: https://www.skoien.io/laser

recommended installation:

git clone github.com/dean9/openCV-laserAlignment.git 
cd openCV-laserAlignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

That was all I needed to do on Mac OS, but I had some dependencies missing when doing this on a fresh raspbian.  consider the following if you hit trouble:
sudo apt-get install libatlas3-base
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libgtk-3-dev

