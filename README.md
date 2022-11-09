# finalproject-group15

## City Temperature Dataset Cleaning

Note: Raw dataset includes 2,906,328 rows and the following columns:
	Region , Country, State, City
	Month, Day, Year, AvgTemperature

During cleaning of the dataset, the following assumptions were made:

1.	Reviewed dataset for empty cells. Empty cells were noted in ‘State’ column only. As temperature calculations will be done at country level, this 
does not have any impact.

2.	Removed 2020 data as file only includes data May 2020. The number of rows removed equaled 38,810.

3.	Dataset includes years ‘200’ and ‘201’. As the average temperature noted for these two years equals (-99), the years will be removed from
dataset. The number of rows removed equaled 440. 

4.	After running summary statistics on the dataset, additional steps were taken to determine the number of lower and upper bound outliers. The 
number of lower bound outliers totaled 91,315, of these, 79,164 equaled an average temperature of (-99). As these are considered outliers, the rows were 
removed from the dataset. After updating the dataframe, the summary statistics were re-run. Cities listed as lower bound outliers were deemed
appropriate
and no additional adjustments were made. 


## ERD & Database
Two datasets will be used in this project. The first dataset consists of data on fossil fuel emissions by country by year. The second file includes
daily temperatures for different cities by year. The datasets will be cleaned using Python/Pandas in Jupyter Notebook prior to uploading and storing in 
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
