#  California Racial Identify Profiling Act (RIPA) Dashboard

### Question/Need:

In 2015, California's State Congress passed Assembly Bill (AB) 953 which enacted the Racial and Identify Profiling Act (RIPA). This act, among other things, requires peace officers to annually report stop data to the Attorney General's office at the California Department of Justice (DOJ). The act also requires peace officers to record their perception of characteristics relevant to each stopped person(s), including gender, race and ethnicity, LGBT status, approximate age, disability and English fluency. 

Data collection for RIPA has proceeded in waves, starting in 2018, beginning with the Law Enforcement Agencies (LEAs) with more than 1000 officers, and expanding to include all LEAs in the state by January 1, 2022. This year, all LEAs in the state will be required to submit their stop data to the DOJ. 

### Current context:

Currently there are several dashboards visualizing the stop data for the first 2 waves of LEA submissions, including the official [DOJ dashboard](https://openjustice.doj.ca.gov/exploration/stop-data). This information is aggregated at the state level and not tailored to individual agencies, and therefore is difficult to use at the local or city level. 

In my experience working with police agencies and city officials, many cities desire to have simple, easy to understand web applications displaying visualizations and statistics for their citizens to understand. However, many smaller cities typically do not have the technical capability to build such an application.

I built a [web application](https://ripa-dash.herokuapp.com/) that allows users and agencies to break down relevant RIPA data to the agency level, and also provides visualizations and statistics of stops, their breakdown by race, ethnicity, and identity, and also provides coordinate locations for each stop. This dashboard will be automatically updated annually when the next wave of RIPA data is rolled out. 

My hope is that the web application can be embedded or linked by police agencies and city councils, in order to provide more information and transparency for their residents.

### Data Description:

The dataset(s) I will use are 3 datasets in CSV format for the years 2018-2020, with about 3M stops per year, downloaded from the [Dept of Justice's Data Portal](https://openjustice.doj.ca.gov/data). 

The unit of analysis is a single stop. There are dozens of features and columns in the dataset. I will use the following:

* Agency name
* Time of stop
* Date of stop
* Duration of stop
* Whether the stop occured in a school or involved a student
* Perceived race or ethnicity of citizen
* Perceived gender of citizen
* Perceived LGBT status
* Perceived age
* English fluency
* Perceived disability status
* Reason for stop
* Whether a search was conducted
* If search was conducted, whether any contraband or evidence was discovered
* Locality of the search (nearest city)

### Tools:

![Data pipeline](/eng/project/images/pipeline2.png)

As per the sketch above, I achieved the following to complete this app.

* Downloaded 3 RIPA CSVs from the DOJ data portal (>6M rows; 4GB total)
* Stored data in Heroku's PosTgreSQL using the Heroku CLI
* Cleaned data into useable format using PostgreSQLPython, pandas, NumPy
* Created a dashboard using Dash/Plotly and Mapbox and deploy to web using Heroku
* Built robustness tests using Heroku

### Sources of Inspiration:

I took inspiration from the CA DOJ's data exploration portal linked below:
* [How do stops unfold?](https://openjustice.doj.ca.gov/exploration/stop-data)

I borrowed heavily from the following links:
* [Dash Callbacks Tutorial](https://dash.plotly.com/basic-callbacks)
* [Plotly Mapbox Tutorial](https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter_mapbox.html)
* [Heroku app deployment](https://devcenter.heroku.com/categories/deployment)
* [Setting up Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)

Lux theme for dashboard taken from [Bootswatch](https://bootswatch.com/)