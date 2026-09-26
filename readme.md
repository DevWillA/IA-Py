# Sistema Inteligente de Búsqueda de Rutas - Ibagué 🚌

Este proyecto es un sistema inteligente basado en conocimiento y búsqueda heurística (Algoritmo A*). Fue desarrollado para dar solución a la Actividad 3 del curso, enfocada en la representación del conocimiento a partir de reglas y estrategias de búsqueda.

El objetivo principal del sistema es encontrar la ruta más eficiente (de menor tiempo) entre un Punto A y un Punto B dentro de una red simplificada del sistema de transporte de la ciudad de Ibagué.

## 👥 Equipo de Trabajo

* **William Javier Amaya:** Diseño de la Base de Conocimiento (Abstracción del mapa, definición de nodos, pesos y reglas heurísticas).
* **Miguel Ángel Tabares:** Desarrollo del Motor de Inferencia y Búsqueda (Implementación del algoritmo A*).

## 📂 Estructura del Proyecto

El código está modularizado en dos archivos principales para separar los datos lógicos del algoritmo de procesamiento:

1. **`base_conocimiento.py`**: Almacena los *hechos* del sistema. Contiene el grafo que representa las estaciones y los tiempos de conexión (pesos), así como las funciones que dictan las reglas heurísticas para guiar la búsqueda.
2. **`motor_busqueda.py`**: Es el motor de inferencia. Importa la base de datos y ejecuta el algoritmo **A-Estrella (A*)**, evaluando el costo real acumulado $g(n)$ más la estimación heurística $h(n)$ para deducir el camino óptimo.

## 🚀 Instrucciones de Ejecución

### Prerrequisitos
* Python 3.x instalado en el sistema.
* No se requieren instalaciones de librerías externas (el proyecto utiliza la librería estándar `heapq`).

### ¿Cómo probar el sistema?
1. Clona este repositorio o descarga los archivos en una misma carpeta.
2. Abre una terminal o símbolo del sistema (CMD/PowerShell).
3. Navega hasta el directorio donde guardaste los archivos.
4. Ejecuta el script del motor de búsqueda con el siguiente comando:

   ```bash
   python motor_busqueda.py
   ```

5. Por consola se mostrará el análisis paso a paso, imprimiendo la conclusión lógica con la mejor ruta encontrada y el tiempo total del trayecto en minutos.

## 📹 Sustentación
El desarrollo, la explicación de los comandos en Python y las pruebas de ejecución se encuentran documentadas en nuestro video de sustentación (Enlace adjunto en el documento PDF de la entrega).

## 📚 Bibliografía
* Benítez, R. (2014). *Inteligencia artificial avanzada*. Barcelona: Editorial UOC. (Conceptos aplicados de los Capítulos 2, 3 y 9).