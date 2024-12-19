# DataBackup

# Technologies used: 
Python: Boto3 library
AWS

# Project Description:
Write a Python script that automates creating backups for EC2 Volumes <br/>
Write a Python script that cleans up old EC2 Volume snapshots <br/>
Write a Python script that restores EC2 Volumes   <br/>

# Introduction and motivation of the Project:
1. Why is creation of snapshot of volumes for EC2 instances important

Volumes are AWS Storage Components that stores EC2 instance data and every EC2 has volumes where it writes its data.
   
The creation of 'snapshots'is important due to the risk of data corruption. Snapshot creation is the generation of a comprehensive backup of EC2 instance data  

which enables seamless data recovery if the original volumes become corrupted or compromised. Additionally, these snapshots can be employed to produce new volumes

when needed. Given these critical functions, it is imperative to automate snapshots creation to ensure that daily backups of volumes are consistently generated. 

The fundamental importance of snapshots in maintaining data integrity and continuity underpins the motivation for this project."

