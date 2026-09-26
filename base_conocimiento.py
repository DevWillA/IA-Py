# base_conocimiento.py

# Grafo que representa las conexiones directas y el tiempo en minutos entre puntos de Ibagué
rutas_ibague = {
    'Plaza de Bolivar': {'Terminal de Transportes': 12, 'Universidad del Tolima': 15},
    'Terminal de Transportes': {'Plaza de Bolivar': 12, 'Sena': 8, 'Mirolindo': 20},
    'Universidad del Tolima': {'Plaza de Bolivar': 15, 'Sena': 5, 'Estadio Murillo Toro': 10},
    'Sena': {'Terminal de Transportes': 8, 'Universidad del Tolima': 5, 'El Salado': 25},
    'Estadio Murillo Toro': {'Universidad del Tolima': 10, 'Mirolindo': 12},
    'Mirolindo': {'Terminal de Transportes': 20, 'Estadio Murillo Toro': 12, 'Picaleña': 15},
    'El Salado': {'Sena': 25},
    'Picaleña': {'Mirolindo': 15}
}

# Heurística: Estimación de tiempo "en línea recta" o ideal hacia un destino específico (Ej. hacia el 'Sena').
# Esta guía es lo que vuelve "inteligente" a la búsqueda para que el algoritmo no explore a ciegas.
heuristica_hacia_sena = {
    'Plaza de Bolivar': 12,
    'Terminal de Transportes': 7,
    'Universidad del Tolima': 4,
    'Sena': 0,
    'Estadio Murillo Toro': 8,
    'Mirolindo': 18,
    'El Salado': 20,
    'Picaleña': 25
}