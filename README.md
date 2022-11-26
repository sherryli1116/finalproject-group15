# Fossil Fuels and the Rise of Temperatures

## A. Presentation 

**[Presentation Slides Link](https://docs.google.com/presentation/d/1LIIxNE26tEv9yMHcSfNOcbrMop_bMVocx2V1dUVHUj8/edit#slide=id.p)**

### **1. Topic** 

When fossil fuels are burned, they emit lots of gasses into our atmosphere; specifically carbon dioxide and greenhouse gasses. This causes a rise in temperatures as greenhouse gasses cause rise in temperatures globally as they trap heat in the air. This analysis will be linear as we will discover the trends/patterns between the amount of fossil fuels and their impact with temperature on a global scale from the years of 1995-2020. 

### **2. Reason topic was selected** 

There are many reasons towards climate change, but the one that has contributed the most are greenhouse gasses. 

- greenhouse gasses trap heat in the Earth’s atmosphere causing a rise in temp 
- CO2 is the gas that is emitted the most in the atmosphere accounting for a total of 79%, just in the United States
- Fossil fuels are also non-renewable and unsustainable 

### **3. Source of data** 

We will be using two CSV files that contain our very large datasets. 

- Fossil Fuel Emissions Data: [owid-co2-data.csv](https://github.com/sherryli1116/finalproject-group15/files/9924958/owid-co2-data.csv)

  Source: Kaggle.com, accessed 2 November 2022, <https://www.kaggle.com/datasets/kvnxls/co2-emissions-dataset-1750-2020>

- Environment Temperature Change Data: [Daily Temperature of Major Cities](https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities?select=city_temperature.csv) 

  Source: Kaggle.com, accessed 2 November 2022, <https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities?select=city_temperature.csv>

Both datasets include the information and years we need to compelete our analysis. There is excess data we will need to clean/transform before we can actually start with our project. Our game plan is to create data frames after cleaning the data we want from both datasets and then combining the clean data sets for our final analysis. 

### **4. Questions we hope to answer with our analysis** 

- As fossil fuel emissions increase, does global temperature increase thereafter? 

- Are different areas of the planet affected differently by emission increase?

- What years did the temperature first begin to have a significant change?

### **5. Technology** 

For our analysis, we will be using the following- 

- *Python:* Allow us to clean/transform our very large dataset. Use Python functions to get the average of CO2 emissions and temperature.  
- *Jupyter :* Jupyter notebook will be used to run Python and run the specific modules we'll need to create data frames 
- *Pandas:* Create data frames after we have cleaned/transformed our data. For our final analysis, we need to merge both of the clean data frames to get the final data frame to create our visuals.   
- *Matplotlib:* This module will let us create visuals we need for our analysis. This will allow us to determinate what the pattern/trend is between CO2 emissions and temperature.  

### **6. Data Exploration** 

Need to clean/transform both datasets we are working with as they are very large and contain data we don't need for our analysis. We must filter the dates to 1950-2020, remove unnecessary cities/countries that are not included in both files and remove unnecessary columns/rows. When we have cleaned and transformed both datasets, then we need to merge the datasets to be used in our final analysis. 

### **7. Description of analysis phase of project** 

TBD

### **8. Analysis** 

Once we have merged our final dataset, next up is creating visualizations that we need to observe the trends in the data. By doing so, we can answer the questions we need for our analysis and if some visualizations are not enough, we might need to dive into creating other data frames to aid in our analysis. It's crucial we understand the patterns between CO2 emissions and temperature in many different regions around the globe to identify the complexity of how fossil fuel emissions can impact temperature in different regions. 

### **9. Recommendation for future analysis** 

Recommendations for future analysis include exploring other factors that may contribute to temperature changes. Factors
such as population and GDP. 

### **10. Debrief** 

TBD

## B. Machine Learning

### **1. Data Preprocessing**

The following were performed during preprocessing of ‘City_Temperature’ file:

- Dataset contained 2,906,327 rows and 8 columns.
- Used copy() function to copy dataframe while dropping column ‘State’. Analysis will focus on city and country, therefore,
  ‘State’ column deemed unnecessary. 
- Checked for null values. None were noted.  
-	Checked for data types. No changes needed as data types appeared appropriate.
-	Removed values from average temperature column that equaled (-99). Rows removed totaled 79,672. 
-	Removed year 2020 due to incomplete data. Rows removed totaled 38,742. 
-	Ran statistics to identify potential outliers. Performed visual review of data below lower bound and deemed data
  appropriate. There was no data above upper bound. 
-	Used groupby() function to aggregate data by Country, City, and Year. 

Resulting dataframe consists of 91,494 rows and 5 columns. 

The following were performed during preprocessing of ‘owid-co2-data’ file:

-	Dataset contained 25,989 rows and 60 columns.
-	Used copy() function to copy dataframe , retaining columns ‘country’, ‘year’, ‘population’, ‘co2’.
-	Replaced country names for 3 countries to align with ‘City_’Temperature’ dataset. These countries included United States,
  Serbia, and Netherlands. 
-	Removed values for years before 1995 and year 2020 to align with years covered in ‘City_Temperature’ dataset. 
-	Renamed columns ‘Country’ and ‘Year’.
-	Merged dataframe with ‘City_Temperature’ dataset on ‘Country’ and ‘Year’.
-	Checked for null values. None were noted. 
-	Ran statistics to identify potential outliers. No outliers were noted. 

Resulting dataframe consists of 89,468 rows and 7 columns. 

We note that there were limitations with data obtained. Carbon emissions amounts were shown at the country level, while
average temperatures were shown by city. In merging the datasets, an assumption was made to use the carbon emissions by
country at the city level. As such, carbon emissions noted for each city are reflective of the corresponding country's
total emissions. 

### **2. Model selection**

Based on an approximate linear relationship between cumulative carbon emissions and global average temperature change,
a linear regression model was selected as the most appropriate model to predict future temperatures. Linear regression
models are easy to implement and interpret but may be prone to overfitting. Datasets were reviewed to identify
potential outliers. 

Using the linear regression model, the dependent variable was set to average temperature and the independent variable 
to carbon emissions. The model was ran for each city in the dataset. The dataset was split 70% training and 30% testing
sets. The split is standard approach for linear regression models. If the dataset were smaller, adjustments to the
split would have been considered. 

### **2. Results**

TBD

Linear regression model can be found [here](https://github.com/sherryli1116/finalproject-group15/blob/MichaelBranch/Starter.ipynb).

## Proposed Project
![image](https://user-images.githubusercontent.com/107594247/199644565-db7ad290-06e9-4a58-8209-e01f7a46dc50.png)


![image](https://user-images.githubusercontent.com/107594247/199403276-957fe9ae-c117-4c59-90a9-9d08d3cc5e5a.png)

## C. Database

We will not be using a database for our analysis because we don't have too much datasets we're working with. Moreover, we're creating visualizations using Matplotlib and may use tools to showcase our visualizations. Therefore, there was no need to create a database for our project. 

An ERD was prepared to show the tables that can be created if needed and uploaded into a database.   

![ERD.png](ERD.png)

## D. Dashboard

### Tools and Interactive Element
We will be using Tableau to show data visualization. It will display the relationship between CO2 emission and teperature according to different
countries. Viewers will be able to see the changes by selecting different countries using the filter option on Tableau. 

As part of our visualizations, we have included:

- CO2 Emissions by Year - In 2019, there were approximately 36 billion metric tons of CO2 emitted globally. 
- CO2 Emmissions - Top 20 Countries - Shows total CO2 emissions between 1995 - 2019 by the top 20 countries. 
- Yearly CO2 Emissions and Average Yearly Temperatures - Interactive map that allows users to select different years and view changes in Yearly CO2    
  Emissions and Average Yearly Temperatures
- CO2 Emissions and Average Temperature - Shows the linear relationship between CO2 Emissions and Average Temperature

Tableau dashboard can found here

**[Storyboard Link](https://docs.google.com/presentation/d/1l64_2mwr48J9JcGY_hhqfUuMYhpYAVZeGpV3cXkw2LA/edit?usp=sharing)**

(https://public.tableau.com/app/profile/sally6562/viz/NYCCitibikeAnalysis_16677751539650/Analysis?publish=yes):
