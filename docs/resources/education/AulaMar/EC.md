# Conductividad

## ¿Qué es la conductividad del agua?

La conductividad del agua es la capacidad que tiene esta para permitir el flujo de cargas eléctricas. Para que haya conductividad, el agua necesita tener iones disueltos (cargas eléctricas positivas o negativas).

!!! info inline end "¿El agua conduce o no conduce?"

	Un agua libre de iones (desionizada) o pura (destilada), no es conductora - **¡de hecho es un aislante muy bueno!** El agua pura, al no tener iones (simplemente es H2O, sin cargas eléctricas), no puede ser conductiva, pero al añadir sustancias minerales o componentes orgánicos, se añaden en forma de iones disueltos, que permiten que el agua conduzca la electricidad.

Existen varias formas de expresar la conductividad: conductancia específica, conductancia eléctrica específica, o conductividad eléctrica. El término _conductividad eléctrica_ es directamente relacionada a la temperatura  del agua, por lo que **es importante medir la temperatura a la que se hizo esta medición de conductividad**. En el caso más general, la conductividad se debe expresar como conductancia específica, es decir, corrigiendo la conductividad a una temperatura de 25ºC, respecto a la temperatura a la que se hizo la medición.

La conductancia es, por tanto, la capacidad del agua de conducir la corriente eléctrica (se mide en Siemens [S]) y es el inverso de la resistencia (que se mide en Ohm [Ω]). La conductividad eléctrica, tal como la mediremos con nuestro sensor, es la medida de conductancia, normalizada a una unidad de distancia y sección transversal.

## ¿Por qué es importante?

La conductividad, con la temperatura, es utilizada para calcular la salinidad, y otros parámetros como los sólidos disueltos (TDS). La salinidad es la cantidad de sales contenida en 1 kg de agua. Se expresa en PSU (Unidad Práctica de Salinidad, que equivale aproximadamente a 1mg/g de sales). La salinidad promedia del agua de mar es de 35 psu, o 35 g/kg.

!!! seawater "En el mar"

	En oceanografía, la conductividad se usa como medida para obtener la estimación de la salinidad del agua de mar (en este caso, corresponde a la _salinidad práctica_). Por otra parte,   la salinidad absoluta corresponde a la concentración de sales contenidas en el agua, y para medirse necesita métodos químicos complejos y que toman mucho tiempo. 

	La salinidad es un factor ecológico de **gran importancia**, y tiene influencia sobre el tipo de organismos (animales y plantas) que pueden vivir en el agua. Las variaciones de salinidad del agua están directamente relacionadas con los aportes de agua dulce de los ríos o de los eventos de lluvias, pero también de la evaporación de las aguas superficiales o de la formación del hielo marino en los océanos. También tiene un impacto sobre la formación de aguas profundas en los polos. Finalmente, acompañada de una medida de temperatura, permite definir la densidad de las masas de agua y con esto obtener información sobre las corrientes.

	Estos cambios de densidad debidos a la temperatura y la salinidad provocan cambios en la flotabilidad de las masas de agua. Además, las variaciones de salinidad pueden tener impacto en la absorción del CO2 en los océanos (en aguas más saladas, el CO2 es menos soluble). Por último, los datos de temperatura, salinidad y densidad son como la tarjeta de identidad de las diferentes masas de aguas contenida en los océanos y nos permite seguir su recorrido a lo largo de su vida (zona de formación hasta desaparecer o transformarse en otra masa por procesos de difusión o mezcla).

!!! tip inline end "Curiosidades"

	La capacidad de carga máxima de los buques mercantes varía en función de la zona de navegación y de la época del año. En función de la densidad del agua que se van a encontrar se pueden cargar más o menos para "flotar lo mismo". El disco de Plimsoll es este dibujo que llevan los buques mercantes en los lados, cerca de la línea de flotación. Sirve para ver hasta dónde cargar en barco en función de la ruta

	![alt_text](/assets/images/education/es/plimsoll.png "Plimsoll")

	**El Mediterráneo**

	La salinidad media del mediterráneo es alrededor de 38 psu, lo cual lo hace un mar más salado que la media mundial.

## ¿Cómo medir la conductividad?

Como norma general, es preferible la toma de medidas in situ, en lugar de la toma de muestras y posterior análisis en laboratorio, debido a los posibles cambios químicos que pueden ocurrir en la muestra.

En caso de que no se pueda hacer una medida in situ, trata de tomar una muestra y hacer la medida lo antes posible. Si la muestra cambia mucho de temperatura, o si se forman deposiciones o burbujas en el transporte, la medida no será representativa.

### El sensor

Para medir conductividad eléctrica, usaremos un sensor llamado **conductímetro**. En el caso de Smart Citizen, usando los sensores de Atlas Scientific, el sensor de conductividad no tiene sensor de temperatura integrado, por lo que deberemos usar un sensor de temperatura adicional para medir la temperatura a la cual estamos tomando la muestra. **Este sensor de temperatura debe sumergirse a la vez cuando tomemos medidas de conductividad**.

En caso de tener un sensor de temperatura, los valores reportados serán referenciados a la temperatura medida, siendo este proceso automático. En caso de no tener un sensor de temperatura, la lectura será referenciada a 25ºC, y puede representar un origen de errores. Adicionalmente, es importante revisar las correcciones con valores de pH extremos (mayores a 12 o menores a 2), ya que éstas pueden introducir errores grandes en los resultados en los sensores de Smart Citizen (y Atlas Scientific).

#### Cómo preparar el sensor

**Antes y después** de medir, se debe limpiar con agua desionizada. En caso de que haya restos, se puede limpiar con tejidos de laboratorio para evitar polvo. Se puede limpiar con un poco de detergente y posteriormente limpiar con agua destilada en caso de que esté muy sucia, o contenga residuos oleosos. 

!!! info "**Calibración**"

	Si el sensor no está calibrado, sigue el procedimiento descrito en [esta guía](https://docs.smartcitizen.me/Guides/calibration/Water%20sensors/#atlas-ec)

#### Cómo medir

Si no conoces el lugar donde vas a tomar la muestra, mide en varios puntos a diferentes profundidades y secciones. En caso de que haya poco movimiento de agua, toma varias muestras a diferentes profundidades.

1. Toma la medida a la profundidad que toque dejando que se estabilice al menos 60s. Para saber si está en equilibrio, espera variaciones de ±5 μS/cm para medidas ≤100 μS/cm o ±3% para medidas >100 μS/cm. No sumerjas la sonda demasiado de forma que nunca entres en zona de sedimentos.
2. Toma medidas de temperatura y conductividad, sin mover las sondas del agua (toma las dos a la vez)
3. Cuando termines, limpia la sonda con agua desionizada

!!! warning
	El sensor de conductividad necesita sumergirse hasta el elemento activo:

	![alt_text](/assets/images/education/es/atlas_cond.png "Hasta aquí!")	

	Además, evita que se acumulen burbujas en la carcasa del sensor. Simplemente agita el sensor un poco para extraer las burbujas:

	![alt_text](/assets/images/education/es/atlas_burbujas.png "Hasta aquí!")


!!! tip "Recursos adicionales"
	Sobre importancia de la salinidad para la oceanografía física, así como su aplicación a la identificación de frentes entre diferentes masas de agua:

	https://www.youtube.com/watch?v=-B5PDNmSidY 
	https://www.youtube.com/watch?v=AsLJLt70Zo4 
	https://www.youtube.com/watch?v=oxAwn8nunGo

	En caso de que quieras profundizar más en las medidas de conductividad, puedes revisar las referencias en [https://pubs.usgs.gov/tm/09/a6.3/tm9-a6_3.pdf](https://pubs.usgs.gov/tm/09/a6.3/tm9-a6_3.pdf) 