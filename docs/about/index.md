---
card: true
type: unit
custom_color: black
name: About
feature_img: https://live.staticflickr.com/4482/37510067734_7c5ca097cc_h.jpg
excerpt: Learn more about the Smart Citizen Project, its funding, its origins and other likeminded projects.
---

# About

WIP - TODO

The Smart Citizen project works to provide tools for anyone willing to use technology in a critical way. By developing environmental sensing tools, branching out in various fields such as open hardware, software, data, social innovation and digital fabrication, our main contribution is the amount of resources that this documentation hopes to compile. The project was born in [Fab Lab Barcelona](https://fablabbcn.org) which, up until now, is the main maintainer of the project. However, the project is [released under **free** and **open source** licenses](#open-source), hoping that anyone can contribute to it, reuse it, adapt it and improve it in any way needed.

<!-- TODO - Link to licenses of the different components -->

!!! info "A note about funding"

    One important aspect to mention in the front page of our documentation is that we have received public funding in several ocasions, including the European Commission funds in H2020 and Horizon Projects. In the [funding page](/About/funding/) you can find a complete list of these projects, for which we are thankful and that we hope that we have been able to deliver results accordingly. For publicly funded projects, information on the project numbers is available through the links in the `ID` column.

![](https://live.staticflickr.com/4519/24368451748_172c258274_h.jpg)

## About Citizen Science

With the proliferation of portable technologies, such as smartphones and wearable technologies, low-cost sensors and increased technological skills among the population, the role of citizens in monitoring their environment has increasingly taken root. Citizens are becoming increasingly active in tackling environmental problems that directly affect them, thereby implementing many bottom-up initiatives around the globe. They are demonstrating that environmental issues in cities can be addressed collaboratively, considering the realities and needs of the communities affected and harnessing their creative capacity and contributions, thereby raising citizens' awareness of environmental issues and increasing the sense of citizenship. This involvement can take many shapes and forms and generally comes together under the umbrella of citizen science. The essence of citizen science is that citizens are involved in one or various stages of a scientific investigation, such as compiling research questions, conducting observations, analysing data and using the resulting knowledge [^2]. Researchers or scientific institutions can lead or mediate in citizen science projects or have no role, as in extreme citizen science [^3]. One of the critical missions of citizen science is to promote the production of citizen-generated data, defined as data that people produce to directly monitor, demand or boost change in issues that affect them [^4]. The SafeCast community collected and openly shared radiation data as a response to the lack of reliable information available during the nuclear disaster in Fukushima [^5] and the Plaça del Sol community in Barcelona, where citizens collected data to demonstrate that noise levels in the area were above WHO recommendations and local legislation [^6], are just two examples of how citizen science can promote citizen-generated data to produce tangible results and social as well as sustainable impacts.

Citizen science is often implemented by mapping the environment and, more concretely, air pollution by low-cost sensors. This type of sensor has gained significant attention in recent years due to its potential in a ubiquitous and granular sensor network that can be exploited for data collection at a low cost per unit. This popularity has been the subject of many studies in the academic field, with several case studies showcasing great potential in providing successful data collection, the key to building community and trust in the technological tools used by the citizens in these participatory processes.

## The Smart Citizen project

### The Device

The Smart Citizen Kit (SCK) is a key component of the larger Smart Citizen System, providing a modular architecture for environmental data collection. Built around a central Data Board, the SCK facilitates data logging and network connectivity. Users can upload data to the Smart Citizen platform via standard domestic WiFi or store it on an internal SD card for later manual upload.

Outfitted with the Urban Sensor Board, the standard kit measures various environmental variables such as air temperature, humidity, and particulate matter (primarily PM2.5 and PM10). Custom sensor configurations are available for specialized applications in air and water monitoring.

The device accommodates various 3D-printed enclosures, ranging from simple indoor setups to rugged outdoor solutions. Most designs are compatible with locally accessible 3D printers, negating the need for long-distance shipping.

![](https://i.imgur.com/CbXDdY8.png)

### Installation

Matching environmental factors to be measured with the specific deployment requirements—such as power and internet connectivity—as well as strategically selecting host locations like citizens' homes, public buildings, or schools, is crucial for successful and robust data collection.

Installing the Smart Citizen Kit on domestic balconies is recommended for standard deployments. This location offers several advantages: it allows for easy power supply via an extension cord from the residence, facilitates a stable WiFi connection through the household's existing router, and elevates the device to a height that offers some protection against vandalism. Balconies provide an optimal environment for data accuracy while ensuring both convenience and security.

The SCK arrives pre-assembled, requiring only a brief setup guided online. Users must register on the Smart Citizen Platform to specify device location and name. A small rechargeable battery powers the kit and offers a 2-5 day battery and backup over short power disruptions. The device can be connected to a standard socket for medium to long deployment using an external USB adapter. Custom power solutions are also available for non-standard implementations.

Designed for resilience, the SCK features internal memory for data buffering and a user interface with status-indicating LEDs and functional buttons. Devices are easily resettable, enabling multiple community deployments with the same hardware.

![](https://i.imgur.com/MPXlpiB.jpg)

### Data Exploration and Archiving

Data uploaded to the Smart Citizen Platform is publicly accessible and easily navigable. Comparative and historical analyses can be performed on device data, downloadable in CSV format for common spreadsheet applications.

A suite of Python, R, and Orange tools is available for advanced analytics. Furthermore, a custom open API offers communities and corporations the flexibility to create bespoke visualization tools or integrate the SCK into existing workflows.

![](https://i.imgur.com/taC62WH.jpg)

## Hypothesis driven deployment

![](https://i.imgur.com/SDMJe2h.png)

The starting point of any citizen data collection intervention is to select a significant issue for people. Galvanising people around a problem helps create a sense of purpose with the intervention and is a cornerstone that sustains lasting participation. The first phase involves identifying issues of interest related to the environment that affects citizens. That is done by reviewing news items from the press, social networks, blogs and scientific articles and involving local communities in collaboratively mapping issues and resources in their areas. The primary outcome of phase one is the identification of shared concerns of citizens who are, therefore, willing to give their time and energy to collect evidence.

The second phase focuses on jointly defining the data collection strategy that serves to amass evidence about the selected subject. When monitoring this phenomenon requires the use of technological sensors, decisions have to be made about where to locate them, as well as when and for how long. The role of citizens is fundamental in this process since they can provide local knowledge as to when and where it is best to monitor the phenomenon. In this phase, it may be useful to set up a matrix of requirements and preferences that allow participants to make decisions. At this stage, citizens also make informed decisions about how the data collected by their sensor is shared and visualised to meet privacy concerns. Different scenarios of data sharing are collaboratively created and discussed.

![](https://i.imgur.com/AU9AfXX.jpg)

Once the data collection strategy has been defined, it is time to install the sensors to collect the data required. To do so, resources and methods are deployed to help install and configure the sensors. Advice and strategies are given to support sensor calibration methods and ensure that the data provided by citizens is as accurate as possible.

![](https://i.imgur.com/ro74n2z.jpg)

Helping participants to understand the data and its meaning is a vital part of the intervention. Meet-ups and social events are organised to make data analysis a social and learning experience. Visualisation of the data is a crucial part of this phase, as it raises awareness among the group taking part and the larger public not directly involved in the intervention. In addition to the data collected using the sensors, participants' personal stories about how they experience their relationship with their environment in their daily lives are also relevant to collect. Merging quantitative and qualitative data enables more informed data analysis that considers local knowledge.

![image alt](https://live.staticflickr.com/4483/38165401276_ef6eacca0c_h.jpg "Smart Citizen Data Literacy and Awarness")

The data analysis results help identify areas where action is needed to bring about change. At this point, the community should plan for change based on collected, structured and analysed evidence. Cocreating and planning collective action is the main activity in this phase. Although many citizen data collection interventions are designed around using a specific technology that helps in data collection, more than providing citizens with a tool is needed to set up and sustain a participatory process. The continuity and sustainability of citizen data collection initiatives are some of these movements' biggest challenges. Designing for sustainability and a sense of belonging goes beyond creating and using material objects. Participatory design researchers use the notion of infrastructure [^9] to express the preparation of a sociotechnical context that supports public participation in the long term, generating a sense of attachment and belonging that helps to sustain commitment.

The infrastructure process can be understood as the creation of the necessary sociotechnical means and resources for accessible knowledge (e.g. toolkits and methods), technology (e.g. open tools and data platforms) and relationships (e.g. networks and public events) for citizen data collection initiatives to scale, grow and last, thereby producing a more profound transformation in society and, ultimately, in the way we produce and use scientific and non-scientific knowledge.

![image alt](https://i.imgur.com/md5MEp0.jpg "Smart Citizen Data Literacy and Awarness")

## Learn more

More information about the Smart Citizen project can be found in:

- Web: https://smartcitizen.me
- Documentation: https://docs.smartcitizen.me
- Platform: https://smartcitizen.me/kits
- Various open-source repositories: https://github.com/search?utf8=%E2%9C%93&q=smartcitizen

The devices can be purchased through the SEEED Studio Marketplace and are available as a [Kit](https://www.seeedstudio.com/Smart-Citizen-Kit-p-2864.html) or a [Starter Pack](https://www.seeedstudio.com/Smart-Citizen-Starter-Kit-p-2865.html). An additional [sales channel](mailto:info@fablabbcn.org) is directly provided by Fab Lab Barcelona for customised and more advanced developments.


## References

[^1]: www.euro.who.int/en/ media-centre/sections/ press-releases/2015/04/ air-pollution-costs- european-economies- us$-1.6-trillion-a-year-in- diseases-and-deaths,- new-who-study-says
[^2]: Max Craglia and Carlos granell: 2014. Citizen Science and Smart Cities—Report of Summit Ispra, 5–7 February 2014. JRC Technical Report.
[^3]: Muki Haklay: 2015. Citizen Science and Policy: A European Perspective. washington, DC: woodrow wilson International.
[^4]: what Is Citizen-generated Data and what Is the DataShift Doing to Promote it? Retrieved from civicus.org/images/ ER%20cgd_brief.pdf
[^5]: Denisa Kera, Jan Rod and Radka Peterova 2013. Post-Apocalyptic Citizenship and Humanitarian Hardware. Nuclear Disaster at Fukushima Daiichi: Social, Political and Environmental Issues, p. 97.
[^6]: Smart Cities Need Thick Data, Not Big Data.
The Guardian, 18 April 2018 www.theguardian. com/science/political- science/2018/apr/18/ smart-cities-need-thick- data-not-big-data
[^7]: Smart Citizen Kit: https://smartcitizen.me
[^8]: Smart Citizen API: https://developer.smartcitizen.me
[^9]: Ehn, P.: 2008. Participa- tion in design things. In Proceedings of the tenth anniversary conference on participatory design 2008 (pp. 92–101). Indiana University. Bjögvinsson, E., Ehn, P. and Hillgren, P.A.: 2012. Design things and design thinking: Con- temporary participatory design challenges. Design issues, 28(3), pp. 101– 116. Dantec, C.A.l. and DiSalvo, C.: 2013. Infra- structuring and the for- mation of publics in par- ticipatory design. Social Studies of Science, 43(2), pp. 241–264.