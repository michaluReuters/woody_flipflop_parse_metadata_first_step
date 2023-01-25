from aws_lambda_powertools import Logger
from domain.utils import extract_data_from_sns_trigger
logger = Logger()


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    return extract_data_from_sns_trigger(event)