#!/bin/sh
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip
pip install boto boto3 ansible
mkdir -p /home/ubuntu/AWS_Ansible/group_vars/all/
touch /home/ubuntu/AWS_Ansible/playbook.yml
