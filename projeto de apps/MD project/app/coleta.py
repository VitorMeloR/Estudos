def bivolt():
    marca = input("Digite a marca do motor: ").upper().strip()
    modelo = input("Digite o modelo do motor: ").upper().strip()
    pacote = input("Digite o pacote do motor(em mm): ").upper().strip()
    rpm = input("Digite o rpm do motor: ").upper().strip()
    volt = input("Digite a voltagem do motor(se for duas tensões digite ambas separadas por espaços): ").upper().strip()
    if '127110' in volt:
        amp110 = input("Digite a amperagem em 110 do motor: ").upper().strip()
        cod = marca[:3]+modelo[:3]+pacote+rpm+volt+amp110
        cod = cod.replace(' ','')
        return cod
    if '127110' and '220227' in volt:
        amp110 = input("Digite a amperagem em 110 do motor: ").upper().strip()
        amp220 = input("Digite a amperagem em 220 do motor: ").upper().strip()
        cod = marca[:3]+modelo[:3]+pacote+rpm+volt+amp110+amp220
        cod = cod.replace(' ','')
        return cod
    if '380' in volt:
        amp220 = input("Digite a amperagem em 220 do motor: ").upper().strip()
        amp380 = input("Digite a amperagem em 380 do motor: ").upper().strip()
        cod = marca[:3]+modelo[:3]+pacote+rpm+volt+amp220+amp380
        cod = cod.replace(' ','')
        return cod
    

codi = bivolt()
print(codi)