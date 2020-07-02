# Create a Directory in HDFS
**a) Enter the following -ls command to view the contents of the user’s root directory in HDFS, which is /user/root**
```ssh
# hdfs dfs -ls 
```
**You do not have any files in /user/root yet, so no output is displayed. 
Run the -ls command again, but this time specify the root HDFS folder**
```ssh
# hdfs dfs -ls /
```
**The output will look like :**

![Capture](https://user-images.githubusercontent.com/64658306/85610593-c2453b00-b674-11ea-80c6-adee98cfb841.JPG)

**b) Enter the following command to create a directory named test in HDFS:**
```ssh
# hdfs dfs -mkdir test 
```
**c) Verify that the folder was created successfully:**
```ssh
# hdfs dfs -ls
```
![Capture1](https://user-images.githubusercontent.com/64658306/85610608-c5d8c200-b674-11ea-8d0a-cfdb404796de.JPG)

**d. Create a couple of subdirectories for test:** 
```ssh
# hdfs dfs -mkdir test/test1
# hdfs dfs -mkdir -p test/test2/test3 
```
**e) Use the -ls command to view the contents of /user/root:**
```ssh
# hdfs dfs -ls
```
**Notice you only see the test directory. To recursively view the contents of a folder, use -ls -R:**
```ssh
# hdfs dfs -ls -R 
```
![Capture2](https://user-images.githubusercontent.com/64658306/85621856-8d8cb000-b683-11ea-93dc-1e336202fe58.JPG)

# Delete a Directory

**a) Delete the test2 folder (and recursively, its subcontents) using the -rm -R command:**
```ssh
# hdfs dfs -rm -R test/test2 
```
![Capture3](https://user-images.githubusercontent.com/64658306/85622186-1c99c800-b684-11ea-87d9-952b575b8d04.JPG)
**b) b. Now run the -ls -R command:
```ssh
# hdfs dfs -ls -R 
```
![Capture4](https://user-images.githubusercontent.com/64658306/85637993-5b3e7b00-b6a2-11ea-9ff2-f1110f59202e.JPG)

# Upload a file to HDFS
**a) Now let’s put a file into the test folder. Change directories to /root/devph/labs/Lab2.1:**
```ssh
# cd /home/hadoop/labs/Lab2.1/ 
```
![Capture5](https://user-images.githubusercontent.com/64658306/85638165-cf791e80-b6a2-11ea-8329-00240790190d.JPG)

**b) Notice this folder contains a file named data.txt:**
```ssh
# tail data.txt
```
![Capture6](https://user-images.githubusercontent.com/64658306/85638329-40203b00-b6a3-11ea-9919-b137b39a5b1f.JPG)

**c) Run the following -put command to copy data.txt into the test folder in HDFS:**
```ssh
# hdfs dfs -put data.txt test/ 
```
![Capture7](https://user-images.githubusercontent.com/64658306/85638579-dfddc900-b6a3-11ea-9cdf-b29387319bbe.JPG)

**d) Verify that the file is in HDFS by listing the contents of test:**
```ssh
# hdfs dfs -ls test
```
**The output should look like the following:**
![Capture8](https://user-images.githubusercontent.com/64658306/85638758-61cdf200-b6a4-11ea-8890-87953e7d5dbd.JPG)

# Copy a File in HDFS
**a) Now copy the data.txt file in test to another folder in HDFS using the -cp command:**
```ssh
# hdfs dfs -cp test/data.txt test/test1/data2.txt 
```
**b) Verify that the file is in both places by using the -ls -R command on test. The 
output should look like the following:**
```ssh
# hdfs dfs -ls -R test 
```
![Capture9](https://user-images.githubusercontent.com/64658306/85639008-19fb9a80-b6a5-11ea-9972-0cad85400f7b.JPG)

**c) Now delete the data2.txt file using the -rm command:**
```ssh
# hdfs dfs -rm test/test1/data2.txt 
```
![Capture10](https://user-images.githubusercontent.com/64658306/85639169-7b236e00-b6a5-11ea-9ba0-a26ea90c2341.JPG)

**d) Verify that the data2.txt file is in the .Trash folder.**

# View the Content of a File in HDFS
**a)  You can use the -cat command to view text files in HDFS. Enter the following command to view the contents of data.txt:**

```ssh
# hdfs dfs -cat test/data.txt 
```
![Capture12](https://user-images.githubusercontent.com/64658306/85639323-043aa500-b6a6-11ea-9fe4-cd15a2ddbe47.JPG)

**b) You can also use the ‐tail command to view the end of a file:**
```ssh
# hdfs dfs -tail test/data.txt 
```
![Capture13](https://user-images.githubusercontent.com/64658306/85639493-8fb43600-b6a6-11ea-8505-6ec0b4ae4d28.JPG)

**Notice the output this time is only the last 20 rows of data.txt.**

# Getting a File from HDFS
**a) See if you can figure out how to use the get command to copy test/data.txt from HDFS into your local /tmp folder**
```ssh
# hdfs dfs -get test/data.txt /tmp/
# cd /tmp
# ls data* 
```
![Capture14](https://user-images.githubusercontent.com/64658306/85639680-0fda9b80-b6a7-11ea-899b-b70d7cfad6d4.JPG)

# The ssh getmerge Command
**a) Put the file /home/hadoop/labs/demos/small_blocks.txt into the test folder in HDFS. You should now have two files in test: data.txt and small_blocks.txt.** 
```ssh
# hdfs dfs -put /home/hadoop/labs/demos/small_blocks.txt test/
```
**b) Run the following getmerge command:**
```ssh
# hdfs dfs -getmerge test /tmp/merged.txt 
```
![Capture15](https://user-images.githubusercontent.com/64658306/85639951-f6861f00-b6a7-11ea-8f02-19bee98234de.JPG)
**The two files that were in the test folder in HDFS were merged into a single file and stored on the local file system.**

# Specify the Block Size and Replication Factor
**a) Put /home/hadoop/labs/Lab2.1/data.txt into /home/hadoop in HDFS, giving it a blocksize of 1,048,576 bytes.**
```ssh
# hdfs dfs -D dfs.blocksize=1048576 -put data.txt data.txt 
```
**b) Run the following fsck command on data.txt:**
```ssh
# hdfs fsck /user/root/data.txt 
```
![Capture16](https://user-images.githubusercontent.com/64658306/85640250-ec185500-b6a8-11ea-8150-f4a4f37370a0.JPG)

**c) How many blocks are there for this file?**

**Answer: The file should be broken down into two blocks.**


