from re import findall
import json
import datetime as DT

class Notes:

    def __init__(self, path: str = 'notes.json'):
        self._notes: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0
        self._date = ''

    def open(self):
        try:
            with open(self._path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for elm in data:
                elm = elm.strip().split(";")
                new = {'title':  elm[0], 'body': elm[1], 'id': elm[2], 'date': elm[3]}
                self._notes.append(new)
        except IOError:
            print('Ошибка при чтении, записи или открытии файлов')

    def save(self):
        data = []
        for elm in self._notes:
            elm = ';'.join([value for value in elm.values()])
            data.append(elm)
        try:
            with open(self._path, 'w', encoding='utf-8') as file:
                file.writelines(f'{json.dumps(data)}\n')
        except IOError:
            print('Ошибка при чтении, записи или открытии файлов')

    def load(self) -> list[dict[str, str]]:
        return json.loads(json.dumps(self._notes))

    def add(self, note: dict[str, str]) -> str:
        self._last_id += 1
        self._date = str(DT.datetime.now())[:-7]
        note['id'] = str(self._last_id)
        note['date'] = f'{str(self._date)};'
        self._notes.append(note)
        return note.get('title')

    def delete(self, index: int):
        return self._notes.pop(index-1).get('title')

    def change(self, index: int, note: dict[str, str]):
        self._date = str(DT.datetime.now())[:-7]
        note['date'] = str(self._date)
        self._notes[index-1] = note
        return self._notes[index-1].get('title')

    def search_by_index(self, index: int) -> str:
        str_ = self._notes[index-1].get('title') + ': \n' + self._notes[index-1].get('body') \
                + '. \n' + self._notes[index-1].get('date')
        return str_

    def sort_by_date_ascending(self) -> list[dict[str, str]]:
        sorted_list = sorted(self._notes, key=lambda date: date['date'], reverse=True)
        return json.loads(json.dumps(sorted_list))

    def sort_by_date_descending(self) -> list[dict[str, str]]:
        sorted_list = sorted(self._notes, key=lambda date: date['date'], reverse=False)
        return json.loads(json.dumps(sorted_list))