# JSON Helpers
import json

def get_json_info(text):
    try:
        json_obj = json.loads(text)
        if isinstance(json_obj, list) and len(json_obj) > 0 and isinstance(json_obj[0], dict):
            keys = list(json_obj[0].keys())
            return keys
        else:
            return []
    except ValueError as e:
        return None


def is_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False


def extract_text_from_json(json_text):
    data = json.loads(json_text)
    if isinstance(data, list):
        # If data is a list, concatenate its items into a single string
        return ' '.join(map(str, data))
    elif isinstance(data, dict):
        # If data is a dictionary, concatenate its values into a single string
        return ' '.join(map(str, data.values()))
    else:
        # If data is neither a list nor a dictionary, treat it as a single string
        return str(data)
