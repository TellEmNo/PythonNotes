import datetime as DT
import json

import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 4:
            return int(choice)

def main_menu2() -> int:
    print(text.main_menu2)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)

def sort_menu() -> int:
    print(text.sort_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 4:
            return int(choice)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def print_notes(notes: list[dict[str, str]], error: str):
    if notes:
        print('\n' + '=' * 55)
        for i, _note in enumerate(notes, 1):
            print(json.loads(json.dumps(f'{i}. {_note.get("title")}: \n {_note.get("body")} \n {_note.get("date")}')))
        print('=' * 55 + '\n')
    else:
        print_message(error)

def print_notes(notes: list[dict[str, str]], error: str):
    if notes:
        print('\n' + '=' * 55)
        for i, _note in enumerate(notes, 1):
            print(json.loads(json.dumps(f'{i}. {_note.get("title")}: \n {_note.get("body")} \n {_note.get("date")}')))
        print('=' * 55 + '\n')
    else:
        print_message(error)

def input_note(message: str, cancel: str, oops: str) -> dict:
    note = {}
    print(message)
    print(oops)
    for key, value in text.input_note.items():
        data = input(value)
        if data:
            note[key] = data
        else:
            print_message(cancel)
    return note


def input_index(message: str, notes: list, error: str) -> int:
    print_notes(notes, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(notes) + 1:
            return int(index)

def find_note(message: str):
    find = input(message)
    return find