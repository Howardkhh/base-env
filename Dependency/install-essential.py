#!/bin/sh

sudo -v
sudo apt-get update
sudo apt-get install -y \
  smartmontools \
  build-essential \
  git curl wget \
  htop iotop \
  landscape-common \
  ppa-purge \
  screen tmux \
  fail2ban \
  sshfs \
  vim zip \
  python-virtualenv \
  python-pip python-dev \
  python3-pip python3-dev
