1)Provided files are AWS account independent and requires Terraform installed environment with AWS CLI user keys configured with required resource create permissions. 
2)To access the new AWS EC2, local key-pair is used, which is placed under same folder. New key pair can also be generated named as keys.pub, with ssh-keygen -t rsa command
3)Below are the commands to initialize and apply the terraform config to run the file.

- terraform init
- terraform plan
- terraform apply
 
