#!/bin/bash
# Sherlock Server installer

# Make sure the installer is launched by root or sudoer
if ((\`id -u\` != 0))
then
  echo 'Please run installer as root or sudo it!'
  exit
fi

ufw allow 'OpenSSH'
apt update
apt upgrade
apt -y install net-tools
apt -y install figlet
apt -y install neofetch
apt -y install openjdk-8-jdk
apt -y install apache2
# Install apache server
ufw allow 'Apache'
ufw enable
apt -y install postgresql
cd
echo "neofetch" >> .bashrc
echo "figlet sherlock-server" >> .bashrc 
echo "`hostname`" >> .bashrc
echo "PS1="\033[38;5;118m`whoami`@`hostname`\033[m\033[38;5;202m ~\033[m\033[38;5;118m>\033[m \[\e[0m\]"" >> .basrc
