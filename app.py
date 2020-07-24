import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

##################################################

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Flask setup
app = Flask(__name__)

##################################################

# Home route
@app.route("/")
def home():
    return (
        f"Hawaii Climate App<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    # Get one year from last record 
    last_year_prcp = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query data to get date and corresponding precipitation for the last year 
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year_prcp).filter(
        Measurement.prcp != None).order_by(Measurement.date).all()

    session.close()
    
    # Convert the query results to a dictionary using date as the key and prcp as the value.
    precip_data = []
    for date, prcp in results: 
        precip_dict = {}
        precip_dict[date] = prcp
        precip_data.append(precip_dict)

    # Return the JSON representation of your dictionary.
    return jsonify(precip_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    # Query list of stations
    stations_list = session.query(Station.station, Station.name).all()

    session.close()

    # Create dictionary with data
    station_data = []
    for station, name in stations_list:
        station_dict = {}
        station_dict[station] = name
        station_data.append(station_dict)

    # Return a JSON list of stations from the dataset.
    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # Get one year from last record of most active station, USC00519281
    year_temp_USC00519281 = dt.date(2017, 8, 18) - dt.timedelta(days=365)

    # Query the temperature for the last 12 months for the most active station 
    temp_data = session.query(Measurement.date, Measurement.tobs).filter(
    Measurement.date >= year_temp_USC00519281).filter(Measurement.station == 'USC00519281').all()

    session.close()
    
    # Create dictionary
    temp_list = []
    for date, tobs in temp_data:
        temp_dict = {}
        temp_dict[date] = tobs
        temp_list.append(temp_dict)

    # Return a JSON list of temperature observations (TOBS) for the previous year for the most active station.
    return jsonify(temp_list)

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)

    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date
    temp_summary = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(
        Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()

    # Create dictionary
    start_date_list = []
    for tobs in temp_summary:
        start_dict = {}
        start_dict["TMIN, TMAX, TAVG"] = tobs
        start_date_list.append(start_dict)
    
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date
    return jsonify(start_date_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)

    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    temp_start_end_summary = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(
        Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()

    session.close()

    # Create a dictionary
    start_end_date_list = []
    for tobs in temp_start_end_summary:
        start_end_dict = {}
        start_end_dict["TMIN, TMAX, TAVG"]= tobs
        start_end_date_list.append(start_end_dict)
    
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end date range.
    return jsonify(start_end_date_list)

if __name__ == "__main__":
    app.run(debug=True)

