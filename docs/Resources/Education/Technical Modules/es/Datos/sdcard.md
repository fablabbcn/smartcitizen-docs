---
title: SD-card
tags:
  - data
  - education
  - basic level
---

### SD-card

Siempre que haya una SD-card presente, el SCK grabará los datos en la misma en formato CSV.

Es posible que veas algunos archivos raros en la SD-card, con extensiones como `(.01, .02...)`. Estos ficheros son en realidad ficheros CSV, pero que el kit necesita renombrar cada vez que ocurre un `reset` para evitar corromper la SDcard. 

!!! info "Reset"
    
    Cada vez que ocurre un reset, bien manual (con el botón o desconectando la alimentación), o bien periódico, un fichero nuevo se genera.

    Cada noche, ocurre un reset _de sanidad_ para asegurar que todo funciona correctamente y que el SCK no se bloquea. Este reset ocurre a las 3-4am (en CET), para evitar que perdamos datos si hay algún problema con el kit. Los ficheros en la SD card se generan secuencialmente como YY-MM-DD.01, .02… dependiendo del número de _reset_ que ocurren en un día. Puedes simplemente renombrar los ficheros de YY-MM-DD.01 a YY-MM-DD_01.CSV. [También puedes revisar esta guía](/Guides/data/Organise your data/#pre-process-the-sd-card-data) para automatizar este proceso.
