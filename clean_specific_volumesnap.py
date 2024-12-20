import boto3 as bot
from operator import itemgetter
import schedule


ec2_client = bot.client('ec2')
ec2_resource = bot.resource('ec2')

def delete_old_snapshot():
    volumes = ec2_client.describe_volumes()['Volumes']

    for snap in volumes:
        shot = ec2_client.describe_snapshots(
            OwnerIds=['self'],
            Filters=[
                {
                    'Name': 'Volume-id',
                    'Values': [snap['VolumeId']]

                },
            ]
        )
        sort_snap = sorted(shot['Snapshots'], key=itemgetter('StartTime'), reverse=True)
        for image in sort_snap:
            delete_snap = ec2_client.delete_snapshot(
                SnapshotId=image['SnapshotId']
            )

schedule.every(40).seconds.do(delete_old_snapshot)
while True:
    schedule.run_pending()
