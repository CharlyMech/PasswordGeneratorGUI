import PySimpleGUI as sg
from random_passwd import *
from db.classes import data_base
from os import getcwd


sg.theme('DarkTanBlue')

# Left pannel buttons
left_pannel = [[sg.Button('New Password', size=(20, 3), font='36', key="rand_passwd")], [sg.T("")],
               [sg.Button('New Pin', size=(20, 3), font='36', key="rand_pin")], [
    sg.T("")],
    [sg.Button('Input Password', size=(20, 3),
               font='36', key="new_passwd")], [sg.T("")],
    [sg.Button('Saved', size=(20, 3), font='36', key="stored")]]


# Define main contents
main = [
    # Content at execution
    [sg.pin(sg.T("Welcome to Random Password Generator", size=(
        50, 1), justification='c', key="main_title", font='40', visible=True))],
    [sg.pin(sg.T("", size=(50, 5),
            key="hidden_line", visible=True))],
    [sg.Image(f"{getcwd()}/src/img/lock_00_128.png",  size=(
        150, 150), key="lock_display", visible=True)],

    # Ramdom Password generator
    [sg.pin(sg.Text("Generate New random password", size=(
        50, 1),  justification='c', key="gen_rand_passwd_TITLE", font='24', visible=False))],
    [sg.pin(sg.Button("Generate", size=(10, 1),
                      key="gen_rand_passwd_BUTTON",  font='18', visible=False))],
    [sg.pin(sg.InputText("Random Password", text_color='gray', size=(25, 1), use_readonly_for_disable=True, disabled=False, justification='c',
                         key="gen_rand_passwd_PASSWD", font='24', visible=False)), sg.pin(sg.Button("Copy", size=(4, 1),
                                                                                                    key="gen_rand_passwd_COPY",  font='18', visible=False))],
    [sg.pin(sg.Button("Save", size=(10, 1),
                      key="gen_rand_passwd_SAVE", font='18', visible=False))],

    # Random PIN generator
    [sg.pin(sg.Text("New Random pin Selected", size=(80, 1), justification='c',
                    key="rand_pin_display", visible=False))],

    # Password manual insertion
    [sg.pin(sg.Text("Insert a Passwd Selected", size=(80, 1), justification='c',
                    key="insert_passwd_display", visible=False))],

    # Stored passwords and pin
    [sg.pin(sg.Text("Passwd and PIN DB display", size=(80, 1), justification='c',
                    key="stored_db_display", visible=False))],
]

# All layout and window generation
layout = [[sg.Column(left_pannel, element_justification='c'),
           sg.VSep(), sg.Column(main, element_justification='c')]]

window = sg.Window('Random Password Generator', layout)


# MAIN #
if __name__ == "__main__":
    data_base()
    # Program loop
    while True:
        event, values = window.read()

        # Style for generated passwd
        #! Commented -> When close window error appears idk why
        # window['gen_rand_passwd_PASSWD'].Widget.config(
        #     readonlybackground=sg.theme_background_color())
        # window['gen_rand_passwd_PASSWD'].Widget.config(borderwidth=0)

        # Random password
        if event == 'rand_passwd':
            window['lock_display'].Update(visible=False)
            window['main_title'].Update(visible=False)
            window['hidden_line'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)

            window['gen_rand_passwd_TITLE'].Update(visible=True)
            window['gen_rand_passwd_BUTTON'].Update(visible=True)
            # window['gen_rand_passwd_PASSWD'].Update(visible=True)

        elif event == 'gen_rand_passwd_BUTTON':
            window['lock_display'].Update(visible=False)
            window['main_title'].Update(visible=False)
            window['hidden_line'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)

            window['gen_rand_passwd_PASSWD'].Update(visible=True)
            window['gen_rand_passwd_PASSWD'].Update(disabled=True)
            window['gen_rand_passwd_PASSWD'].Update(visible=True)
            window['gen_rand_passwd_PASSWD'].Update(text_color='black')
            window['gen_rand_passwd_PASSWD'].Update(random_passwd(12))
            window['gen_rand_passwd_COPY'].Update(visible=True)
            window['gen_rand_passwd_SAVE'].Update(visible=True)

        # Random pin
        if event == 'rand_pin':
            window['lock_display'].Update(visible=False)
            window['main_title'].Update(visible=False)
            window['hidden_line'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)
            window['rand_pin_display'].Update(visible=True)

        # New password
        if event == 'new_passwd':
            window['lock_display'].Update(visible=False)
            window['main_title'].Update(visible=False)
            window['hidden_line'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=True)

        # Show stored passwords and pin
        if event == 'stored':
            window['lock_display'].Update(visible=False)
            window['main_title'].Update(visible=False)
            window['hidden_line'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=True)

        # Exit loop and program
        if event == sg.WIN_CLOSED:
            break

    window.close()
