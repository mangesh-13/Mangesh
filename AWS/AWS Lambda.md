# AWS lambda:
 * AWS Lambda is compute service that lets you run code without provisioning or managing servers.
 * With AWS lambda, you can run code for virtually any type of application or backend service-all with zero administration.

# AWS Lambda manages all the administration it manages:

*  AWS manages how much memory, CPU, network and other resources needed to run your code.
*  Server and OS maintenance.
*  High availability and automatic scaling.
*  Monitoring fleet health
*  Applying security patches
*  Deploying your code
*  Monitoring and logging your lambda functions
*  AWS lambda runs your code on a high availability compute infrastructure
*  AWS lamda runs executes your code only when needed and scales automatically from a few requests per day to thousands per second.
*  You only pay for the compute time you consume. No charge when your code is not running.
*  All you need to do is supply your code in the form of one or more lamda functions to AWS lambda, in one of the languages that AWS lambda supports(currently Node js, Java, Powershell, C#, Ruby,Pythin and Go) and the server can run the code on your behalf.

# How Lambda function works?

* First you upload your code to lambda in one or more lambda function.
* Aws lambda will then execute the code on your behalf.
* After the code is invoked, lambda automatically take care of provisoning and managing the required servers.

# Difference between AWS lambda and AWS EC2
  
| AWS Lambda | AWS EC2 |
| --- | --- |
| AWS lambda is platform as a service | AWS EC2 is an Infrastructure as a service |
| It supports only limited language | No environment restrictions, you can run any code or language |
| Write your code and push your code into AWS lambda | For the first time in EC2, you have to choose the OS and install all the software  required and then push your code in EC2|
| You cannot log into compute instances, choose customized OS or language platform | You can select variety of OS, instance types, network and security patches, RAM and CPU etc |
