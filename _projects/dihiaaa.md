---
title: Proyectos desarrollados por el IAAA y subvencionados por el PROGRAMA DE APOYO A DIGITAL INNOVATION HUBS (DIH_01) dentro del ARAGON EDIH/ARAGON EUROPEAN DIGITAL INNOVATION HUB
acron: IAAA-DIH
code: 
keywords: Inteligencia Artificial, Islas de calor, Agregador de Noticias, Agricultura, Precio combustibles
years: 2023 - 2025
layout: project_website_page
---


# Convocatoria
En esta web se recogen detalles de los proyectos desarrollados por el IAAA y subvencionados por el PROGRAMA DE APOYO A DIGITAL INNOVATION HUBS (DIH_01) dentro del ARAGON EDIH/ARAGON EUROPEAN DIGITAL INNOVATION HUB (Ministerio de Industria, Comercio y Turismo y European Union - Next Generation)


<img src='{{site.baseurl}}/images/other-logos/logoDIH-EOI.png' width='800' style="margin-bottom: 40px;">


# Experimentación destinada a la validación del uso de imágenes de satélite para poder identificar emisiones de calor en zonas urbanas con sensores no diseñados con este fin (2023/DIH_01/000240)

El objetivo de este proyecto ha sido era evaluar el uso de inteligencia artificial para identificar islas de calor en ciudades, un fenómeno urbano donde la acumulación térmica impide el enfriamiento nocturno. Con este fin, se tomó como punto de partida una propuesta de la empresa sobre el uso de métodos alternativos a los sensores térmicos de Sentinel-3, que, aunque precisos, tienen una resolución demasiado baja (1 km² por píxel) para aplicaciones urbanas. Se intentó correlacionar datos de Sentinel-2 y Sentinel-3, pero no se encontró relación suficiente para mejorar la precisión de las imágenes térmicas.
  
Adicionalmente, el trabajo ha incluido: Una revisión del estado del arte en detección de islas de calor mediante IA y teledetección; Un análisis de correlación entre Sentinel-2 y Sentinel-3; Una serie de experimentos y desarrollos tecnológico dirigidos a conseguir la reproducción del mapa de islas de calor del Ayuntamiento de Zaragoza (que se publican por esta entidad en su Web); Una aproximación al problema de identificación de islas de calor mediante el uso de datos de estaciones meteorológicas privadas; y El desarrollo de una red neuronal para predecir islas de calor sin necesidad de sensores físicos.
  
Los resultados obtenidos a lo largo de todo el trabajo desarrollado se pueden resumir en:
  
●	Análisis de Sentinel-2 y Sentinel-3: Se comprobó que no existía correlación suficiente para mejorar la resolución de las imágenes térmicas urbanas.
  
●	Mapas de islas de calor en Zaragoza: Se replicaron mapas existentes usando imágenes satelitales y se aplicó el método de interpolación Kriging, obteniendo resultados precisos en áreas con datos meteorológicos confiables. De este modo, se comprobó que la metodología del Ayuntamiento de Zaragoza es replicable con datos adecuados.
  
●	Uso de estaciones privadas: Se exploró el uso de redes meteorológicas privadas para generar mapas térmicos urbanos. Tras aplicar filtros de calidad, se logró obtener datos útiles para la modelización de islas de calor. De este modo, se puede concluir que las estaciones meteorológicas privadas pueden ser una alternativa viable en ausencia de datos oficiales.
  
●	Desarrollo de IA: Se diseñó una red neuronal inspirada en U-Net para predecir zonas de calor sin datos meteorológicos. Se logró una precisión alta, con un error medio de 0.11°C, mucho menor que el de modelos tradicionales. Así, se puede establecer que la IA permite predecir con alta precisión las zonas afectadas por islas de calor sin necesidad de sensores físicos.
  
A modo de conclusión última, se puede afirmar que este trabajo establece una base sólida para futuros desarrollos en la detección de islas de calor mediante técnicas avanzadas de teledetección e inteligencia artificial.
  
Los resultados del trabajo a llevar a cabo se sustentan en dos entregables:
  
●	Un informe en el que se recoge todas las experimentaciones llevadas a cabo durante el proyecto, así como las conclusiones extraídas del análisis de las mismas.
  
●	El código fuente de todas las mencionadas experimentaciones. Este código fuente permitirá a la empresa repetir los experimentos que se han llevado a cabo, así como servir de base para el diseño de nuevos que puedan ser considerados necesarios.
  
Desarrollado para: [Geospatiumlab, s.l.](https://www.geoslab.com)
  
  
  
# Tecnología base para el desarrollo de un agregador de noticias agrarias basado en procesado de lenguaje natural (2023/DIH_01/000320)

La agricultura tradicional ha formado parte de la actividad humana desde tiempos antiguos, en los que las tareas en el campo eran realizadas manualmente. Con el paso del tiempo, se empezó a contar con la ayuda de animales para llevar a cabo las tareas más arduas, y posteriormente, las máquinas fueron incorporadas a la actividad agrícola con el fin de aligerar el esfuerzo humano en las labores de cultivo. Actualmente, la tendencia natural es delegar cada vez más dichas tareas a máquinas y sistemas automatizados, siempre bajo la supervisión y dirección de los seres humanos, y con la asistencia de sistemas inteligentes que permiten tomar decisiones óptimas, mejorando así la eficiencia y reduciendo los costes asociados a la producción agrícola.
  
En los últimos años, se ha observado un incremento exponencial en la cantidad de información útil para dichos sistemas automáticos disponible en la red, lo cual ha sido posible gracias al crecimiento vertiginoso de los medios digitales y las redes sociales. No obstante, dicha información se encuentra dispersa en una amplia variedad de fuentes y formatos, lo que dificulta en gran medida su procesamiento y análisis por parte de los interesados en la materia. Este hecho puede resultar particularmente problemático en un sector como la agricultura, en el que la información actualizada y precisa puede ser crucial para la toma de decisiones acertadas en áreas como la gestión de recursos, el control de plagas y enfermedades, y la mejora de la productividad y la calidad de los cultivos.
  
En este contexto, la empresa se ha embarcado en el diseño y la implementación de un buscador y clasificador de noticias especializado en el ámbito agrícola. Este buscador y clasificador ●	ne como objetivo recopilar y estructurar de manera eficiente la información disponible en la red sobre agricultura. Además, este buscador y clasificador de noticias sobre agricultura facilitará la tarea de mantenerse actualizado en un campo tan dinámico. Los usuarios podrán acceder de manera rápida y sencilla a información relevante, como avances tecnológicos en el sector agrícola, investigaciones científicas, políticas y regulaciones vigentes, tendencias de mercado, consejos prácticos y casos de éxito en la industria.
  
Como elemento de base para poder construir el sistema que se plantea, se necesita disponer de las adecuadas herramientas y tecnologías avanzadas en los campos de la ciencia de datos y el procesamiento de lenguaje natural que posibiliten la extracción de datos relevantes provenientes de diversas fuentes, su adaptación a un formato común y su almacenamiento y clasificación en una base de datos centralizada. 
  
El trabajo técnico desarrollado ha buscado determinar cuál es la mejor aproximación tecnológica para la integración de los recursos de noticias agrarias en el sistema agregador, así como sobre qué modelos y herramientas de procesado de lenguaje natural se debería construir el sistema que la empresa quiere desarrollar. Concretamente, se ha llevado a cabo los siguientes trabajos:
  
●	El primer problema abordado ha correspondido con la extracción, transformación y almacenamiento de datos de las noticias que se encuentran publicadas en los diferentes sitios web. 
  
●	Seguidamente ha sido necesario poder establecer cuál debe ser el flujo de trabajo para que el desarrollo de un agregador pueda escalar y evolucionar según lo hace la publicación de contenidos de referencia. 
  
●	Como tercer paso se ha abordado el problema de la indexación de las noticias. Para ello, se ha hecho un exhaustivo análisis de las posibilidades que ofrecen tanto los modelos de embeddings generalistas, como los especializados.
  
●	A continuación, se ha abordado el problema de la permanencia viva de los contenidos en la web. Para ello, se ha planteado la necesidad de contar con un revisor de noticias que sea capaz de controlar la accesibilidad a las mismas (siguen estando disponibles), así como si han sido actualizadas.
  
Finalmente, se ha elaborado una propuesta de API de acceso a los componentes tecnológicos realizados, junto con un prototipo demostrador que pueda servir de referencia para que la empresa lleve a cabo sus futuros desarrollos tecnológicos en la línea de lo ya expuesto.
  
Como resultado de estos trabajos, la empresa ha recibido un completo informe, así como el código fuente desarrollado para las pruebas y mecanismos de evaluación desarrollados, así como el prototipo construido. Todo ello va a permitir a la PYME la puesta en marcha de un desarrollo tecnológico propio que pueda integrarse como parte de sus productos.
  
Desarrollado para: [7eData Business, s.l.](https://https://7edata.com)
  
  
  
# Experimentación destinada a la validación de tecnologías de base para el desarrollo de un componente software para la fijación de precio óptimo de combustibles para vehículos (2023/DIH_01/000414)

El incremento del precio de los carburantes en los últimos años ha llevado a que consumidores/as estudien con más detalle el precio que se ofrece por las estaciones de servicio para decidir en cuál se compra. Así mismo, la obligación de notificar al Ministerio para la Transición Ecológica las modificaciones de los precios de venta casi en tiempo real, y la correspondiente exposición pública de estos precios por parte de esta entidad, lleva a que profesionales y ciudadanía en general cuenten con cada vez más información para tomar sus decisiones de compra de carburantes.
  
Por otro lado, los puntos de venta tratan de aprovechar al máximo también esta información, junto con otros datos que pueden recopilar, para llevar a cabo una gestión de precios de venta que permita maximizar la rentabilidad de las operaciones de repostaje sobre la base del estudio de la competencia y de las dinámicas de la clientela. De este modo, en algunos casos, se realizan actualizaciones de precio cada hora.
  
En este contexto, la empresa se ha embarcado en el desarrollo de un módulo que permita incluir en su ERP de gestión de estaciones de servicio funcionalidades de ayuda a la fijación de precio cada hora de los diferentes combustibles basadas en técnicas de inteligencia artificial. En cada implantación del ERP, este módulo se conectará a las bases de datos locales que registran los precios de coste, número de operaciones llevadas a cabo e historial de precios propio, así como a fuentes de datos públicas de precios del Ministerio y, eventualmente, otros sensores que pueda tener desplegados la estación de servicio (por ejemplo, contadores de vehículos en la vía pública). Con esta información, este módulo suministrará estimaciones de rentabilidad que serán el soporte para que el operario determine el precio a fijar.
  
De cara al desarrollo de este módulo, la empresa no sabía cuál es el modelo de inteligencia artificial que debería ser la base para su construcción. En este sentido, ya se cuenta con experiencia en el desarrollo de otros módulos de IA que están siendo incluidos en sus productos. Sin embargo, la complejidad de los mismos es mucho más baja dado el número de datos con los que deben operar, la precisión que deben suministrar, y los tiempos de respuesta necesarios (en el caso que ocupa a este proyecto, el módulo puede llevar a tener que ejecutar reentrenamientos y actualizaciones en ciclos inferiores a los 15 minutos).
  
El objetivo de este proyecto ha sido establecer cuál es el mejor modelo de inteligencia artificial que debe ser seguido por la empresa de cara a poder desarrollar el mencionado módulo de ayuda a la fijación de precio. Para ello, el equipo de la Universidad de Zaragoza ha llevado a cabo todo un conjunto de experimentos con datos históricos de precios. Estos experimentos han analizado un conjunto de aproximaciones tecnológicas de IA operando con datos históricos con los que cuenta la empresa. Estos datos comprenden valores propios de precios de diferentes combustibles, así como los precios de combustibles publicados por el Ministerio para la Transición Ecológica, y datos históricos de cotizaciones del petróleo.
  
Los resultados del trabajo a llevar a cabo se sustentan en dos entregables:
  
●	Un informe en el que se recoge todas las experimentaciones llevadas a cabo durante el proyecto, así como las conclusiones extraídas del análisis de las mismas.
  
●	El código fuente de todas las mencionadas experimentaciones. Este código fuente permitirá a la empresa repetir los experimentos que se han llevado a cabo, así como servir de base para el diseño de nuevos que puedan ser considerados necesarios.
  
Desarrollado para: [ADVANCE SOLUCIONES DE NEGOCIO, s.l. ](https://www.advancesoluciones.com/)
 
   
