import requests

def buscar_cep(cep_input):
    request = requests.get(f'https://cep.awesomeapi.com.br/json/{cep_input}')
    print(request)
    if request.status_code == 200:
        cep = request.json()
        return cep
    elif request.status_code == 400:
        return 'CEP inválido'
    elif request.status_code == 404:
        return 'CEP não encontrado'
    
def filtrage(cep):
    dict_cep = cep
    cep_filtrado = [dict_cep['state'],
                    dict_cep['ddd'],
                    dict_cep['city'],
                    dict_cep['district'],
                    dict_cep['address'],
                    dict_cep['city_ibge']
    ]
    return cep_filtrado
