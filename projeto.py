import requests

# Substitua 'SUA_CHAVE_DE_API' pela chave de API que você obteve no Console do Google Cloud.
API_KEY = ''

# Defina as coordenadas (latitude e longitude) das duas localizações de origem e destino.
#origem = '-10.9481197,-37.0740589'  # Exemplo: San Francisco, CA
#destino = '-10.9534261,-37.0529574'  # Exemplo: Los Angeles, CA
area_geografica = '37.7749,-122.4194,10000'
'''
# Parâmetros da solicitação para a API Directions
params = {
    'origin': origem,
    'destination': destino,
    'mode': 'transit',  # Define o modo de transporte como 'transit' para transporte público.
    'key': API_KEY,
}
'''
params = {
    'location': area_geografica,
    'radius': 10000,  # Raio em metros.
    'type': 'transit_station',  # Tipo de lugar: estações de transporte público.
    'key': API_KEY,
}

# URL da API Directions
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Faz a solicitação GET para a API
response = requests.get(url, params=params)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converte a resposta para JSON
    #print(data)
    # Agora, 'data' contém os dados da rota de transporte público.
    # Você pode analisar esses dados para obter informações sobre a rota, estações, horários, etc.
else:
    print('Falha na solicitação:', response.status_code)
    
# Crie um dicionário para representar o grafo.
grafo = {}
#print(data)

# Itere pelos passos da rota da API para construir o grafo.
for step in data['routes'][0]['legs'][0]['steps']:
    if 'transit_details' in step:
        # Se o passo incluir informações de transporte público.
        linha = step['transit_details']['line']['name']
        partida = step['transit_details']['departure_stop']['name']
        chegada = step['transit_details']['arrival_stop']['name']

        # Adicione as estações de partida e chegada ao grafo, se ainda não estiverem presentes.
        if partida not in grafo:
            grafo[partida] = []
        if chegada not in grafo:
            grafo[chegada] = []

        # Adicione a conexão entre as estações com a linha de transporte.
        grafo[partida].append((chegada, linha))
        grafo[chegada].append((partida, linha))

# Agora, 'grafo' representa as conexões entre as estações com as respectivas linhas de transporte.

print(grafo)
#print("\n\n")
#print(grafo[chegada])
'''
from collections import deque

# Função para realizar a busca em largura (BFS) no grafo
def busca_em_largura(grafo, inicio, destino):
    # Verifica se as estações de início e destino estão presentes no grafo
    if inicio not in grafo or destino not in grafo:
        return None  # Se alguma das estações não existe, retorna None

    # Inicializa a fila para a BFS
    fila = deque()
    fila.append([inicio])  # Inicia a fila com uma lista contendo a estação de início

    while fila:
        caminho = fila.popleft()
        estacao_atual = caminho[-1]

        # Verifica se chegamos ao destino
        if estacao_atual == destino:
            return caminho

        # Percorre todas as estações vizinhas
        for vizinha, linha in grafo[estacao_atual]:
            if vizinha not in caminho:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinha)
                fila.append(novo_caminho)

    return None  # Se não encontrarmos um caminho, retorna None

# Exemplo de uso:
inicio = 'Van Ness Outbound'
destino = 'Spring / Temple'
caminho_mais_curto = busca_em_largura(grafo, inicio, destino)

if caminho_mais_curto:
    print("Caminho mais curto encontrado:", caminho_mais_curto)
else:
    print("Não foi possível encontrar um caminho entre as estações.")
'''
