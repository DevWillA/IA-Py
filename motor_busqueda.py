import heapq
from base_conocimiento import rutas_ibague, heuristica_hacia_sena

def busqueda_a_estrella(grafo, heuristica, inicio, destino):
    # Frontera de exploración (Cola de prioridad para elegir siempre el camino más prometedor)
    frontera = []
    heapq.heappush(frontera, (0, inicio))
    
    # Diccionarios para rastrear el camino y los costos
    caminos = {inicio: None}
    costo_acumulado = {inicio: 0}
    
    while frontera:
        _, actual = heapq.heappop(frontera)
        
        # Si llegamos al destino, detenemos la búsqueda
        if actual == destino:
            break
            
        for vecino, costo in grafo[actual].items():
            nuevo_costo = costo_acumulado[actual] + costo
            
            # Actualizamos si encontramos un atajo más rápido o un nodo nuevo
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                # f(n) = g(n) (costo real) + h(n) (heurística)
                prioridad = nuevo_costo + heuristica.get(vecino, 0)
                heapq.heappush(frontera, (prioridad, vecino))
                caminos[vecino] = actual
                
    # Reconstrucción de la ruta óptima
    ruta = []
    nodo = destino
    while nodo is not None:
        ruta.append(nodo)
        nodo = caminos.get(nodo)
    ruta.reverse()
    
    return ruta, costo_acumulado.get(destino, 0)

# Bloque de ejecución para probar el sistema
if _name_ == "_main_":
    punto_a = 'Plaza de Bolivar'
    punto_b = 'Sena'
    
    print(f"Calculando ruta inteligente desde {punto_a} hasta {punto_b}...\n")
    ruta_optima, tiempo_total = busqueda_a_estrella(rutas_ibague, heuristica_hacia_sena, punto_a, punto_b)
    
    print(f"-> Mejor ruta encontrada: {' -> '.join(ruta_optima)}")
    print(f"-> Tiempo total estimado: {tiempo_total} minutos")