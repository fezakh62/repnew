from __future__ import annotations


def add_ing(s: str) -> str:
    return s + "ing"


def change_symbol(s: str) -> str:
    return s.replace("#", "/")


def change_order(s: str) -> str:
    words = s.split()
    if len(words) >= 2:
        words[0], words[1] = words[1], words[0]
    return " ".join(words)


def clean_string(s: str) -> str:
    return s.strip()


def to_capitalize(s: str) -> str:
    return s.capitalize()


def to_list(s: str) -> list:
    return s.split()


def formatting(array: list, s1: str, s2: str) -> str:
    return f"Hello, {' '.join(array)}! {s1} to {s2}"


def to_string(array: list) -> str:
    return " ".join(array)


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    if indx > len(array):
        array.append(item)
    else:
        array.insert(indx, item)
    return array


def delete_from_list(array: list, indx: int) -> list:
    if 0 <= indx < len(array):
        array.pop(indx)
    return array
