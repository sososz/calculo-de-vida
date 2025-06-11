import requests

resposta = requests.get("https://api.teleport.org/api/urban_areas/slug:paris/details/")

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)  # Mostra o JSON que a API retornou
else:
    print("Erro ao acessar a API.")
