---------------------------------------------------
Installing Application
---------------------------------------------------
1. Update OS
	$ sudo apt-get update

2. Install miniconda
    $ wgethttps://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh 
    $ sudo sh ./Miniconda-latest-Linux-x86_64.sh
    $ conda create -n access_manager python=3 numpy sklearn
    $ conda install -c https://conda.anaconda.org/ericmjl rpi.gpio
    $ conda install -c https://conda.anaconda.org/menpo opencv3

3. Clone the 'accessManager' repository
	$ cd /home/[desiredUserDir]/
	$ git clone https://github.com/malamaker/accessManager.git
	$ cd /home/[desiredUserDir]/accessManager/
	$ git checkout {dev/master}
	$ git pull

4. Setting the app to start on boot
	$ sudo cp /home/[desiredUserDir]/accessManager/accessManager /etc/init.d/
	$ sudo chmod 755 /etc/init.d/accessManager
	$ sudo update-rc.d accessManager defaults
	$ sudo shutdown -r now


---------------------------------------------------
Installing Updates
---------------------------------------------------
$ service accessManager stop
$ cd /home/[desiredUserDir]/accessManager/
$ git pull

