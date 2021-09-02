#  <#Title#>

### Question/Need:

* What is the question behind your analysis? What is the purpose of the model/system you plan to build?
A large pharmacy chain store (think Walgreens/Duane Reade) is considering closing a fraction of its stores in NYC over the next year and wants to understand which areas have had reduced foot traffic due to COVID-19. They want to use the MTA data from Q3 2020 - Q3 2021 to decide which stores they should close this year. 

To begin with, they have suggested looking specifically at store closures in lower Manhattan, one of the areas most affected by the pandemic.

* Who benefits from exploring this question or building this model/system?
The pharmacy chain store will benefit from having less costs for the next year. In addition, city authorities might benefit from understanding which areas in Manhattan are experiencing lower foot traffic overall (and hence may require redistribution of city resources).

### Data Description:

* What dataset(s) do you plan to use, and how will you obtain the data?
In addition to the MTA turnstile data, I will use the following datasets:
* * Dataset of MTA station names (available from the MTA website)
* * Dataset of Walgreens stores in NYC (Scrape from DR website or Google Places API)
* * Choose subset of stations within lower Manhattan and stores within a certain radius distance (to be determined)

* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?
I expect a unit of analysis to be a subway station in lower Manhattan with a time series over 1 year (2020-2021) showing daily entries and exits. 

### Tools:

* How do you intend to meet the tools requirement of the project?
I will use SQL to query the database and extract or update any tables as needed. Then I will use pandas to conduct EDA on the database, including cleaning, exploratory analysis and joining of any relevant datasets. I will also use Matplotlib to consider time series visualizations. For location coordinates/geospatial data, I will query from Google Places API or use OpenStreetMap.

* Are you planning in advance to need or use additional tools beyond those required?
I may use BeautifulSoup to scrape Walgreens locations in the lower Manhattan area. If there is time, I might also use a mapping tool to show a time-series bubble map of subway usage over the year.

### MVP Goal:

* What would a minimum viable product (MVP) look like for this project?
I will start with 3 subway stations (which ones to be determined) and look only at those locations and the Walgreens locations closest to these stations. If I write my code efficiently, I will be able to run the same code for a larger set of locations with minimal editing.
