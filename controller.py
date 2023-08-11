import datetime

import view
import model
import text

def start():
    my_notes = model.Notes()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_notes.open()
                view.print_message(text.load_successful)
            case 2:
                my_notes.save()
                print(view.print_message(text.save_successful))
            case 3:
                notes = my_notes.load()
                view.print_notes(notes, text.load_error)
            case 4:
                note = view.input_note(text.new_note, text.cancel_input, text.oops)
                title = my_notes.add(note)
                view.print_message(text.new_note_successful(title))
                view.print_message(text.reminder)
            case 5:
                find = view.find_note(text.find)
                res = my_notes.search(find)
                view.print_message(text.found_note(res))
            case 6:
                notes = my_notes.load()
                index = view.input_index(text.index_change_note, notes, text.load_error)
                note = view.input_note(text.change_note_msg, text.cancel_input, text.oops)
                title = my_notes.change(index, note)
                view.print_message(text.change_note(title))
                view.print_message(text.reminder)
            case 7:
                notes = my_notes.load()
                index = view.input_index(text.index_delete_note, notes, text.load_error)
                title = my_notes.delete(index)
                view.print_message(text.delete_note(title))
            case 8:
                break
