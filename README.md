# finalproject-group15

## Presentation 

**Topic:** When fossil fuels are burned, they emit lots of gasses into our atmosphere; specifically carbon dioxide and greenhouse gasses. This causes a rise in temperatures as greenhouse gasses cause rise in temperatures globally as they trap heat in the air. This analysis will be linear as we will discover the trends/patterns between the amount of fossil fuels and their impact with temperature on a global scale from the years of 1995-2020. 


### Questions we hope to answer with our analysis 

- As fossil fuel emissions increase, does global temperature increase thereafter? 

- Are different areas of the planet affected differently by emission increase?

- What years did the temperature first begin to have a significant change?


**Technology:** For our analysis, we will be using the following- 

- *Python:* Clean/organize data 
- *Jupyter:* Jupyter notebook will be used to run Python and run the specific modules we'll need to create data frames 
- *Pandas:* this module will allow us to create data frames that we will need to store and organzie after we clean our datasets. In the end, we will have 
three seperate data frames, but will use the final data frame which is a combination of both for our analysis. 
- *Matplotlib:* This will allow us to create the visualizations we need for our presentation and analysis 
- *Tableau Public:* might use this to create a visual dashboard/story of our overall findings 
- *PostGres:* might use this database to store all of our tables and findings. It will allow us to create an integral environment for our data 

## ERD & Postgres

We will be using two CSV files that contain our very large datasets. 

- Fossil Fuel Emissions Data: [owid-co2-data.csv](https://github.com/sherryli1116/finalproject-group15/files/9924958/owid-co2-data.csv)

[owid-co2-data.csv](https://github.com/sherryli1116/finalproject-group15/files/9924958/owid-co2-data.csv)
    
    Source: Kaggle.com, accessed 2 November 2022, <https://www.kaggle.com/datasets/kvnxls/co2-emissions-dataset-1750-2020>

- Environment Temperature Change Data: [Daily Temperature of Major Cities][Daily Temperature of Major Cities](https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities?select=city_temperature.csv)
    
    Source: Kaggle.com, accessed 2 November 2022, <https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities-            
    select=city_temperature.csv>

Both datasets include the information and years we need to compelete our analysis. There is excess data we will need to clean/transform before we can
actually start with our project. Our game plan is to create data frames after cleaning the data we want from both datasets and then combining the clean
data sets for our final analysis. 

The first dataset consists of data on fossil fuel emissions by country by year. The second file includes daily
temperatures for different cities by year. The datasets will be cleaned using Python/Pandas in Jupyter Notebook prior to uploading and storing in 
Postgres. ERD shows that two tables expected to be created after the files have been cleaned.  

![ERD.png](ERD.png)


## Machine Learning and Data Analysis Plan

Using these Datasets, a linear model will be developed on a per city basis.  The assumption is that Linear is most appropriate as the impacts of carbon
emissions on the relative temperature.  Using the developed models, a estimation will be built using linear regression to form an esimate of future 
temperatures of available cities by years.  SciKit modeling through Supervised Machine Learning will be used as the most efficient system for large
datasets but with few variables. 


## proposed project
![image](https://user-images.githubusercontent.com/107594247/199644565-db7ad290-06e9-4a58-8209-e01f7a46dc50.png)


![image](https://user-images.githubusercontent.com/107594247/199403276-957fe9ae-c117-4c59-90a9-9d08d3cc5e5a.png)
