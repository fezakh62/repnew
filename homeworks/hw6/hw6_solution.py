def level_up(experience: int, threshold: int, reward: int) -> bool:
    return experience + reward >= threshold


def motor_time(n: int) -> int:
    hours = (n // 60) % 24
    minutes = n % 60
    time_str = f"{hours:02d}{minutes:02d}"
    return sum(int(digit) for digit in time_str)


def time_converter(time_str: str) -> str:
    hours, minutes = map(int, time_str.split(":"))
    if hours == 0:
        return f"12:{minutes:02d} a.m."
    elif hours == 12:
        return f"12:{minutes:02d} p.m."
    elif hours < 12:
        return f"{hours}:{minutes:02d} a.m."
    else:
        return f"{hours - 12}:{minutes:02d} p.m."
