The EC2 host needs ansible installed which can be done through below commands

sudo apt install python

sudo apt install python-pip

pip install boto boto3 ansible

1.Create SSH keys to connect to the EC2 instance after provisioning
ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_aws



2.Create Ansible Vault file to store the AWS Access and Secret keys.

ansible-vault create group_vars/all/pass.yml

3.Edit the pass.yml file and enter the keys global constants for corresponding AWS account user with necessary permissions.
ansible-vault edit group_vars/all/pass.yml

ec2_access_key: ##############                                      
ec2_secret_key: ###################

4.Create the instance
ansible-playbook playbook.yml --ask-vault-pass --tags create_ec2

For installing Nginx and Mysql, below scripts will be run corresponding to the newly created ec2 IP(refer inventory)
​
ssh -i ~/.ssh/my_aws ubuntu@#.#.#.# " sudo apt update  && sudo apt install nginx -y  && sudo ufw allow 'Nginx HTTP' "
ssh -i ~/.ssh/my_aws ubuntu@#.#.#.# " sudo apt install mysql-server -y "
