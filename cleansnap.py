import boto3 as bot
import schedule
from operator import itemgetter

ec2_client = bot.client('ec2')
ec2_resource = bot.resource('ec2')



def clean_snap():
    list_snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self']
    )
    sort_snapshots = sorted(list_snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    for image in sort_snapshots[2:]:
        ec2_client.delete_snapshot(
            SnapshotId=image['SnapshotId']
        )
schedule.every(1).minute.do(clean_snap)
while True:
    schedule.run_pending()
