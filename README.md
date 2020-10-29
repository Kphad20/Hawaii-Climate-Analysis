# SQLAlchemy-Hawaii Climate Analysis

## Step 1 - Climate Analysis and Exploration
To begin, I will use Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis will be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

1. I'll choose a start date and end date for my trip (July 25, 2020 - August 7, 2020).
2. I'l use SQLAlchemy "create_engine" to connect to my sqlite database.
3. Use SQLAlchemy "automap_base()" to reflect my tables into classes and save a reference to those classes called "Station" and "Measurement."

### Precipitation Analysis
1. Design a query to retrieve the last 12 months of precipitation data.
2. Select only the date and prcp values.
3. Load the query results into a Pandas DataFrame and set the index to the date column.
4. Sort the DataFrame values by date.
5. Plot the results using the DataFrame plot method.
6. Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis
1. Design a query to calculate the total number of stations.
2. Design a query to find the most active stations.
</br>- List the stations and observation counts in descending order.
</br>- Find the station with the highest number of observations.
</br>- I'll use functions such as "func.min," "func.max," "func.avg," and "func.count" in my queries.

3. Design a query to retrieve the last 12 months of temperature observation data (TOBS).
</br>- Filter by the station with the highest number of observations.
</br>- Plot the results as a histogram with bins=12.

## Step 2 - Climate App
After my initial analysis, I will design a Flask API based on the queries that I have just developed. I'll use Flask to create my routes.

### Routes
1. /
</br>- Home page.
</br>- List all available routes.

2. /api/v1.0/precipitation
</br>- Convert the query results to a dictionary using date as the key and prcp as the value.
</br>- Return the JSON representation of dictionary.

3. /api/v1.0/stations
</br>- Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs
</br>- Query the dates and temperature observations of the most active station for the last year of data.
</br>- Return a JSON list of temperature observations (TOBS) for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
</br>- Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
</br>- When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
</br>- When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

### Notes
I will need to join the station and measurement tables for some of the queries and use Flask jsonify to convert my API data into a valid JSON response object.

##  Step 3 - Temperature Analysis
1. The notebook contains a function called "calc_temp" that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
2. I will use the calc_temps function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year.
3. I will plot the min, avg, and max temperature from my previous query as a bar chart.
</br>- I will use the average temperature as the bar height.
</br>- I will use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

4. I will calculate the rainfall per weather station using the previous year's matching dates.



