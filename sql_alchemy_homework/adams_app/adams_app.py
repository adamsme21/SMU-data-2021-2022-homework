import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine

path = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(path)

app = Flask(__name__)


@app.route("/")
def home():
    print("Server received the / request, or the listener was activated")
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def getprecip():
    conn = engine.connect()
    query="""
        SELECT
            date,
            station,
            prcp
        FROM
            measurement
        ORDER BY
            date asc,
            station asc
        """
    df2 = pd.read_sql(query, conn)
    conn.close()
    data = df2.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def stations():
    conn = engine.connect()    
    query= """
        SELECT
            station,
            name
        FROM
            station
        """

    df4= pd.read_sql(query, conn)
    conn.close()
    data = df4.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/tobs")
def tempobs():
    conn = engine.connect()
    query="""
        SELECT
            s.station,
            s.name,
            m.tobs,
            m.date
        FROM
            station s
        JOIN 
            measurement m on s.station = m.station
        WHERE
            s.station = 'USC00519523'
        AND
            date >= '2016-08-23';
        """
    df5= pd.read_sql(query, conn)
    conn.close()
    data = df5.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def startprcp(start):
    conn = engine.connect()
    query= """
        SELECT
            min(tobs),
            max(tobs),
            avg(tobs)
        FROM
            measurement
        WHERE
            date = '{start}'
        """
    df6= pd.read_sql(query, conn)
    conn.close()
    data = df6.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def rangeprcp(start, end):
    conn = engine.connect()
    query= f"""
        SELECT
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM
            measurement
        WHERE
            date >= '{start}'
        AND date <= '{end}'
        """
    df7= pd.read_sql(query, conn)
    conn.close()
    data = df7.to_dict(orient="records")
    return(jsonify(data))


if __name__ == '__main__':
    app.run(debug=True)

        