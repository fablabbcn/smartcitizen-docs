---
internal:
  proofread: false
  links: false
  images: false
---

# Electrical Conductivity Measurements

## What is water conductivity?

The conductivity of water is the capacity it has to allow the flow of electric charges. For conductivity to occur, water needs to have dissolved ions (positive or negative electric charges).

!!! info inline end "Is water conductive, or not?"

    Ion-free (deionized) or pure (distilled) water is non-conductive; in fact, it is a very good insulator! Distilled water, having no ions (as it is pure H2O, without electrical charges), cannot be conductive. However, by adding mineral substances or organic components, which are added in the form of dissolved ions, the water becomes conductive.

There are several ways to express conductivity: specific conductance, specific electrical conductance, or electrical conductivity. The term _electrical conductivity_ is directly related to water temperature, so **it is important to measure the temperature at which this conductivity measurement is taken**. In the most general case, conductivity should be expressed as a specific conductance, in other words, by correcting the conductivity to a temperature of 25ºC, with respect to the temperature at which the measurement was taken.

Conductivity is therefore the water's ability to conduct electric current (measured in Siemens [S]) and is the inverse of resistance (measured in Ohm [Ω]). Electrical conductivity, as measured by our sensor, is the conductance measurement, normalized to a unit of distance and cross-section.

## Why is it important?

Conductivity, along with temperature, is used to calculate salinity and other parameters such as dissolved solids (TDS). Salinity is the amount of salt contained in 1 kg of water. It is expressed in PSU (Practical Salinity Unit, which is equivalent to approximately 1mg/g of salt). The average salinity of seawater is 35 psu, or 35 g/kg.

!!! seawater "In the sea"

    In oceanography, conductivity is used as a measurement to obtain the estimation of the salinity of seawater (in this case, it corresponds to _practical salinity_). On the other hand, absolute salinity corresponds to the concentration of salt contained in water, a measurement which requires complex and time-consuming chemical methods.

    Salinity is an ecological factor of **great importance**, and influences the type of organisms (animals and plants) that can live in water. Variations in water salinity are directly related to freshwater inputs from rivers and rainfall events, but they also relate to the evaporation of surface water and the formation of sea ice in the oceans. It also has an impact on deep water formation at the poles. Finally, accompanied by a temperature measurement, salinity measurements allow for the calculation of the density of these bodies of water, from which information about currents can be obtained.

    These density changes due to temperature and salinity cause changes in the buoyancy of bodies of water. In addition, salinity variations can have an impact on the absorption of CO2 in the oceans (in saltier waters, CO2 is less soluble). Finally, the data on temperature, salinity and density act like an identification card for the different masses of water contained in the oceans and allow us to follow their journey throughout their existence (from their zone formation through their disappearance or transformation into another mass through diffusion or mixing processes).

!!! tip "Interesting fact"

    The maximum load capacity of merchant ships varies depending on their area of navigation and the time of year. Depending on the density of the water they will encounter, they can be loaded more or less to "float the same". The Plimsoll line is a drawing often seen on the sides of merchant ships, near the waterline. It serves to show how full the boat can be safely loaded depending on its route:

    ![](/assets/images/water/plimsoll.png "Plimsoll")

    **The Mediterranean Sea**

    The average salinity of the Mediterranean Sea is around 38 psu, which makes it saltier than the world average.

## How is conductivity measured?

As a general rule, it is preferable to take measurements in situ, rather than taking samples and subsequently performing analysis in the laboratory, due to possible chemical changes that may occur in the sample.

If a measure cannot be made on-site, try to take a sample and perform the measurement as soon as possible. If the temperature of the sample changes significantly, or if sedimentation or bubbles form in transport, the measurement will not be representative.

## Supported sensors

{{ insert_cards(type="sensor", filter="target", value=["electrical conductivity"])}}
