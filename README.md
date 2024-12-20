# DataBackup

# Technologies used: 
Python: Boto3 library
AWS

# Project Description:
Write a Python script that automates creating backups for EC2 Volumes <br/>
Write a Python script that cleans up old EC2 Volume snapshots <br/>
Write a Python script that restores EC2 Volumes   <br/>

# Introduction and motivation of the Project:
1. Why is creation of snapshot of volumes for EC2 instances important <br/>

Volumes are AWS Storage Components that stores EC2 instance data and every EC2 has volumes where it writes its data. <br/>
   
The creation of 'snapshots'is important due to the risk of data corruption. <br/>
Snapshot creation is the generation of a comprehensive backup of EC2 instance data  <br/>
which enables seamless data recovery if the original volumes become corrupted or compromised. <br/>

Additionally, these snapshots can be employed to produce new volumes when needed. <br/>


The fundamental importance of snapshots in maintaining data integrity and continuity underpins the motivation for this project."

# Steps

Check the boto documentation
get the volumeId as it is required to create snapshot
loop through the volumes and create snap shot by referring to the volumeid


# Step2
The best practice is to keep only the latest snapshots and automatically creating snapshots of volumes every day may lead to lots of snapshots and therefore needs to automatically delete old snapshots of volumes.

Loop through the list of snapshots <br/>
sort snapshots base on StartTime and delete the every snap shot except the first two snapshots

       volumes = ec2_client.describe_volumes()
       for snap in volumes:
          shot = ec2_client.describe_snapshots(
              OwnerId=['self'],
              Filters=


check complete code from file :  'clean_specific_volumesnap.py'


