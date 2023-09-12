# Instrucciones

En esta página detallaremos los distintos aspectos que necesitas saber para usar el sensor.

## Introducción

El proyecto Smart Citizen tiene como objetivo proveer herramientas tecnológicas para el empoderamiento ciudadano entorno a la monitorización ambiental. Para ello, el proyecto se compone de varias categorías:

![](/assets/images/blocks.png)

En esta página, nos centraremos en explicar cómo funcionan los sensores y la plataforma.

{{ get_snippet_rel('docs/includes/modules/intro/Hardware.md') }}

{{ get_snippet_rel('docs/includes/modules/intro/Interface.md') }}

!!! info "Reset"

	En el caso de la estación de agua, puedes acceder a este botón desde fuera de la carcasa:

	![](/assets/images/reset_water.jpg)

### Sensores de agua

<img src="https://live.staticflickr.com/65535/51230999551_3941affaa5_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

Los sensores soportados para este sistema son:

{{ get_snippet_rel("docs/includes/supported sensors/water/es/index.md") }}

!!! info "En Aulamar"
	Para el caso de Aulamar hemos preparado mucho [material didáctico](/Resources/Education/AulaMar/#guias-por-metrica) para entender mejor las métricas que vamos a medir.

{{ get_snippet_rel('docs/includes/modules/calibration/water.md') }}

{{ get_snippet_rel('docs/includes/modules/intro/Onboarding.md') }}

## Datos

Existen diversar maneras de acceder a los datos capturados por los sensores:

- SD Card
- Visualización WEB y Dashboard
- API

{{ get_snippet_rel('docs/includes/modules/data/sdcard.md') }}

{{ get_snippet_rel('docs/includes/modules/data/platform.md') }}

{{ get_snippet_rel('docs/includes/modules/data/dashboard.md') }}
