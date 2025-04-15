import boto3
import pandas as pd

def list_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    return [r['RegionName'] for r in regions]

def list_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    res = ec2.describe_instances()
    return [inst['InstanceId'] for r in res['Reservations'] for inst in r['Instances']]

def list_metrics(region, instance_id):
    cw = boto3.client('cloudwatch', region_name=region)
    res = cw.list_metrics(Namespace='AWS/EC2', Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}])
    return list(set([m['MetricName'] for m in res['Metrics']]))

def fetch_metric_data(region, instance_id, metric_name):
    cw = boto3.client('cloudwatch', region_name=region)
    res = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName=metric_name,
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=pd.Timestamp.now() - pd.Timedelta(days=7),
        EndTime=pd.Timestamp.now(),
        Period=300,
        Statistics=['Average']
    )
    df = pd.DataFrame(res['Datapoints'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df.sort_index()
