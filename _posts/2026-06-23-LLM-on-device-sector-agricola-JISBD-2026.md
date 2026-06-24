---
title: "LLM on-device en el sector agrícola: viabilidad y retos de ingeniería"
subtitle: Trabajo en curso presentado en las XXX Jornadas de Ingeniería del Software y Bases de Datos
layout: post
image: /images/posts/2026-06-23-LLM-agro-caso-uso.png
categories: [Paper overview]
---

Los modelos de lenguaje grandes (*Large Language Models*, LLM) permiten interactuar con sistemas digitales mediante lenguaje natural. Sin embargo, la mayoría de las soluciones actuales dependen de infraestructuras en la nube, algo que puede resultar problemático durante el trabajo agrícola en zonas con conectividad limitada.

Nuestro trabajo en curso, **«LLM on-device en el sector agrícola: hacia el estudio de viabilidad y retos de ingeniería»**, aborda este problema a partir de un caso de uso concreto: ayudar a los profesionales agrícolas a cumplimentar el **cuaderno de explotación** y a registrar toda su actividad. El trabajo fue presentado en las [XXX Jornadas de Ingeniería del Software y Bases de Datos (JISBD 2026)](https://www.sistedes.es/jornadas/jisbd), celebradas en Alicante del 16 al 18 de junio de 2026.

El [Cuaderno Digital de Explotación Agrícola (CUE)](https://www.aragon.es/pac-2026/cuaderno-digital-cue) registra la actividad de la explotación y permite justificar el cumplimiento de los requisitos necesarios para recibir ayudas de la Política Agraria Común (PAC). Su cumplimentación puede resultar una tarea tediosa para los agricultores, especialmente cuando debe realizarse durante o después de las labores de campo. Una de las motivaciones del trabajo es aliviar esta carga mediante un asistente que utilice la voz como principal mecanismo de entrada: el profesional describiría oralmente una labor y el sistema la trasladaría al registro correspondiente. Además, podría consultar normativa y documentación técnica para completar los datos y generar avisos, por ejemplo, ante el uso de un producto no permitido.

![Caso de uso de un asistente LLM para cumplimentar documentación agrícola en campo]({{ site.baseurl }}/images/posts/2026-06-23-LLM-agro-caso-uso.png){: .center-image width="100%"}
<h4 style="margin-bottom: 2em;"><center><b>Arquitectura conceptual del sistema propuesto</b></center></h4>

El objetivo principal es lograr que el modelo funcione *on-device*, manteniendo el procesamiento en el propio teléfono o tableta. Así se reduciría la dependencia de la conectividad y se evitaría enviar los datos sensibles de la explotación a servicios externos. El reto no consiste únicamente en ejecutar el modelo localmente, sino en mantener la calidad necesaria para elaborar correctamente el cuaderno pese a las limitaciones de memoria, cómputo, energía y contexto.

Para conseguirlo se probarán técnicas como la cuantización, la poda, la destilación y PEFT (*Parameter-Efficient Fine-Tuning*). Estos experimentos permitirán conocer mejor los límites de los LLM en dispositivos móviles y las estrategias más adecuadas para superarlos. Si la calidad obtenida *on-device* no fuera suficiente, se estudiará la viabilidad de un despliegue *on-edge*, que mantenga el procesamiento próximo al origen de los datos y aporte más recursos.

La viabilidad del sistema se organiza alrededor de tres retos de ingeniería. El primero es la **adecuación funcional**: determinar qué degradación de calidad puede aceptarse sin comprometer la corrección del cuaderno. El segundo es una **evaluación realista** que no se limite a métricas aisladas del modelo, sino que considere el sistema completo, incluyendo la entrada por voz, el ruido ambiental y una conectividad limitada. El tercero es establecer criterios para tomar las **decisiones arquitectónicas** a partir de los resultados obtenidos.

![Principales problemas abiertos y retos de ingeniería de los LLM on-device]({{ site.baseurl }}/images/posts/2026-06-23-LLM-agro-retos-ingenieria.png){: .center-image width="100%"}
<h4 style="margin-bottom: 2em;"><center><b>Dimensiones de viabilidad del sistema</b></center></h4>

El trabajo se encuentra en una fase inicial. Por una parte, se está realizando un mapeo sistemático de la literatura sobre LLM *on-device* y *on-edge* para identificar soluciones existentes, tendencias y vacíos de investigación. Por otra, estamos trabajando con aplicaciones agrícolas que ya se utilizan en producción y desarrollando cuestionarios para sus usuarios. Esta recopilación de requisitos permitirá adaptar el asistente a sus necesidades, tareas y condiciones reales de trabajo.

![Metodología y fases previstas del trabajo]({{ site.baseurl }}/images/posts/2026-06-23-LLM-agro-metodologia.png){: .center-image width="100%"}
<h4 style="margin-bottom: 2em;"><center><b>Fases del trabajo: mapeo sistemático, requisitos, prototipo y evaluación</b></center></h4>

Los requisitos obtenidos guiarán el desarrollo de un prototipo con modelos ligeros y técnicas de optimización. La evaluación medirá la latencia, el consumo de energía, la memoria utilizada y la calidad de las respuestas. Posteriormente, el sistema completo se probará en condiciones cercanas al uso real, prestando especial atención a la entrada por voz, el ruido y la conectividad.

El artículo no presenta todavía una solución final, sino una agenda de investigación para construir un sistema **útil**, **evaluable** y **mantenible**. Los siguientes pasos serán definir los criterios de evaluación, desarrollar el prototipo y determinar empíricamente qué configuraciones permiten aliviar la cumplimentación del cuaderno desde los dispositivos utilizados en el campo.

---

[LLM on-device en el sector agrícola: hacia el estudio de viabilidad y retos de ingeniería.](https://biblioteca.sistedes.es/entities/art%C3%ADculo/9746f900-8758-4859-8098-37c6a3c220a4) F.J. GONZÁLEZ-ONTAÑÓN, S. MARTIN-SEGURA, M.E. SUAZA-MEDINA, M.Á. LATRE, F.J. ZARAZAGA-SORIA. Actas de las XXX Jornadas de Ingeniería del Software y Bases de Datos (JISBD 2026), SISTEDES, 2026.

---
