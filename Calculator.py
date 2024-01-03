import PySimpleGUI as sg

sg.theme('DarkGrey2')  

layout = [  [sg.Text('ARITHEMETIC CALCULATOR')],
            [sg.Text('Enter Fist Value '),sg.Push(), sg.InputText(key='-val1-')],
            [sg.Text('Enter Second Value '),sg.Push(), sg.InputText(key='-val2-')],
            [sg.Button(' + '), sg.Button(' - '),sg.Button(' / '), sg.Button(' * '),sg.Push(), sg.Button('Clear')],
            [sg.Text(key='-Output-')]]


window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
        break
    
    try:

        value1 = int(values['-val1-'])
        value2 = int(values['-val2-'])

        #ADDITION
        if event == ' + ':
            Result = value1 + value2
            
        #SUBSTRACTION
        if event == ' - ':
            Result = value1 - value2
        
        #MULTIPLICATION
        if event == ' * ':
            Result = value1 * value2

        #DIVISION
        if event == ' / ':
            if value2 != 0 :
                  Result = value1 / value2
            else:
                  Result = "Error: Division by Zero"

        window['-Output-'].update(f"Result: {Result}")

        if event == 'Clear':
          window['-val1-'].update('')  
          window['-val2-'].update('')  
          window['-Output-'].update('')   
    
    except ValueError:
            window['-Output-'].update("Error: Invalid Input")

    

window.close()
