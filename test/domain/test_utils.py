import unittest
from domain.utils import extract_data_from_sns_trigger


class TestExtractDataFromSnsTrigger(unittest.TestCase):

    def test_extract_data_from_sns_trigger_valid_input(self):
        event = {
            "Records": [
                {
                    "Sns": {
                        "Message": '{"body": {"metadata": {"name": "file.txt", "id": 12345}}}'
                    }
                }
            ]
        }
        expected_result = {"file_name": "file.txt", "id": 12345}
        result = extract_data_from_sns_trigger(event)
        self.assertEqual(result, expected_result)

    def test_extract_data_from_sns_trigger_empty_input(self):
        event = {
            "Records": [
                {
                    "Sns": {
                        "Message": '{"body": {"metadata": {"name": "", "id": ""}}}'
                    }
                }
            ]
        }
        expected_result = {"file_name": "", "id": ""}
        result = extract_data_from_sns_trigger(event)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
