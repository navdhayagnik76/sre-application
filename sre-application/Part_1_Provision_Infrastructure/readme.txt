1. The provided files are AWS account independent and will require just Terraform installed environment with AWS CLI user keys configured with required resource create permissions. 

2. For accessing the new AWS EC2 a local key pair has been used, which is placed in the same folder. Fresh key pair can also be generated named as keys.pub, with ssh-keygen -t rsa

3. Commands to initialize and apply the terraform config for running file.

terraform init
terraform plan
terraform apply
 
