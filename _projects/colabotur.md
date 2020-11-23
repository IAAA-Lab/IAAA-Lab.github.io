---
title: Infraestructura web para el modelado colaborativo sobre una malla geodésica de espacios geográficos con interés turístico
subtitle: Web infrastructure for the collaborative modeling on a discrete global grid of geographic spaces with tourist interest
acron: COLABOTUR
code: LMP19_18
keywords: Territorios Inteligentes, Infraestructuras de Información, Gobernanza Inteligente, Movilidad Inteligente, Cuadros de Mando
years: 2019-2020
layout: project_website_page
---

# Noticias / News

- **2020-11-23**: Presentation at the [GEOProcessing 2020 Conference](https://www.iaria.org/conferences2020/GEOProcessing20.html). The [paper is available](https://www.thinkmind.org/index.php?view=article&articleid=geoprocessing_2020_1_140_30091), and there is also a [video of the presentation](https://youtu.be/NJLLUI9oOG4).
- **2020-11-20**: [Modelo de procesos: conversión de datos sobre emociones a las mallas DGGS de distintas escalas](https://youtu.be/-CSIoGyw_s8). Tutorial disponible on-line.
- **2020-11-16**: [Conferencia titulada "Cartografía emocional, cartografía sensible"](https://youtu.be/N9UAcAJcOVI). Formación on-line con sistemas de información geográfica y cartografía temática para la gestión territorial y el cumplimiento de los Objetivos de Desarrollo Sostenible. Colaboración entre el Gobierno de Aragón y la Universidad de Zaragoza para proyectos de cooperación al desarrollo en ámbitos universitarios
- **2020-10-30**: Presentation of the prototype for capturing emotional data in the [JIIDE 2020 Conference](https://www.dgterritorio.gov.pt/jiide2020/Default.aspx). The presentation is [available](https://www.dgterritorio.gov.pt/jiide2020/pdfs/apresentacoes/JIIDE2020_Sessao_10_UMER_Muhammad.pdf).
- **2019-07-16**: We offer a [1-year (extendable) research contract]({{site.baseurl}}/2019/07/16/research-contract-colabotur/) within this project. Application deadline: **September 2, 2019**.

# Resumen

Este proyecto propone el desarrollo de una **infraestructura web** que permita avances científico-técnicos en el campo de las **aplicaciones colaborativas y la neogeografía**, dando soporte a la creación y mantenimiento de información geográfica en el ámbito del turismo, y con un fuerte énfasis en la posibilidad de compartir vivencias y experiencias personales y emocionales. El proyecto se demostrará sobre un prototipo de aplicación web turística para una comarca de Aragón.

La georreferenciación de las localizaciones geográficas en esta infraestructura se basará en una **malla geodésica**, sobre la que emprendedores y operadores turísticos, los habitantes de las zonas turísticas y los propios turistas podrán diseñar y compartir colaborativamente lugares de potencial interés turístico y vivencias asociadas a ellos. El software de infraestructura desarrollado se publicará como software libre.

La neogeografía ha propiciado una mayor colaboración entre expertos y el público general a la hora de crear y mantener actualizados distintos tipos de datos geográficos. Esta colaboración debe permitirnos profundizar cada vez más en el conocimiento del espacio físico, espacio que hoy en día hay que considerar bajo nuevas dimensiones ligadas a la revolución tecnológica y digital, a lo que hemos denominado genéricamente como espacio **flexidimensional**, que además requiere de nuevas soluciones de cartografía temática para poder explorarse adecuadamente, algo que también se abordará en el proyecto.

El sistema aborda especialmente los aspectos de creación, edición y propiedad compartida de datos geográficos, incluyendo aquellos que la cartografía clásica no suele considerar, como las valoraciones emocionales (un espacio tranquilo donde disfrutar de un café), áreas difusas y temporales (la zona de tu barrio donde has organizado una “búsqueda del tesoro” con tus amigos), lugares semiprivados (mi rincón favorito del parque), o áreas de límites difusos y opinables (una “zona de tapas”). La necesidad de definir y compartir este tipo de datos geográficos surge de manera natural en el contexto de las experiencias turísticas, donde cada vez se valora más disfrutar, descubrir y compartir experiencias y vivencias más personales, algo que refleja por ejemplo el auge de portales como TripAdvisor.

La infraestructura web requiere crear las localizaciones geográficas sobre conjuntos de celdas seleccionados de una malla geodésica (localizadas e identificadas de manera única, y con soporte para resoluciones múltiples), y cada una de estas localizaciones tiene por construcción una URL (dirección web) única, que es un requisito esencial para su integración en la Web. No hay distintos tipos de geometrías (puntos, líneas, polígonos u otras), ni problemas de integración derivados de partir de información georreferenciada en base a distintos sistemas de coordenadas, datums o elipsoides. Tampoco hay que definir clases de Features o Spatial Things y asignar identificadores únicos a sus instancias a posteriori, ni se requiere que exista, o que haya que crear, un topónimo al que asociar la información.

# Summary

This project proposes the development of a **web infrastructure** that will allow scientific-technical advances in the field of **collaborative applications and neogeography**, supporting the creation and maintenance of geographic information related to tourism, and with a strong emphasis on the possibility of sharing personal and emotional experiences. The project will be demonstrated on a prototype tourist web application for a *comarca* (an administrative area) of Aragon.

The georeferencing of locations in this infrastructure will be based on a **geodesic grid**, on which entrepreneurs and tour operators, the inhabitants of tourist destinations and tourists themselves will be able to design and share collaboratively places of potential tourist interest and some experiences associated with them. The software infrastructure developed will be published as free/open software.

Neogeography has led to a greater collaboration between experts and the general public in creating and keeping different types of geographical data up to date. This collaboration should allow us to go deeper and deeper into the knowledge of the physical space, space that today must be considered under new dimensions linked to the technological and digital revolution, what we have generically called as **flexidimensional** space, which also requires new thematic cartography solutions to be properly explored, something that will also be addressed in the project.

The system addresses especially the aspects of creation, edition and shared ownership of geographic data, including those that classic cartography does not usually consider, such as emotional valuations (a quiet space where to enjoy a coffee), diffuse and temporal areas (the area of your neighborhood where you have organized a "treasure hunt" with your friends), semi-private places (my favorite corner of the park), or areas of diffuse and debatable boundaries (a "*tapas* area"). The need to define and share this type of geographic data arises naturally in the context of tourist experiences, where it is increasingly valued to enjoy, discover and share more personal experiences, something that is shown for example on the rise of portals such as TripAdvisor.

The web infrastructure requires the creation of geographic locations on sets of cells selected from a geodesic grid (located and uniquely identified, and with support for multiple resolutions), and each of these locations has, by construction, a unique URL (web address), which is an essential requirement for its integration into the Web. There are no different types of geometries (points, lines, polygons or others), nor integration problems derived from georeferenced information based on different coordinate systems, datums or ellipsoids. There is also no need to define Features or Spatial Things classes and assign unique identifiers to their instances *a posteriori*, nor it is required that there exists, or that there is a need to create, a toponym to associate the information with.


## Financiación
Este proyecto, con referencia {{ page.code }}, está financiado durante {{ page.years }} por fondos FEDER Aragón 2014-2020, "Construyendo Europa desde Aragón".

<img src='{{site.baseurl}}/images/other-logos/european_union_official_flag_yellow_600x401.jpg' width='300' style="margin-bottom: 40px;">
