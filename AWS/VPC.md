# Virtual Private Cloud:

## A Virtual Private Cloud is a virtual network that closely resembles a traditiobal networking that operates in your own datacenter, with the benifits of using the scalable infrastructure of AWS

* It is logically isolated from other virtual network in the AWS cloud.
* Max 5 VPC can be created and 200 Subnets in 1 VPC.
* We can allocate max 5 elastic IP.
* Once we created VPC, DHCP, NACL and security group will be automatically created.
* A VPC is confined to and AWS region and does not extend between the region.

* Once the VPC is created, you cannot change its CIDR block range.
* If you need a different CIDR size, create a new VPC.
* The different subnets within a VPC cannot overlap.
* You can however expand your VPC CIDR by adding New/Extra IP address ranges


# VPC Types
* 1) Default VPC 
* 2) Custom VPC


# Default VPC :

* It is created in each AWS region when an AWS account is created.
* It has default CIDR, security group, NACL and route table settings.
* It has an internet gateway by default.


# Custom VPC:

* It is a VPC on AWS account owner creates.
* AWS user creating the custom VPC can decide CIDR.
* Has its own default security group, network ACL and route tables.
* Does not have an internet Gateway by default. Need to be created if needed.

# Steps to create VPC:

* create a VPC
* Subnet
* Internet gateway
* Route table

# Components of VPC:

## 1) Public Subnet:
 * If a subnet's traffic is routed to an internet gateway, the subnet is known as a public subnet. 
 * If you want your instance in a public subnet to communicate with the internet over IPv4, it must have a public IPv4 or an elastic IP address.


## 2) Private Subnet:
 
 * If a subnet does not have a route to the internet gateway, the subnet is known as a Private Subnet.
 * When you create a VPC, you must have an IPv4 CIDR block for the VPC. The allowd block size is between /16 to /28 netmask.
 * The first four and last IP address of subnet cannot be assigned.
