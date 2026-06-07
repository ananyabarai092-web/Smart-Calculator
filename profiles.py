import json
import os
from collections import Counter
from achievements import generate_badges

USER_FILENAME = 'users.json'


def _get_file_path() -> str:
    return os.path.join(os.path.dirname(__file__), USER_FILENAME)


def load_users() -> dict:
    path = _get_file_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as users_file:
            return json.load(users_file)
    except (json.JSONDecodeError, IOError):
        return {}


def save_users(users: dict):
    path = _get_file_path()
    with open(path, 'w', encoding='utf-8') as users_file:
        json.dump(users, users_file, indent=2)


def normalize_username(username: str) -> str:
    return username.strip().lower()


def register_user(username: str) -> dict:
    if not username.strip():
        raise ValueError('Username cannot be empty.')
    users = load_users()
    key = normalize_username(username)
    if key in users:
        raise ValueError('A profile with that username already exists.')
    profile = {
        'username': username.strip(),
        'calculations_performed': 0,
        'favorite_operation': 'None',
        'total_sessions': 0,
        'operations_count': {},
        'memory_usage': 0,
        'created_date': '',
    }
    users[key] = profile
    save_users(users)
    return profile


def login_user(username: str) -> dict:
    users = load_users()
    profile = users.get(normalize_username(username))
    if profile is None:
        raise ValueError('Username not found. Please register first.')
    return profile


def update_session(profile: dict):
    users = load_users()
    key = normalize_username(profile['username'])
    profile['total_sessions'] = profile.get('total_sessions', 0) + 1
    users[key] = profile
    save_users(users)


def update_after_calculation(profile: dict, operation: str):
    users = load_users()
    key = normalize_username(profile['username'])
    profile['calculations_performed'] = profile.get('calculations_performed', 0) + 1
    operations = profile.get('operations_count', {})
    operations[operation] = operations.get(operation, 0) + 1
    profile['operations_count'] = operations
    favorite = Counter(operations).most_common(1)
    profile['favorite_operation'] = favorite[0][0] if favorite else 'None'
    users[key] = profile
    save_users(users)


def update_memory_usage(profile: dict):
    users = load_users()
    key = normalize_username(profile['username'])
    profile['memory_usage'] = profile.get('memory_usage', 0) + 1
    users[key] = profile
    save_users(users)


def build_profile_summary(profile: dict) -> dict:
    badges = generate_badges(profile)
    return {
        'username': profile.get('username', 'Unknown'),
        'calculations_performed': profile.get('calculations_performed', 0),
        'favorite_operation': profile.get('favorite_operation', 'None'),
        'total_sessions': profile.get('total_sessions', 0),
        'memory_usage': profile.get('memory_usage', 0),
        'badges': badges,
    }
