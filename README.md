# Proyecto-Mineria-de-datos-
Proyecto de clase ITESO
Sarah, Pablo y Diego
# Análisis de Rutas Migratorias de Aves

## Pregunta de Investigación
**¿Es posible identificar la especie de un ave y agrupar sus zonas de destino basándose exclusivamente en los datos numéricos de su trayecto geográfico y físico?**

## Contexto y Justificación
El seguimiento de las rutas migratorias es fundamental en la ecología. Las aves funcionan como excelentes bioindicadores; los cambios en sus patrones de vuelo, destinos y tiempos de migración reflejan directamente las variaciones en el clima y la salud de los ecosistemas que atraviesan. Este proyecto utiliza datos geográficos y climáticos para construir modelos predictivos que pueden ser de utilidad para el monitoreo ambiental y la preservación de especies.

## Modelos Utilizados
Para responder a la pregunta de investigación, el análisis se dividió en dos enfoques principales:

1. **Clasificación de Especies (Aprendizaje Supervisado):**
   * Se evaluaron modelos de **Random Forest**, **K-Nearest Neighbors (KNN)** y **Regresión Logística**.
   * **Objetivo:** Predecir a qué especie pertenece un ave basándose en variables como altitud máxima, velocidad promedio, distancia de vuelo, temperatura y velocidad del viento.

2. **Agrupamiento de Destinos (Aprendizaje No Supervisado):**
   * Se aplicó el algoritmo **K-Means**.
   * **Objetivo:** Encontrar patrones espaciales en las coordenadas de destino (`End_Latitude`, `End_Longitude`) para descubrir zonas de convergencia naturales sin conocer de antemano las regiones geográficas.

## Resultados Principales
* **Identificación de Especies:** Los modelos supervisados demostraron que cada especie tiene un perfil de vuelo medible. Es posible identificar la especie analizando únicamente la telemetría del viaje y el clima.
* **Convergencia Geográfica:** K-Means logró agrupar exitosamente los destinos de migración en 5 clústeres principales, demostrando que el desplazamiento de las aves sigue patrones de convergencia específicos hacia ciertos ecosistemas.

## Conclusión
Sí, es posible. Los datos numéricos de telemetría y clima contienen patrones lo suficientemente definidos para ser modelados. La combinación de modelos supervisados y no supervisados permite no solo clasificar a las aves en vuelo, sino también mapear matemáticamente sus zonas de llegada, lo cual tiene aplicaciones directas en la creación de sistemas de alerta temprana para ecosistemas y en la delimitación de reservas naturales.
