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
                while True:
                    choice2 = view.main_menu2()
                    match choice2:
                        case 1:
                            notes = my_notes.load()
                            view.print_notes(notes, text.load_error)
                        case 2:
                            note = view.input_note(text.new_note, text.cancel_input, text.oops)
                            title = my_notes.add(note)
                            view.print_message(text.new_note_successful(title))
                            view.print_message(text.reminder)
                        case 3:
                            notes = my_notes.load()
                            index = view.input_index(text.index_note, notes, text.load_error)
                            res = my_notes.search_by_index(index)
                            view.print_message(text.found_note(res))
                        case 4:
                            notes = my_notes.load()
                            index = view.input_index(text.index_change_note, notes, text.load_error)
                            note = view.input_note(text.change_note_msg, text.cancel_input, text.oops)
                            title = my_notes.change(index, note)
                            view.print_message(text.change_note(title))
                            view.print_message(text.reminder)
                        case 5:
                            while True:
                                choice2 = view.sort_menu()
                                match choice2:
                                    case 1:
                                        notes = my_notes.sort_by_date_ascending()
                                        view.print_notes(notes, text.load_error)
                                    case 2:
                                        notes = my_notes.sort_by_date_descending()
                                        view.print_notes(notes, text.load_error)
                                    case 3:
                                        break
                        case 6:
                            notes = my_notes.load()
                            index = view.input_index(text.index_delete_note, notes, text.load_error)
                            title = my_notes.delete(index)
                            view.print_message(text.delete_note(title))
                        case 7:
                            view.print_message(text.reminder)
                            break
            case 2:
                my_notes.save()
                print(view.print_message(text.save_successful))
            case 3:
                break