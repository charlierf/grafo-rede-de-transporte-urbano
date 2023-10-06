import requests

# Substitua 'SUA_CHAVE_DE_API' pela chave de API que você obteve no Console do Google Cloud.
API_KEY = ''

# Defina as coordenadas (latitude e longitude) das duas localizações de origem e destino.
#origem = '-10.9481197,-37.0740589'  # Exemplo: San Francisco, CA
#destino = '-10.9534261,-37.0529574'  # Exemplo: Los Angeles, CA
area_geografica = '-10.9481197,-37.0740589'

# Parâmetros da solicitação para a API Places
params = {
    'location': area_geografica,
    'radius': 2000000,  # Raio em metros.
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
print(data['results'])
'''
# Itere pelas estações obtidas da API Places.
for station in data['results']:
    station_name = station['name']
    station_location = station['geometry']['location']

    # Adicione a estação como um vértice no grafo, se ainda não estiver presente.
    if station_name not in grafo:
        grafo[station_name] = []

    # Itere pelas outras estações para encontrar conexões (arestas).
    for other_station in data['results']:
        if other_station != station:
            other_station_name = other_station['name']
            other_station_location = other_station['geometry']['location']

            # Calcule a distância entre as estações (pode ser usado como peso da aresta).
            # Neste exemplo, estamos usando a distância euclidiana simples.
            distance = ((station_location['lat'] - other_station_location['lat'])**2 +
                        (station_location['lng'] - other_station_location['lng'])**2)**0.5

            # Adicione a conexão entre as estações com a distância como peso da aresta.
            grafo[station_name].append((other_station_name, distance))

# Agora, 'grafo' representa as conexões entre as estações com as respectivas distâncias como pesos de aresta.

# Exemplo de como acessar o grafo:
#print(grafo)

for chave in grafo.keys():
  print(f'Chave = {chave} \n')#Valor = {grafo[chave]}\n')

#print("\n\n")
#print(grafo[chegada])

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
inicio = 'Rodoviaria De Aracaju'
destino = 'R. Delmiro Gouvêia, 2920 - Atalaia, Aracaju - SE, 49035-810, Brasil'
caminho_mais_curto = busca_em_largura(grafo, inicio, destino)

if caminho_mais_curto:
    print("Caminho mais curto encontrado:", caminho_mais_curto)
    for estacao in caminho_mais_curto:
        print(estacao)
else:
    print("Não foi possível encontrar um caminho entre as estações.")
'''
