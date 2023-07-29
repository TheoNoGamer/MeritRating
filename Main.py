import PySimpleGUI as sg

text_size = (1, 1)
input_size = (2, 2)

layout = [
    [sg.Text('F', size=text_size), sg.Input('0', key='F_input', size=input_size),
     sg.Text('E', size=text_size), sg.Input('0', key='E_input', size=input_size),
     sg.Text('D', size=text_size), sg.Input('0', key='D_input', size=input_size),
     sg.Text('C', size=text_size), sg.Input('0', key='C_input', size=input_size),
     sg.Text('B', size=text_size), sg.Input('0', key='B_input', size=input_size),
     sg.Text('A', size=text_size), sg.Input('0', key='A_input', size=input_size)],
    [sg.Text('Ditt meritvärde är:', font='40'), 
     sg.Text('', font='40', key='-merit-'), 
     sg.Push(), sg.Button('Update')]
]

F_poäng = 0
E_poäng = 10
D_poäng = 12.5
C_poäng = 15
B_poäng = 17.5
A_poäng = 20

current_num = []

window = sg.Window('Meritvärde', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Update':
        F_value = int(values['F_input'])  
        E_value = int(values['E_input'])  
        D_value = int(values['D_input'])  
        C_value = int(values['C_input'])  
        B_value = int(values['B_input'])  
        A_value = int(values['A_input'])  
        
        current_num = [F_value, E_value, D_value, C_value, B_value, A_value] 
        
        print(current_num)
        
        total_merit = sum(grade_points * grade_value for grade_points, grade_value in zip(current_num, [F_poäng, E_poäng, D_poäng, C_poäng, B_poäng, A_poäng]))
        window['-merit-'].update(f'{total_merit:.1f}')
    
window.close()
