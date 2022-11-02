import PySimpleGUI as sg

sg.theme('DarkTanBlue')

# Left pannel buttons
left_pannel = [[sg.Button('New Password', size=(20, 3), font='36', key="rand_passwd")], [sg.T("")],
               [sg.Button('New Pin', size=(20, 3), font='36', key="rand_pin")], [
    sg.T("")],
    [sg.Button('Input Password', size=(20, 3),
               font='36', key="new_passwd")], [sg.T("")],
    [sg.Button('Saved', size=(20, 3), font='36', key="stored")]]

# Define main contents
'''
!   Still working on display every section and functionallity
'''
main = [
    # Content at execution
    [sg.pin(sg.Text("Select an option from left", size=(
        80, 1), key="main_content", visible=True))],
    # Ramdom Password generator
    [sg.pin(sg.Text("New Random password Selected", size=(80, 1),
                    key="rand_passwd_display", visible=False))],
    # Random PIN generator
    [sg.pin(sg.Text("New Random pin Selected", size=(80, 1),
                    key="rand_pin_display", visible=False))],
    # Password manual insertion
    [sg.pin(sg.Text("Insert a Passwd Selected", size=(80, 1),
                    key="insert_passwd_display", visible=False))],
    # Stored passwords and pin
    [sg.pin(sg.Text("Passwd and PIN DB display", size=(80, 1),
                    key="stored_db_display", visible=False))],
]

# All layout and window generation
layout = [[sg.Column(left_pannel, element_justification='c'),
           sg.VSep(), sg.Column(main, element_justification='c')]]

window = sg.Window('Random Password Generator', layout)

# MAIN #
if __name__ == "__main__":
    # Program loop
    while True:
        event, values = window.read()

        # Random password
        if event == 'rand_passwd':
            window['main_content'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=True)

        # Random pin
        elif event == 'rand_pin':
            window['main_content'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)
            window['rand_pin_display'].Update(visible=True)

        # New password
        elif event == 'new_passwd':
            window['main_content'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=True)

        # Show stored passwords and pin
        elif event == 'stored':
            window['main_content'].Update(visible=False)
            window['rand_pin_display'].Update(visible=False)
            window['insert_passwd_display'].Update(visible=False)
            window['rand_passwd_display'].Update(visible=False)
            window['stored_db_display'].Update(visible=True)

        # Exit loop and program
        if event == sg.WIN_CLOSED:
            break

    window.close()
