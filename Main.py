import PySimpleGUI as sg

text_size = (1, 1)
input_size = (2, 2)

text_size2 = (5, 1)
input_size2 = (4, 2)

def create_window(theme):
    sg.theme(theme)

    tab_points_layout = [
        [sg.Text('F_point', size=text_size2), sg.Input('0', key='F_point', size=input_size2),
        sg.Text('E_point', size=text_size2), sg.Input('10', key='E_point', size=input_size2),
        sg.Text('D_point', size=text_size2), sg.Input('12.5', key='D_point', size=input_size2)],
        [sg.Text('C_point', size=text_size2), sg.Input('15', key='C_point', size=input_size2),
        sg.Text('B_point', size=text_size2), sg.Input('17.5', key='B_point', size=input_size2),
        sg.Text('A_point', size=text_size2), sg.Input('20', key='A_point', size=input_size2)]
    ]

    tab_grades_layout = [
        [sg.Text('F', size=text_size), sg.Input('0', key='F_input', size=input_size),
        sg.Text('E', size=text_size), sg.Input('0', key='E_input', size=input_size),
        sg.Text('D', size=text_size), sg.Input('0', key='D_input', size=input_size),
        sg.Text('C', size=text_size), sg.Input('0', key='C_input', size=input_size),
        sg.Text('B', size=text_size), sg.Input('0', key='B_input', size=input_size),
        sg.Text('A', size=text_size), sg.Input('0', key='A_input', size=input_size)],
        [sg.Text('Your merit rating is:', font='40', size=(16, 1)),
        sg.Text('0', font='40', key='-merit-'),
        sg.Push(), sg.Button('Update')]
    ]

    layout = [
        [sg.TabGroup([
            [sg.Tab('Grades Input', tab_grades_layout)],
            [sg.Tab('Points Input', tab_points_layout)]
            
        ], enable_events=True)]
]

    

    return sg.Window('Merit Rating', layout)

window = create_window('SandyBeach') 
    
current_num = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Update':
        
        F_points = float(values['F_point'])
        E_points = float(values['E_point'])
        D_points = float(values['D_point'])
        C_points = float(values['C_point'])
        B_points = float(values['B_point'])
        A_points = float(values['A_point'])


        Points = [F_points, E_points, D_points, C_points, B_points, A_points]
        
        F_value = int(values['F_input'])  
        E_value = int(values['E_input'])  
        D_value = int(values['D_input'])  
        C_value = int(values['C_input'])  
        B_value = int(values['B_input'])  
        A_value = int(values['A_input'])  
        
        current_num = [F_value, E_value, D_value, C_value, B_value, A_value] 
        
        print(current_num)
        
        total_merit = sum(grade_points * grade_value for grade_points, grade_value in zip(current_num, Points))
        window['-merit-'].update(f'{total_merit:.1f}')
    
window.close()
