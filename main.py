import boto3 as bt
import schedule
ec2_vc=bt.client('ec2')
ec2_resource = bt.resource('ec2')
volume_list = ec2_vc.describe_volumes()['Volumes']


def snapshot_creation():
    for snapshot in volume_list:
        snap = ec2_resource.create_snapshot(

            VolumeId=snapshot['VolumeId']

        )
        print(snap)

schedule.every(5).seconds.do(snapshot_creation)
while True:
   schedule.run_pending()
