main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Сохранить
    3. Показать заметки
    4. Добавить заметку
    5. Найти заметку
    6. Изменить заметку
    7. Удалить заметку
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Заметки успешно открыты'

save_successful = 'Сохранение прошло успешно!'

load_error = 'В заметках пусто или они не открыты'

input_note = {'title': 'Введите заголовок: ', 'body': 'Введите текст: '}

new_note = "Новая заметка!"

oops = 'Для отмены, нажмите "Enter", предварительно сделав поле для заполнения пустым'

cancel_input = 'Ошибка ввода'

index_delete_note = 'Введите индекс заметки, которую хотите удалить: '

index_change_note = 'Введите индекс заметки, которую хотите изменить: '

change_note_msg = 'Введите новые данные'

reminder = 'Не забудьте сохранить изменения'

find = 'Введите для поиска совпадений: '

def new_note_successful(title: str) -> str:
    return f'Заметка {title} успешно добавлена'


def delete_note(title: str) -> str:
    return f'Заметка {title} успешно удалена!'


def change_note(title: str) -> str:
    return f'Заметка {title} успешно изменена!'


def found_note(result) -> str:
    return f'Найдена заметка: {result}'