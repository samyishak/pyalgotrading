Miniconda

* [Install miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/macos.html)
* Update conda itself (the installer is in general not as regularly updated as the package)
* Check if you can start Python in a new shell instance (make sure the path is set correctly)

Docker

* [Docker for Apple Silicon](https://docs.docker.com/docker-for-mac/apple-silicon/)

Cloud Instance (DigitalOcean)

* [Create Droplet](https://cloud.digitalocean.com/droplets/new)
	* [SSH auth](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)
	* todo [Cloud-Config](https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup)
* Set up server
	* Initial server config https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
	* Connect via OpenSSH https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/openssh/
* Python installation
	* Create `install.sh` file
	* Create `setup.sh` file
	* Run `setup.sh`
* Connect via SSH
	* PyCharm
	* VSCode