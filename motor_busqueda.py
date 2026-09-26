import heapq
from base_conocimiento import rutas_ibague, obtener_heuristica_hacia_destino

class MotorDeInferencia:
    def _init_(self, base_hechos):
        self.grafo = base_hechos

    def busqueda_inteligente(self, inicio, destino):
        # 1. Cargar la heurística específica para el destino
        heuristica = obtener_heuristica_hacia_destino(destino)
        
        # 2. Frontera de búsqueda (Cola de prioridad)
        # Guarda tuplas de (costo_total_f, nodo_actual)
        frontera = []
        heapq.heappush(frontera, (0, inicio))
        
        # 3. Diccionarios de rastreo
        caminos_logicos = {inicio: None}
        costo_real_g = {inicio: 0}
        
        while frontera:
            # Extraer el nodo más prometedor
            _, actual = heapq.heappop(frontera)
            
            # Regla de parada: Se alcanzó la conclusión/destino
            if actual == destino:
                break
                
            # Explorar conexiones (aplicar reglas lógicas de movimiento)
            for vecino, tiempo_viaje in self.grafo[actual].items():
                nuevo_costo = costo_real_g[actual] + tiempo_viaje
                
                # Si encontramos un camino más rápido hacia el vecino
                if vecino not in costo_real_g or nuevo_costo < costo_real_g[vecino]:
                    costo_real_g[vecino] = nuevo_costo
                    
                    # f(n) = g(n) (costo real) + h(n) (heurística estimada)
                    valor_heuristico = heuristica.get(vecino, 0)
                    prioridad = nuevo_costo + valor_heuristico
                    
                    heapq.heappush(frontera, (prioridad, vecino))
                    caminos_logicos[vecino] = actual
                    
        return self._reconstruir_ruta(caminos_logicos, inicio, destino), costo_real_g.get(destino, -1)

    def _reconstruir_ruta(self, caminos, inicio, destino):
        ruta = []
        actual = destino
        if actual not in caminos and actual != inicio:
            return [] # No existe conexión lógica
            
        while actual is not None:
            ruta.append(actual)
            actual = caminos.get(actual)
        ruta.reverse()
        return ruta

# --- PRUEBA Y EJECUCIÓN DEL SISTEMA ---
if _name_ == "_main_":
    print("="*55)
    print(" SISTEMA INTELIGENTE DE BÚSQUEDA DE RUTAS - IBAGUÉ ")
    print("="*55)
    
    # Instanciamos el motor cargando los hechos
    sistema_experto = MotorDeInferencia(rutas_ibague)
    
    origen = 'El Salado'
    destino = 'Centro (Plaza de Bolívar)'
    
    print(f"\n[!] Procesando la mejor ruta desde '{origen}' hasta '{destino}'...")
    
    ruta_optima, tiempo_total = sistema_experto.busqueda_inteligente(origen, destino)
    
    if ruta_optima:
        print(f"\n[+] Conclusión Lógica - Ruta Óptima encontrada:")
        print(" -> ".join(ruta_optima))
        print(f"\n[+] Tiempo total estimado: {tiempo_total} minutos")
    else:
        print("\n[-] Error: No se pudo deducir una ruta entre los puntos indicados.")