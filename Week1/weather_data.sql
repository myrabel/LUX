//1. Find all records where the weather was exactly clear.

SELECT * FROM Weather_Data WHERE (Weather = 'Mainly Clear' OR Weather = 'Clear');
SELECT COUNT(*) FROM Weather_Data WHERE (Weather = 'Mainly Clear' OR Weather = 'Clear');


//2. Find the number of times the wind speed was exactly 4 km/hr//

SELECT COUNT(*) FROM Weather_Data WHERE "Wind Speed_km/h" = '4';

//3. What is the mean visibility of the dataset?//
SELECT AVG(Visibility_km) from Weather_Data;


//4. Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km//
SELECT * FROM Weather_Data WHERE ("Wind Speed_km/h" > '24') AND (Visibility_km = '25');


//5. What is the mean value of each column for each weather condition?//
SELECT AVG(Temp_C) from Weather_Data;
SELECT AVG("Dew Point Temp_C") from Weather_Data;
SELECT AVG("Rel Hum_%") from Weather_Data;
SELECT AVG("Wind Speed_km/h") from Weather_Data;
SELECT AVG(Visibility_km) from Weather_Data;
SELECT AVG(Press_kPa) from Weather_Data;

