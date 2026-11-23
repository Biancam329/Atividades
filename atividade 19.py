Consumo de API REST (ViaCEP): Utilizando a biblioteca requests, crie uma função que
receba um CEP, consulte a API pública 
[https://viacep.com.br/ws/](https://viacep.com.br/ws/){cep}/json/ e exiba 
o endereço completo formatado, tratando erros de conexão ou CEP inválido.

RESPOSTA:
import requests

def consultar_cep(cep):
    cep_limpo = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}")
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")

consultar_cep("74000-000")
