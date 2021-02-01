import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-west-2.amazonaws.com/697695473970/test_queue'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageBody=(
        'Invoke Lambda Function'
    )
)

print(response['MessageId'])
