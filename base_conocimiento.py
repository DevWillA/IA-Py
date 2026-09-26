# base_conocimiento.py

# HECHOS: Grafo que representa las conexiones y el tiempo promedio en minutos (peso).
rutas_ibague = {
    'El Salado': {'Sena': 10, 'Parque de los Venados': 15},
    'Sena': {'El Salado': 10, 'Éxito de la 80': 8, 'Terminal de Transportes': 20},
    'Parque de los Venados': {'El Salado': 15, 'Centro (Plaza de Bolívar)': 30},
    'Éxito de la 80': {'Sena': 8, 'Multicentro': 5, 'Mirolindo': 12},
    'Multicentro': {'Éxito de la 80': 5, 'Universidad del Tolima': 10, 'Estadio Murillo Toro': 15},
    'Universidad del Tolima': {'Multicentro': 10, 'Terminal de Transportes': 12, 'Centro (Plaza de Bolívar)': 15},
    'Mirolindo': {'Éxito de la 80': 12, 'Terminal de Transportes': 18, 'Picaleña': 20},
    'Terminal de Transportes': {'Sena': 20, 'Universidad del Tolima': 12, 'Mirolindo': 18, 'Centro (Plaza de Bolívar)': 10},
    'Estadio Murillo Toro': {'Multicentro': 15, 'Centro (Plaza de Bolívar)': 8},
    'Centro (Plaza de Bolívar)': {'Universidad del Tolima': 15, 'Terminal de Transportes': 10, 'Estadio Murillo Toro': 8, 'Parque de los Venados': 30},
    'Picaleña': {'Mirolindo': 20}
}

# REGLA HEURÍSTICA: Estimación del costo (en minutos ideales) hacia un destino.
# Esta evaluación heurística guía al algoritmo para que no busque a ciegas.
def obtener_heuristica_hacia_destino(destino):
    """
    Retorna un diccionario con la heurística (h(n)) hacia un destino específico.
    En este caso, simularemos la heurística asumiendo que el destino es el 'Centro (Plaza de Bolívar)'.
    """
    if destino == 'Centro (Plaza de Bolívar)':
        return {
            'El Salado': 35,
            'Sena': 25,
            'Parque de los Venados': 20,
            'Éxito de la 80': 22,
            'Multicentro': 18,
            'Universidad del Tolima': 10,
            'Mirolindo': 25,
            'Terminal de Transportes': 8,
            'Estadio Murillo Toro': 5,
            'Centro (Plaza de Bolívar)': 0,
            'Picaleña': 40
        }
    else:
        # Retorna una heurística neutra (0) si el destino es otro, 
        # convirtiendo la búsqueda en un Algoritmo de Dijkstra tradicional.
        return {}