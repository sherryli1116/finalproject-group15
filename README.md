# finalproject-group15

## ERD & Database
Two datasets will be used in this project. The first dataset consists of data on fossil fuel emissions by country by year. The second file includes daily
temperatures for different cities by year. The datasets will be cleaned using Python/Pandas in Jupyter Notebook prior to uploading and storing in 
Postgres. ERD shows that two tables expected to be created after the files have been cleaned.  

![ERD.png](ERD.png)

## Resources:

1. File Name: fossil-fuel-co2-emissions-by-nation.csv
	
	a. Source: Kaggle
	
	b. Data Description: Data on different fuel emissions by country from 1751-2014
	
		i. Year
		ii. Country
		iii. Total (million metric tons of C)
		iv. Solid Fuel
		v. Liquid Fuel
		vi. Gas Fuel
		vii. Cement
		viii. Gas Flaring
		ix. Per Capita
		x. Bunker Fuels (Not in Total)

2. File Name: owid-co2-data

	a. Source: Kaggle
	
	b. Data Description: Data on different fuel emissions by country from 1949-2020
	
		i. Country
		ii. Year
		iii. Co2
		iv. Co2 per Capita
		v. Cement co2 and Cement co2 per capita
		vi. Coal co2 and Coal co2 per capita
		vii. Flaring co2 and Flaring co2 per capita
		viii. Gas co2 and Gas co2 per capita
		ix. Oil co2 and Oil co2 per capita
		x. Various other columns including global share per type 

3. File Name: CO2_emission

	a. Source: Kaggle, original source is https://data.worldbank.org
	
	b. Data Description: Data on CO2 emissions by country/region from 1990-2019
	
		i. Country
		ii. Region
		iii. Year

4. File Name: city_temperature

	a. Source: Kaggle (https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities)
	
	b. Data Description: Data on daily temperatures by world cities from 1995-2020
	
		i. Region
		ii. Country
		iii. City
		iv. Month/Day/Year
		v. Average Temperature

5. File Name: GlobalLandTemperatures_GlobalLandTemperaturesByCountry

	a. Source: Kaggle, original source is https://berkeleyearth.org
	
	b. Data Description: Data on average monthly temperature by country from 1743-2013
	
		i. Date
		ii. Average Temperature
		iii. Average Temperature Uncertainty
		iv. Country

## List of Resources in Folder and what data is relevant

Environment temperature Change - Change in temperature by year and location going back to 1961

FAOSTAT Data - By month temp differences in a single location by year

ghcn-m-v1 - Temperatures calculated at exact latitude and longitues across the globe back to 1880 (-9999 is null values)

results-2020 - 2000s era storm data for the US

CityTs - Massive file i had to break up to upload.  ~2Mil datapoints for city month day year back to 1995 and the average Temperature


##Additional Resources available (too large to upload but maybe usable in SQL?)

https://www.kaggle.com/datasets/sohelranaccselab/global-climate-change   - Fantastic data, just is ~520MB in size so its difficult to move it here

## proposed project
![image](https://user-images.githubusercontent.com/107594247/199644565-db7ad290-06e9-4a58-8209-e01f7a46dc50.png)


![image](https://user-images.githubusercontent.com/107594247/199403276-957fe9ae-c117-4c59-90a9-9d08d3cc5e5a.png)
