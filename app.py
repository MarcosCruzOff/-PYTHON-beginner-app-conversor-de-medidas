import PySimpleGUI as sg

layout = [
    [   
        sg.Input(key='-INPUT-'),
        sg.Spin(['Km para m', 'Kg para g', 'seg para min'],key='-UNIDADES-'),
        sg.Button('Converter', key='-CONVERTE-')
    ],
    [sg.Text('Saida', key='-SAIDA-')]
]
window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERTE-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNIDADES-']:
                case 'Km para m':
                    output = float(input_value) * 1000
                    output_String = f'{input_value} km para m é: {output} metros.'
                    
                case 'Kg para g':
                    output = float(input_value) * 1000
                    output_String = f'{input_value} kg para g é: {output} gramas.'
                
                case 'seg para min':
                    output = round(float(input_value) / 60, 2)
                    output_String = f'{input_value} segundos para minutos é: {output}'
            
            window['-SAIDA-'].update(output_String)
        
        
window.close()
