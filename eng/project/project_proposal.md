#  California Racial Identify Profiling Act (RIPA) Dashboard

### Question/Need:

In 2015, California's State Congress passed Assembly Bill (AB) 953 which enacted the Racial and Identify Profiling Act (RIPA). This act, among other things, requires peace officers to annually report stop data to the Attorney General's office at the Department of Justice (DOJ). The act also requires peace officers to record their perception of characteristics relevant to each stopped person(s), including gender, race and ethnicity, LGBT status, approximate age, disability and English fluency. 

Data collection for RIPA has proceeded in waves, starting in 2018, beginning with the Law Enforcement Agencies (LEAs) with more than 1000 officers, and expanding to include all LEAs in the state by January 1, 2022. This year, all LEAs in the state will be required to submit their stop data to the DOJ. 

Currently there are several dashboards visualizing the stop data for the first 2 waves of LEA submissions, including the official [DOJ dashboard](https://openjustice.doj.ca.gov/exploration/stop-data). This information is aggregated at the state level and not tailored to individual agencies, and therefore is difficult to use at the local or city level. 

In my experience working with police agencies and city officials, many cities desire to have simple, easy to understand web applications displaying visualizations and statistics for their citizens to understand. However, many smaller cities typically do not have the technical capability to build such an application.

I will build a web application that allows users and agencies to break down relevant RIPA data to the agency level, and also provides visualizations and statistics of stops, their breakdown by race, ethnicity, and identity, and also provides coordinate locations for each stop. This dashboard will be automatically updated annually when the next wave of RIPA data is rolled out. My hope is that the web application can be embedded or linked by police agencies and city councils, in order to provide more information and transparency for their residents.

### Data Description:

* What dataset(s) do you plan to use, and how will you obtain the data?

The dataset(s) I will use are 3 datasets in CSV format for the years 2018-2020, with about 3M stops per year, downloaded from the [Dept of Justice's Data Portal](https://openjustice.doj.ca.gov/data). 

* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

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

* How do you intend to meet the tools requirement of the project?

![Data pipeline](/eng/project/images/pipeline.png)

As per the sketch above, I will use the following tools to build my data pipeline. 

* Download the annual RIPA CSVs from the DOJ data portal
* Store data in relational database with SQLAlchemy
* Clean data into useable format using Python, pandas, NumPy
* Create a dashboard using Dash/Plotly and deploy to web using Heroku
* I will build several robustness tests for future data downloads, and also build a scraper tool to periodically check for updates on the DOJ data portal

### MVP Goal:

* What would a minimum viable product (MVP) look like for this project?

For my MVP, I will begin by processing the smallest dataset for 2018, and build several visualizations using the dataset. If successful, it should be easy to then add on the 2 larger datasets (2019 and 2020).