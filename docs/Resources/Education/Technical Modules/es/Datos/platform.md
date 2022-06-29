---
title: Plataforma
tags:
  - data
  - education
  - intermediate level
---

### Plataforma

[![](https://i.imgur.com/mo5RzkR.jpg)](https://smartcitizen.me/kits/)

La plataforma web de Smart Citizen permite realizar las siguientes funciones:

- Navegación geolocalizada y visualización de datos por dispositivo
- Gestión del perfil de usuario y edición de kits
- [Subida de datos de SCKs sin conectividad con SD card](/Guides/getting started/Uploading SD Card Data/)
- [Descarga de datos en CSV](/Guides/getting started/Downloading the Data/#download-data)

### API

El <a href="http://developer.smartcitizen.me/" target="_blank">API de Smart Citizen</a> te permite descargar información de tus dispositivos y hacer cosas chulas con ellos.

Es un API <a href="https://en.wikipedia.org/wiki/Representational_state_transfer" target="_blank">REST</a> y te retorna los datos en formato <a href="https://en.wikipedia.org/wiki/Json" target="_blank">JSON</a>. Esto quiere decir que puedes acceder de forma fácil la información desde cualquier lenguaje de programación Javascript, PHP, [processing](https://processing.org), Python, ... y empezar a hacer cosas muy rápidamente.

### Usando _scripts_

Si quieres avanzar más rápido, hemos preparado una serie de ejemplos y librerías en python en [scdata](https://pypi.org/project/scdata/). _scdata_ es un paquete de `python` que te permite descargar, visualizar y analizar datos de forma rápida. Revisa los [ejemplos](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples) en el repositorio de git.

!!! tip "Ejemplos extras"
    Hay otros muchos ejemplos en otros lenguajes de programación en el repositorio de [smartcitizen-toolkit](https://github.com/fablabbcn/smartcitizen-toolkit). En él encontrarás cómo acceder a los datos desde [processing](https://processing.org), o [nodered](https://nodered.org/).