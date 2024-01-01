import PySimpleGUI as sg
import csv

sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
layout = [  [sg.Text('Enter your name'), sg.Push(), sg.InputText(key='-name-')],
            [sg.Text('Enter Phone Number'), sg.Push(), sg.InputText(key='-phone-')],
            [sg.Text('Enter Email'), sg.Push(), sg.InputText(key='-email-')],
            [sg.Text('Enter Address'), sg.Push(), sg.InputText(key='-address-')],
            [sg.Button('Save'), sg.Button('Update'), sg.Button('Cancel')],
            [sg.Text('Search By Name'), sg.Push(), sg.InputText(key='-searchText-')],
            [sg.Button('Search')],
            [sg.Text(key='-searchOutput-')],
            [sg.Button('View All')],
            [sg.Multiline(size=(50, 10), key='-viewOutput-', disabled=True)],
            [sg.Text('Delete Record by Name'), sg.Push(), sg.InputText(key='-deleteText-')],
            [sg.Button('Delete')],
            [sg.Text(key='-deleteOutput-')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    name = values['-name-']
    phone = values['-phone-']
    email = values['-email-']
    address = values['-address-']
    info = [name, phone, email, address]
    if event == 'Save':
        with open('info.csv','a', newline="") as w:
            cw = csv.writer(w)
            cw.writerow(info)
        window['-name-'].update('')
        window['-phone-'].update('')
        window['-email-'].update('')
        window['-address-'].update('')
    
    if event == 'Update':
        update_text = values['-searchText-']
        with open('info.csv', 'r') as r:
            cr = csv.reader(r)
            lines = list(cr)
        
        found = False
        with open('info.csv', 'w', newline='') as w:
            cw = csv.writer(w)
            for line in lines:
                if line and line[0] == update_text:
                    cw.writerow(info)
                    found = True
                    window['-name-'].update('')
                    window['-phone-'].update('')
                    window['-email-'].update('')
                    window['-address-'].update('')
                else:
                    cw.writerow(line)
        
        if found:
            window['-searchOutput-'].update(f"Contact details for '{update_text}' updated successfully.")
        else:
            window['-searchOutput-'].update(f"Contact details for '{update_text}' not found.")
    
    searchText = values['-searchText-']
    if event == 'Search':
        with open('info.csv','r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i and i[0] == searchText:
                    window['-searchOutput-'].update(f"Name: {i[0]}\nPhone Number: {i[1]}\nEmail: {i[2]}\nAddress: {i[3]}")
    
    if event == 'View All':
        view_text = ""
        with open('info.csv','r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i:
                    view_text += f"Name: {i[0]}\nPhone Number: {i[1]}\nEmail: {i[2]}\nAddress: {i[3]}\n\n"
            window['-viewOutput-'].update(view_text)
    
    delete_text = values['-deleteText-']
    if event == 'Delete':
        found = False
        with open('info.csv', 'r', newline='') as file:
            lines = list(csv.reader(file))
        with open('info.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line and line[0] == delete_text:
                    found = True
                else:
                    writer.writerow(line)

        if found:
            window['-deleteOutput-'].update(f"Record for '{delete_text}' deleted successfully.")
        else:
            window['-deleteOutput-'].update(f"Record for '{delete_text}' not found.")

window.close()
