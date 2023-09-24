escolha = int(input('digite 1 para convert °C para °F\ndigite 2 para converter °F para °C\n'))
if escolha == 1:
    temperatura = float(input('digite a temperatura: '))
    convercao = (temperatura*1.8)+32
    print(f'{temperatura:,.2f}°C convertido  em fahrenheit fica {convercao:,.2f}')
if escolha == 2:
    temperatura =  float(input('digite a temperatura: '))
    convercao = (temperatura-32)/1.8
    print(f'{temperatura:,.2f}°F convertido  em celcius fica {convecao:,.2f}°C')