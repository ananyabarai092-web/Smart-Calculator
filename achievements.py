from collections import Counter


def generate_badges(user_profile: dict) -> list[str]:
    badges = []
    calculations = user_profile.get('calculations_performed', 0)
    sessions = user_profile.get('total_sessions', 0)
    favorite = user_profile.get('favorite_operation', 'None')

    if calculations >= 1:
        badges.append('First Calculation 🧮')
    if calculations >= 10:
        badges.append('Calculation Enthusiast ⭐')
    if calculations >= 50:
        badges.append('Math Maestro 🏆')
    if sessions >= 5:
        badges.append('Regular Visitor 🔁')
    if favorite and favorite != 'None':
        badges.append(f'Favorite: {favorite} 💡')
    if user_profile.get('memory_usage', 0) >= 3:
        badges.append('Memory Master 🧠')
    return badges
