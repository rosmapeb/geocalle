---
layout: page
title: Cómo contribuir
permalink: /como_contribuir/
---


# Cómo contribuir

GeoCalle es un repositorio web que se apoya fundamentalmente de dos
tecnologías: 1. [OpenLayers](https://openlayers.org) y 2. [Git](https://git-scm.com).

OpenLayers es una biblioteca que permite el despliegue de mapas e
información geográfica a través de la web. Es capaz de admitir datos
en el formato estándar [GeoJSON](http://geojson.org/) que, además de ser compatible con otras
herramientas SIG, es fácilmente manejable por el sistema de control de
versiones Git.

Git es un protocolo y una colección de programas que permiten la
edición colaborativa de repositorios a través control de cambios a
archivos. Para el repositorio GeoCalle nos apoyamos también de [GitHub](https://github.com),
un servicio de hospedaje especializado en brindar repositorios Git.
GitHub nos brinda la [infraestructura para la publicación](https://pages.github.com/) de páginas
web y mapas interactivos, además implementa un flujo de trabajo que
permite a cualquiera colaborar fácilmente en la creación y edición de
contenidos.

El diseño en torno a estas dos herramientas busca minimizar los
requerimientos de infraestructura necesarios para operar el
repositorio, sin limitar sus capacidades.


# Fork, pull-request

El flujo de trabajo para contribuir datos o cualquier contenido a este
repositorio es el denominado "Fork y Pull-Request". Consiste de que un
colaborador potencial "bifurca" (fork) este repositorio, o sea: hace
un clon en su propio perfil, donde es libre de agregar datos o hacer
cambios. Cuando su aportación está lista, nos envía un "pull-request",
o sea, una solicitud de que fusionemos su repositorio con el nuestro,
incorporando así sus aportaciones. Como parte de esta fusión hay
mecanismos que nos permiten discutir -de ser necesario- posibles
adecuaciones o aclaraciones, lo cuál hace transparente toda la gestión
de los contenidos. Al final, a través de Git, se fusionan las
aportaciones al repositorio central, reteniendo información de autoría
y permitiendo la trazabilidad de todo el esfuerzo.

<img src="../gitflow.png" width="60%">

Existe una enorme oferta de guías acerca del uso de Git y para el
flujo de trabajo "Fork, pull-request" de GitHub. Algunas
recomendaciones:

 - [Pro Git](https://git-scm.com/book/es/v1). Libro en español
   dedicado al protocolo Git
 - [Git - la guía sencilla](http://rogerdudler.github.io/git-guide/index.es.html). Una
   guía sencilla para comenzar con Git sin complicaciones
 - [Fork de repositorios en GitHub](http://aprendegit.com/fork-de-repositorios-para-que-sirve/). Guía
   de Fork, pull-request en español.
 - [Understanding the GitHub Flow](https://guides.github.com/introduction/flow/). Guía
   oficial de GitHub.

Este es el flujo de trabajo que preferimos, sin embargo Git puede ser
[un reto sustancial](https://xkcd.com/1597/) y estamos dispuestos a
ayudar o a admitir aportaciones por otras vías, si contacta a los
autores.


# GeoJSON

GeoJSON es un formato estándar abierto diseñado para representar
elementos geográficos sencillos, junto con atributos no
espaciales. Está basado en el formato JSON (JavaScript Object
Notation), por lo que es bastante legible por humanos (a diferencia de
-por ejemplo- formatos binarios o basados en XML), y tiene una
amplia adopción.

Por tratarse de un formato basado en texto plano es posible para Git
mantener control de cambios. Esta simplicidad nos permite publicar
datos sin necesidad de infraestructura más sofisticada como
GeoServer. 

El formato de GeoJSON en uso por este repositorio para su adecuado
funcionamiento con nuestra configuración de OpenLayeres precisa de
