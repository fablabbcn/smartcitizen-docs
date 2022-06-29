# Temperatura

![](/assets/images/education/t_header.gif)

## ¿Qué es la temperatura del agua?

A nivel conceptual, la temperatura del agua puede ser algo muy simple: es un valor que indica cómo de caliente o frío se encuentra un cuerpo, objeto o, en este caso, líquido. Sin embargo, el agua, sobre todo en masas grandes, puede presentar enormes variaciones entre distintas partes: en la superficie vs. en profundidad, o en la orilla vs. aguas adentro.

## ¿Por qué es importante?

La temperatura es un factor muy importante, porque condiciona todos los otros factores del agua. Además, es un factor ecológico de importancia considerable, y tiene influencia sobre los tipos de organismos que pueden vivir en el agua: normalmente, a mayor temperatura, mayor actividad biológica. Tiene un impacto directo en oxígeno disuelto (inverso - a mayor temperatura, menor oxígeno disuelto a igualdad de condiciones), además de condicionar la velocidad a la que ocurren las reacciones químicas en el agua. Tiene impacto en disolución de sales y metales y por ello tiene impacto en la conductividad eléctrica.

!!! seawater "En el mar"
	
	Está relacionado con la de la salinidad de las corrientes en el océano, y en general, los cambios de temperatura en los océanos son debidos a los intercambios con la atmósfera.

## ¿Cómo medir temperatura?

Siempre que sea posible, toma lecturas usando la sonda de temperatura in situ, sumergiéndola directamente en el agua. Intenta no afectar las medidas, cogiendo el termómetro lo más separado posible de la parte metálica para evitar calentarlo. Si el termómetro necesita tiempo para estabilizarse, toma varias medidas y anótalas, junto con la hora, o toma la última medida (y sólo esa) cómo válida.

Si no es posible introducir el sensor en el agua, y necesitas tomar una muestra, estabiliza el recipiente para el muestreo antes de medir (sumergiéndolo en agua para que se caliente/enfríe a la misma temperatura que la del agua).

!!! danger "OJO!"
	Revisa las especificaciones del sensor en el apartado inferior, porque tiene un tiempo de estabilización “largo”, de aproximadamente 13s.

### El sensor

Para medir temperatura, usaremos un sensor resistivo (RTD, _resistance temperature detector_) del tipo PT1000 (hecho de platino, y con una resistencia a 0ºC de 1000Ω). Este sensor está encapsulado dentro de una punta de acero inoxidable, para conducir el calor muy eficientemente. Para poder usarlo a temperaturas más extremas, o fijarlo en una tubería, usaremos un _thermowell_:

![alt_text](/assets/images/education/es/atlas_thermo.png "Thermowell")

El sensor se puede sumergir completamente, y tiene las **siguientes características** (aquí citamos algunas, tienes todas en el datasheet):

* Rango: -200 a 850ºC (sin thermowell -55°C a 125°C)
* Precisión: +/- (0.15 + (0.002\*t))
* Máxima profundidad en agua: 70m
* Velocidad de respuesta: 90% in 13s

Este tipo de sensor no necesita de mantenimiento ni recalibración, únicamente limpieza periódica para retirar incrustaciones. Con usar un cepillo normal es suficiente.

!!! warning "Antes de hacer nada, revisa este datasheet (hoja de datos):"

	[https://files.atlas-scientific.com/PT-1000-probe.pdf](https://files.atlas-scientific.com/PT-1000-probe.pdf) 
