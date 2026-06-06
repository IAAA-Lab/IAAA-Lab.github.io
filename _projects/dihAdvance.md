---
title: Experimentación destinada a la validación de tecnologías de base para el desarrollo de un componente software para la fijación de precio óptimo de combustibles para vehículos (2023/DIH_01/000414)
acron: IAAA-ADVANCE
code: 
keywords: Inteligencia Artificial, Precio combustibles
years: 2024
layout: project_website_page
---


El incremento del precio de los carburantes en los últimos años ha llevado a que consumidores/as estudien con más detalle el precio que se ofrece por las estaciones de servicio para decidir en cuál se compra. Así mismo, la obligación de notificar al Ministerio para la Transición Ecológica las modificaciones de los precios de venta casi en tiempo real, y la correspondiente exposición pública de estos precios por parte de esta entidad, lleva a que profesionales y ciudadanía en general cuenten con cada vez más información para tomar sus decisiones de compra de carburantes.
  
Por otro lado, los puntos de venta tratan de aprovechar al máximo también esta información, junto con otros datos que pueden recopilar, para llevar a cabo una gestión de precios de venta que permita maximizar la rentabilidad de las operaciones de repostaje sobre la base del estudio de la competencia y de las dinámicas de la clientela. De este modo, en algunos casos, se realizan actualizaciones de precio cada hora.
  
En este contexto, la empresa se ha embarcado en el desarrollo de un módulo que permita incluir en su ERP de gestión de estaciones de servicio funcionalidades de ayuda a la fijación de precio cada hora de los diferentes combustibles basadas en técnicas de inteligencia artificial. En cada implantación del ERP, este módulo se conectará a las bases de datos locales que registran los precios de coste, número de operaciones llevadas a cabo e historial de precios propio, así como a fuentes de datos públicas de precios del Ministerio y, eventualmente, otros sensores que pueda tener desplegados la estación de servicio (por ejemplo, contadores de vehículos en la vía pública). Con esta información, este módulo suministrará estimaciones de rentabilidad que serán el soporte para que el operario determine el precio a fijar.
  
De cara al desarrollo de este módulo, la empresa no sabía cuál es el modelo de inteligencia artificial que debería ser la base para su construcción. En este sentido, ya se cuenta con experiencia en el desarrollo de otros módulos de IA que están siendo incluidos en sus productos. Sin embargo, la complejidad de los mismos es mucho más baja dado el número de datos con los que deben operar, la precisión que deben suministrar, y los tiempos de respuesta necesarios (en el caso que ocupa a este proyecto, el módulo puede llevar a tener que ejecutar reentrenamientos y actualizaciones en ciclos inferiores a los 15 minutos).
  
El objetivo de este proyecto ha sido establecer cuál es el mejor modelo de inteligencia artificial que debe ser seguido por la empresa de cara a poder desarrollar el mencionado módulo de ayuda a la fijación de precio. Para ello, el equipo de la Universidad de Zaragoza ha llevado a cabo todo un conjunto de experimentos con datos históricos de precios. Estos experimentos han analizado un conjunto de aproximaciones tecnológicas de IA operando con datos históricos con los que cuenta la empresa. Estos datos comprenden valores propios de precios de diferentes combustibles, así como los precios de combustibles publicados por el Ministerio para la Transición Ecológica, y datos históricos de cotizaciones del petróleo.
  
Los resultados del trabajo a llevar a cabo se sustentan en dos entregables:
  
●	Un informe en el que se recoge todas las experimentaciones llevadas a cabo durante el proyecto, así como las conclusiones extraídas del análisis de las mismas.
  
●	El código fuente de todas las mencionadas experimentaciones. Este código fuente permitirá a la empresa repetir los experimentos que se han llevado a cabo, así como servir de base para el diseño de nuevos que puedan ser considerados necesarios.
  
Desarrollado para: [ADVANCE SOLUCIONES DE NEGOCIO, s.l. ](https://www.advancesoluciones.com/)


Este proyecto ha sido subvencionado por el PROGRAMA DE APOYO A DIGITAL INNOVATION HUBS (DIH_01) dentro del ARAGON EDIH/ARAGON EUROPEAN DIGITAL INNOVATION HUB (Ministerio de Industria, Comercio y Turismo y European Union - Next Generation)


<img src='{{site.baseurl}}/images/other-logos/logoDIH-EOI.png' width='800' style="margin-bottom: 40px;">
   
