# Import the dependencies.
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
import pandas as pd

#################################################
# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#################################################

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
app = Flask(__name__)
#open and close the sessions individually

#################################################


#################################################
# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This will return the latest 12 months of precipitation by day as a dictionary.<br/><br/>"
        f"/api/v1.0/stations<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This will return all weather monitoring stations represented in this data.<br/><br/>"
        f"/api/v1.0/tobs<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This will return the most recent year of temperature data from the most active station.<br/><br/>"
        f"/api/v1.0/start_date<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This will return the minimum, average, and maximum temperature over a time range spanning<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp the user-specified start_date to the last date in the data. As an example, you could type the following endpoint:<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp /api/v1.0/2016-08-23<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp to get the minimum, average, and maximum temperatures from 2016-08-23 to the last date.<br/><br/>"
        f"/api/v1.0/start_date/end_date<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This works exactly as the above end point, except you also specificy an end date instead of<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp defaulting to the last date in the data.<br/><br/>"
        f"/api/v1.0/all_dates/start_date<br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp This is not a question in the module, but this end point returns the mininum, average, and maximum <br/>"
        f"&nbsp&nbsp&nbsp&nbsp&nbsp termperatures for EVERY day starting with the start date and ending with the last date in the data.<br/>"
    )

#################################################
