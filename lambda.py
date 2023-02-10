import json
import boto3
from aws_lambda_powertools import Logger
from domain.utils import extract_data_from_sns_trigger

logger = Logger()
client = boto3.client('events')


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    data = extract_data_from_sns_trigger(event)
    logger.info(data)

    data_str = json.dumps(data)

    response = client.put_events(
        Entries=[
            {
                'Source': "new-ppe-sonyhivemetadata-step1-complete",
                'Resources': ["new-ppe-sh-sonyhive-metadata-import-step1-lambda"],
                'DetailType': "metadata-step-complete",
                'Detail': data_str
            },
        ]
    )

    logger.info(response)
