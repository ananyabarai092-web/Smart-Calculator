import json
import os
from datetime import datetime

HISTORY_FILENAME = 'history.json'


def _get_file_path() -> str:
    return os.path.join(os.path.dirname(__file__), HISTORY_FILENAME)


def load_history() -> list:
    path = _get_file_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as history_file:
            return json.load(history_file)
    except (json.JSONDecodeError, IOError):
        return []


def save_history(records: list):
    path = _get_file_path()
    with open(path, 'w', encoding='utf-8') as history_file:
        json.dump(records, history_file, indent=2)


def add_record(operation: str, inputs: list, result, user: str | None = None) -> dict:
    date_value = datetime.now().strftime('%Y-%m-%d')
    time_value = datetime.now().strftime('%H:%M:%S')
    record = {
        'operation': operation,
        'inputs': inputs,
        'result': result,
        'date': date_value,
        'time': time_value,
        'user': user or 'guest',
    }
    history = load_history()
    history.append(record)
    save_history(history)
    return record


def delete_record(index: int) -> bool:
    history = load_history()
    if 0 <= index < len(history):
        history.pop(index)
        save_history(history)
        return True
    return False


def clear_history():
    save_history([])


def search_history(keyword: str) -> list:
    history = load_history()
    keyword_lower = keyword.lower()
    return [record for record in history if keyword_lower in record['operation'].lower() or keyword_lower in str(record['inputs']) or keyword_lower in str(record['result'])]
