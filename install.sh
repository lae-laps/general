read -p "password for root: " password
mkdir tools
cd tools
git clone https://github.com/HACK3RY2J/Anon-SMS
git clone https://github.com/umeshshinde19/instainsane
git clone https://github.com/htr-tech/nexphisher
git clone https://github.com/opsdisk/pagodo
git clone https://github.com/hangetzzu/saycheese
git clone https://github.com/Darkmux/SETSMS
git clone https://github.com/sherlock-project/sherlock
wget -qnc https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
sudo dpkg -i nordvpn-release_1.0.0_all.deb
sudo apt update
rm nordvpn-release_1.0.0_all.deb
sudo -p $password apt install nordvpn
sudo -p $password apt install neofetch
