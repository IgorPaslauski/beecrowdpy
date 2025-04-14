from collections import deque

def find_shortest_path(graph, start, end, cheese):
    # BFS para encontrar o caminho mais curto
    queue = deque([[start]])
    visited = {start}

    if start == end:
        return 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        # Verifica todas as conexões do nó atual
        for next_node in graph[node]:
            if next_node not in visited:
                if next_node == cheese:
                    # Se encontrarmos o queijo, continuamos a busca até a saída
                    new_path = path + [next_node]
                    queue_cheese = deque([new_path])
                    visited_cheese = visited | {next_node}
                    
                    while queue_cheese:
                        cheese_path = queue_cheese.popleft()
                        cheese_node = cheese_path[-1]

                        for next_cheese in graph[cheese_node]:
                            if next_cheese not in visited_cheese:
                                if next_cheese == end:
                                    return len(cheese_path) - 1  # Retorna movimentos até a saída
                                visited_cheese.add(next_cheese)
                                queue_cheese.append(cheese_path + [next_cheese])
                elif next_node == end:
                    # Se chegarmos diretamente à saída sem passar pelo queijo
                    return len(path)
                else:
                    visited.add(next_node)
                    queue.append(path + [next_node])

    return -1  # Se não houver caminho

# Leitura da entrada
n, m = map(int, input().split())  # n e m não parecem ser usados, mas mantidos por segurança
input_line = input()  # Linha "Entrada A" (ponto de entrada e primeiro nó)

# Criando o grafo
graph = {}
nodes = set()

# Adicionando arestas ao grafo
for _ in range(m):
    a, b = input().split()
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)  # Grafo não direcionado
    nodes.add(a)
    nodes.add(b)

# Adicionando entrada e saída fictícias se não existirem
start_node = "Entrada"
end_node = "Saida"
cheese = "*"

if start_node not in graph:
    graph[start_node] = []
if end_node not in graph:
    graph[end_node] = []

# Conectando entrada e saída aos primeiros/últimos nós conforme a entrada
first_connection = input_line.split()[1]  # Primeiro nó após "Entrada"
last_connection = [node for node in graph if "Saida" in graph[node]][0] if "Saida" in nodes else None

if first_connection in graph:
    graph[start_node].append(first_connection)
    graph[first_connection].append(start_node)

if last_connection:
    graph[end_node].append(last_connection)
    graph[last_connection].append(end_node)

# Verificando conexões adicionais fornecidas
extra_connections = []
while True:
    try:
        line = input()
        if not line:
            break
        a, b = line.split()
        extra_connections.append((a, b))
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
        nodes.add(a)
        nodes.add(b)
    except EOFError:
        break

# Calculando o caminho mais curto
shortest_path_length = find_shortest_path(graph, start_node, end_node, cheese)

print(shortest_path_length)
