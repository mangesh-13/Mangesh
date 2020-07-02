# Objective :  Export data from HDFS into a MySQL table using Sqoop
### Lab steps
**Put the Data into HDFS**
**change the directory and check the content of the salarydata.txt**
```ssh
# cd ~/labs/Lab3.2
# tail salarydata.txt
```
![Capture](https://user-images.githubusercontent.com/64658306/86383780-dd82fc80-bcab-11ea-8c5b-12eaaaad95fa.JPG)

**Create a new directory in HDFS named salarydata.**
```ssh
# hdfs dfs -mkdir salarydata
```
![Capture1](https://user-images.githubusercontent.com/64658306/86383811-dfe55680-bcab-11ea-8364-ae00d90b3bc3.JPG)

**Put salarydata.txt into the salarydata directory in HDFS.**
```ssh
# hdfs dfs –put salarydata.txt salarydata
```
![Capture2](https://user-images.githubusercontent.com/64658306/86383833-e247b080-bcab-11ea-8f0d-0413322d19d0.JPG)
![Capture3](https://user-images.githubusercontent.com/64658306/86383852-e378dd80-bcab-11ea-822e-f840eb8da724.JPG)

**Create a Table in the Database** 
![Capture8](https://user-images.githubusercontent.com/64658306/86393286-7456b580-bcba-11ea-99dd-eea10e801a27.JPG)

There is a script in the Exporting HDFS Data to an RDBMS lab folder that creates 
a table in MySQL that matches the records in salarydata.txt. View the SQL script:
```ssh
# more salaries2.sql
```
![Capture4](https://user-images.githubusercontent.com/64658306/86383881-e5db3780-bcab-11ea-9261-006fe78377a7.JPG)

**Export the Data**

Run a Sqoop command that exports the salarydata folder in HDFS into the 
salaries2 table in MySQL. At the end of the MapReduce output, you should see a 
log event stating that 10,000 records were exported. 

![Capture5](https://user-images.githubusercontent.com/64658306/86394048-89801400-bcbb-11ea-9929-6014d8a8bed9.JPG)
![Capture6](https://user-images.githubusercontent.com/64658306/86394051-8be26e00-bcbb-11ea-832f-3cc6dfa5dd47.JPG)
![Capture7](https://user-images.githubusercontent.com/64658306/86394053-8e44c800-bcbb-11ea-8522-8c8efa425bea.JPG)
![Capture9](https://user-images.githubusercontent.com/64658306/86393304-791b6980-bcba-11ea-8d99-825db3c20356.JPG)
