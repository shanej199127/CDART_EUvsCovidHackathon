<p align="center">
   <img width="527" height="255" src="https://github.com/shanej199127/CDART_EUvsCovidHackathon/blob/master/img/cdart%20logo.jpg">

</p>

# CDART_EUvsCovidHackathon
Group for hackathon for EU VS Covid 2020


# A big thank you to all contributors 

# Version 0.1
# Project Overview

We try to create a platform where, later to be rolled out as an app (android/ios) which risk profile based on your location. i.e. moving from Hochtaunuskreis to Maintaunus Kreis your risk goes up since there are more infected people in MTK than in HG. Add some info on Hospital availability on top to complete the risk profile for travellers. 

Providing a risk-assessment tool to businesses determining,

a) who could go back to work based on low risk profile and 

b) which customer would be allowed to enter store based on risk profile. 

Risk profile will depend on location/distances traveled in a given time period/people surrounding the person. Thereby providing an ecosystem to monitor people's health and predict possible asymptamatic cases.

Please visit <youtube video link> for a porject 

# Technical Overview
![Technical Model Diagram](https://github.com/shanej199127/CDART_EUvsCovidHackathon/blob/master/img/Technical%20Model%20Diagram.JPG)


# Backend Services
The backend databases are managed in Backendless (https://develop.backendless.com/). New data sources will be added through API calls or importing csv files (for ones APIs are not available) into the backend DB.

This data is then being sent over to a server where a predictive model will be run which provides a <b>SCORE</b> value for that user/district. This will be prompted back again at frontend. Meantime, backend will automatically create a <b>TIMETAG</b> to have previous predicted risk scores of the user/district.

# Frontend Services
Data is being populated and aggregated to/from backend via REST API generated via Backendless. Data is gathered in 3 main pilars namely, Personal health Data, Location Data, Family & Associates Data. More pilars could be easily integrated for future developments. Currently being developed for iOS. 


<p align="center">
   <img width="348" height="722" title="Proposed App" src="https://github.com/shanej199127/CDART_EUvsCovidHackathon/blob/master/img/app1%20(1).JPG">

</p>

# Incoming Data Source
MVP work is focussed on Showcasing for Germany only.

Robert Koch Institute COVID Data: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0

Mobility Data from: Google LLC "Google COVID-19 Community Mobility Reports." https://www.google.com/covid19/mobility/ Accessed: 2020-04-25.
 
Los Alamos Data: https://www.lanl.gov/
 
## ******* Feel free to pull and waiting you for thoughts on helping the world combat COVID-19 *******

# Future releases (version 1.0):
1. REST APIs for data reads for future developers
2. Front-end integration for Android
3. Right now the granurality is for Landkreis (District) level for Germany. In future, this could be extended to other countries.
