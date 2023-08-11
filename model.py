import datetime
import json
import datetime as DT

class Notes:

    def __init__(self, path: str = 'notes.json'):
        self._notes: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0
        self._date = ''

    def open(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for elm in data:
            elm = elm.strip().split(";")
            new = {'title':  elm[0], 'body': elm[1], 'id': elm[2], 'date': elm[3]}
            self._notes.append(new)

    def save(self):
        data = []
        for elm in self._notes:
            elm = ';'.join([value for value in elm.values()])
            data.append(elm)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.writelines(f'{json.dumps(data)}\n')

    def load(self) -> list[dict[str, str]]:
        return json.loads(json.dumps(self._notes))

    def add(self, note: dict[str, str]) -> str:
        self._last_id += 1
        self._date = str(DT.datetime.now())
        note['id'] = str(self._last_id)
        note['date'] = f'{str(self._date)};'
        self._notes.append(note)
        return note.get('title')

    def delete(self, index: int):
        return self._notes.pop(index-1).get('title')

    def change(self, index: int, note: dict[str, str]):
        self._notes[index-1] = note
        return self._notes[index-1].get('title')

    def search(self, find: str):
        with open(self._path, 'r', encoding='utf-8') as file:
            read_data = file.readlines()
            for letters in read_data:
                if find in letters:
                    res = letters.strip()
        return res