---
variables:
  - [pH, pH, '#f05133', 'white']
  - [Oxígeno disuelto, OD, '#ffd200', 'black']
  - [Conductividad, EC, '#289045', 'white']
  - [Temperatura, T, '#58595b', 'white']
---

# AulaMar

<img src="https://live.staticflickr.com/65535/51230999551_3941affaa5_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

!!! danger "Lo primero es lo primero"
	¡**Muy importante**! Revisa [esta página](General) antes de hacer nada.

## Guías por métrica

Selecciona debajo guías y materiales para cada una de las métricas que medimos:

<div class="grid-two-columns">
	{%- for x in page.meta.variables %}
		<a href={{ x[1] }}>
			<div class="button-metric" style="background-color: {{ x[2] }}">
				<span style="font-size: 25px;font-weight: bolder; color: {{x[3]}}">{{ x[0] }}</span>
			</div>
		</a>
	{%- endfor %}
</div>

## Material para el docente

En la parte superior de cada página puedes descargar el contenido de esta web en PDF si lo prefieres. Debajo tienes materiales adicionales para las actividades:

- [Instrucciones de uso](Instrucciones)
- [Material Docente (secuencia didáctica)]()
- [Estadillo - Cuaderno de laboratorio]()

## Referencias y material adicional

!!! info "Gracias a..."
	Todo este material se ha hecho durante el proyecto AULAMAR (Fundació Bit Habitat, ref. ID253). Este material se ha elaborado junto con el Instituto de Ciencias del Mar (ICM - CSIC, Barcelona)

Estas son unas referencias que hemos utilizado como inspiración, motivación y referencia para generar este material, aparte de contenido propio:

*A Citizen’s Guide To Understanding And Monitoring Lakes And Streams*: [https://apps.ecology.wa.gov/publications/documents/94149.pdf](https://apps.ecology.wa.gov/publications/documents/94149.pdf)

*USGS National Field Manual for the Collection of Water-Quality Data*: [https://www.usgs.gov/mission-areas/water-resources/science/national-field-manual-collection-water-quality-data-nfm](https://www.usgs.gov/mission-areas/water-resources/science/national-field-manual-collection-water-quality-data-nfm)

*U.S. Geological Survey, 2019, Specific conductance: U.S. Geological Survey Techniques and Methods, book 9, chap. A6.3, 15 p.,* https://doi.org/10.3133/tm9A6.3.

*NOAA*: https://www.noaa.gov/education/resource-collections/ocean-coasts

*Atlas Scientific*: [https://atlas-scientific.com/](https://atlas-scientific.com/)
