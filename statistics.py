from collections import Counter
from datetime import datetime


def generate_statistics(history_records: list) -> dict:
    if not history_records:
        return {
            'total_calculations': 0,
            'most_used_operation': 'N/A',
            'highest_result': 'N/A',
            'lowest_result': 'N/A',
            'average_result': 'N/A',
            'last_calculation_time': 'N/A',
        }

    total_calculations = len(history_records)
    operations = [record['operation'] for record in history_records]
    results = [record['result'] for record in history_records if isinstance(record['result'], (int, float))]
    most_used_operation = Counter(operations).most_common(1)[0][0]
    highest_result = max(results) if results else 'N/A'
    lowest_result = min(results) if results else 'N/A'
    average_result = round(sum(results) / len(results), 2) if results else 'N/A'
    last_record = max(history_records, key=lambda item: datetime.strptime(f"{item['date']} {item['time']}", '%Y-%m-%d %H:%M:%S'))
    last_calculation_time = f"{last_record['date']} {last_record['time']}"

    return {
        'total_calculations': total_calculations,
        'most_used_operation': most_used_operation,
        'highest_result': highest_result,
        'lowest_result': lowest_result,
        'average_result': average_result,
        'last_calculation_time': last_calculation_time,
    }
