send_sqs.py will insert a message in  the queue.
When queue receives the message it will automatically trigger the Lambda(lambda_func.py + data.json)
Then the Lambda will perform a POST request to the Nginx webserver
