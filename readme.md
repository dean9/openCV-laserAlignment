# Explanation here: https://www.skoien.io/laser <br />

## recommended installation: <br />

git clone github.com/dean9/openCV-laserAlignment.git <br />
cd openCV-laserAlignment <br />
python3 -m venv venv <br />
source venv/bin/activate <br />
pip install -r requirements.txt <br />

### That was all I needed to do on Mac OS, but I had some dependencies missing when doing this on a fresh raspbian.  consider the following if you hit trouble: <br />
sudo apt-get install libatlas3-base <br />
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev <br />
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev <br />
sudo apt-get install libgtk-3-dev <br />
