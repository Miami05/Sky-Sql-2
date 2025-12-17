from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"


QUERY_FLIGHTS_BY_DATE = """
        SELECT flights.*,
       airlines.airline,
       flights.ID as FLIGHT_ID,
       flights.DEPARTURE_DELAY as DELAY
       FROM flights
       JOIN airlines ON flights.airline = airlines.id
       WHERE flights.day = :day
       AND flights.month = :month
       AND flights.year = :year
"""

QUERY_DELAYED_FLIGHTS_BY_AIRLINE = """
    SELECT flights.*,
           airlines.AIRLINE as airline_name,
           flights.ID as FLIGHT_ID,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE flights.DEPARTURE_DELAY > 0
      AND airlines.AIRLINE = :airline_input
"""


QUERY_DELAYED_FLIGHTS_BY_ORIGIN = """
    SELECT flights.*,
           airlines.AIRLINE as airline_name,
           flights.ID as FLIGHT_ID,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE flights.DEPARTURE_DELAY > 0
      AND flights.ORIGIN_AIRPORT = :origin_airport
"""


# Define the database URL
DATABASE_URL = "sqlite:///data/flights.sqlite3"

# Create the engine
engine = create_engine(DATABASE_URL)


def execute_query(query, params):
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records (dictionary-like objects).
    If an exception was raised, print the error, and return an empty list.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            records = result.fetchall()
            return records
    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id):
    """
    Searches for flight details using flight ID.
    If the flight was found, returns a list with a single record.
    """
    params = {"id": flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)


def get_flights_by_date(day, month, year):
    """Return all flights scheduled on a specific date"""
    params = {"day": day, "month": month, "year": year}
    return execute_query(QUERY_FLIGHTS_BY_DATE, params)


def get_delayed_flights_by_airline(airline_input):
    """Return all delayed flights for a given airline"""
    params = {"airline_input": airline_input}
    return execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRLINE, params)


def get_delayed_flights_by_airport(origin_airport):
    """Return all delayed flights for a given airport"""
    params = {"origin_airport": origin_airport}
    return execute_query(QUERY_DELAYED_FLIGHTS_BY_ORIGIN, params)
