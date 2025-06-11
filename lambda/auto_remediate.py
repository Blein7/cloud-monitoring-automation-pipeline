import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")

    # Extract instance ID from CloudWatch alarm SNS message
    try:
        message = event['Records'][0]['Sns']['Message']
        alarm_message = json.loads(message)
        instance_id = alarm_message['Trigger']['Dimensions'][0]['value']
        logger.info(f"Target instance ID: {instance_id}")
    except Exception as e:
        logger.error(f"Error parsing event: {e}")
        raise e

    # Reboot the instance as remediation
    try:
        response = ec2.reboot_instances(InstanceIds=[instance_id])
        logger.info(f"Reboot initiated for instance {instance_id}: {response}")
    except Exception as e:
        logger.error(f"Failed to reboot instance {instance_id}: {e}")
        raise e

    return {
        'statusCode': 200,
        'body': f'Successfully rebooted instance {instance_id}'
    }
