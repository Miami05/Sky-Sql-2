# Flight Data Query System

A command-line application for querying flight data from a SQLite database. Search flights by ID, date, airline, or airport with CSV export support.

## Features

- Search flights by ID or date
- Find delayed flights by airline or airport
- Export results to CSV
- Input validation for dates and IATA codes
- Interactive menu interface

## Installation

```bash
pip install sqlalchemy
```

**Requirements:** Python 3.6+, SQLite database at `data/flights.sqlite3`

## Usage

```bash
python main.py
```


### Menu Options

1.  Show flight by ID
    
2.  Show flights by date
    
3.  Delayed flights by airline
    
4.  Delayed flights by origin airport
    
5.  Exit

## Examples

### Search by Flight ID
Enter flight ID: 12345  
Got 1 results.  
12345. LAX -> JFK by American Airlines, Delay: 15 Minutes


### Search by Date
Enter date in DD/MM/YYYY format: 25/12/2024  
Got 147 results.  
12345. LAX -> JFK by American Airlines  
12346. ORD -> MIA by United Airlines, Delay: 30 Minutes


### Delayed Flights by Airline
Enter airline name: American Airlines  
Got 23 results.  
12345. LAX -> JFK by American Airlines, Delay: 15 Minutes


### Delayed Flights by Airport
Enter origin airport IATA code: LAX  
Got 18 results.  
12345. LAX -> JFK by American Airlines, Delay: 15 Minutes


## CSV Export

After each query:
Would you like to export this data to a CSV file? (y/n): y  
Enter filename (e.g., delayed_flights.csv): results.csv  
Results exported successfully to results.csv


**CSV Columns:** FLIGHT_ID, ORIGIN_AIRPORT, DESTINATION_AIRPORT, AIRLINE, DELAY

## Input Validation

- **Flight ID**: Must be an integer
- **Date**: Format `DD/MM/YYYY` (e.g., 25/12/2024)
- **IATA Code**: Exactly 3 letters (e.g., LAX, JFK)
- **Airline**: Any string (case-sensitive)

## Project Structure

project/  
├── main.py # CLI application  
├── flights_data.py # Database queries  
└── data/  
└── flights.sqlite3 # SQLite database

## Database Schema

### `flights` Table
- `ID`, `ORIGIN_AIRPORT`, `DESTINATION_AIRPORT`, `AIRLINE` (FK)
- `DEPARTURE_DELAY`, `DAY`, `MONTH`, `YEAR`

### `airlines` Table
- `ID`, `AIRLINE` (name)

## Configuration

Change database path in `flights_data.py`:
DATABASE_URL = "sqlite:///data/flights.sqlite3"


## Troubleshooting

- **"Query error"**: Check database file exists and has correct schema
- **"Try again..." for dates**: Use exact format DD/MM/YYYY
- **No results**: Verify airline names are case-sensitive exact matches
- **CSV fails**: Check write permissions and include .csv extension

## License

MIT License - Copyright (c) 2025

