# CDART_EUvsCovidHackathon
Group for hackathon for EU VS Covid 2020


# A big thank you for Contributors 
# version 1.0

We try to create a platform where, later to be rolled out as an app (android/ios) which risk profile based on your location. i.e. moving from Hochtaunuskreis to Maintaunus Kreis your risk goes up since there are more infected people in MTK than in HG. Add some info on Hospital availability on top to complete the risk profile for travellers. 

Providing a risk-assessment tool to businesses determining
a) who could go back to work based on low risk profile and 
b) which customer would be allowed to enter store based on risk profile. 
Risk profile will depend on location/distances traveled in a given time period/people surrounding the person. Thereby providing an ecosystem to monitor people's health and predict possible asymptamatic cases.

Technical diagram could be found in Technical Model Diagram.vsdx 

![Technical Model Diagram](https://user-images.githubusercontent.com/45632421/80303039-11bed600-87ae-11ea-8512-eef72802a8d4.JPG)

# Incoming Data Source
COVID Data from: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0

Age Data from: https://www-genesis.destatis.de/gis/genView?GenMLURL=https://www-genesis.destatis.de/regatlas/AI002-2.xml&CONTEXT=REGATLAS01

Mobility Data from: Google LLC "Google COVID-19 Community Mobility Reports." https://www.google.com/covid19/mobility/ Accessed: 2020-04-25.
 

# Future releases:
1. REST APIs for data reads for future developers
2. Front-end integration for Android
3. Right now the granurality is for Landkreis (District) level for Germany. In future, this could be extended to other countries.
