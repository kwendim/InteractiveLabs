mkdir ~/data
sudo apt-get purge -y docker.io docker-ce docker-ce-cli containerd.io
sudo apt-get install -y curl apt-transport-https ca-certificates gnupg-agent software-properties-common
sudo apt-get update