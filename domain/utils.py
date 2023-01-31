import json


def extract_data_from_sns_trigger(event):
    event_dict = json.loads(event["Records"][0]["Sns"]["Message"])

    data = {}
    file_name_sns = event_dict["body"]["metadata"].get("name")
    hive_id = event_dict["body"]["metadata"].get("id")
    data["file_name"] = file_name_sns
    data["id"] = hive_id

    return data
