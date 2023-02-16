import json


def extract_data_from_sns_trigger(event):
    """
    This function simply extracts data from incoming event

    :param event: event triggering function
    :return: required data to be processed
    """
    event_dict = json.loads(event["Records"][0]["Sns"]["Message"])

    data = {}
    file_name_sns = event_dict["body"]["metadata"].get("name")
    hive_id = event_dict["body"]["metadata"].get("id")
    data["id"] = hive_id
    data["name"] = file_name_sns

    return data
