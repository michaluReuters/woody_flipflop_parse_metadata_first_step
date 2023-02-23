import os
import json
import boto3
from aws_lambda_powertools import Logger
from domain.utils import extract_data_from_sns_trigger

logger = Logger()
client = boto3.client('events')
LAMBDA_NAME = os.environ["AWS_LAMBDA_FUNCTION_NAME"]


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    data = extract_data_from_sns_trigger(event)
    logger.info(data)

    data_str = json.dumps(data)

    response = client.put_events(
        Entries=[
            {
                'Source': f"{LAMBDA_NAME}-complete",
                'Resources': [LAMBDA_NAME],
                'DetailType': "metadata-step-complete",
                'Detail': data_str
            },
        ]
    )

    logger.info(response)
