# README
## Background

**Smart exposure to digital currencies**, This application uses an interactive command line interface to collect investment information from the user; it then recomends a cryptocurrency portfolio based on risk levels, and by analyzing real-time data using API calls.  This Crypto porfolio analyzer is an innovative addition to the fintech industry. We want to offer optimized cryptocurrency porfolios to everyone, even those who lack the financial knowledge and understanding of cryptocurrencies. We plan to build additional features into this like the ability to link to cryptocurrency wallets, and buying/selling with a cryptocurrency trading bot using machine learning.


## Table of Contents
1. [Front-end Interface](#1-Front-end-Interface)

2. [Calculate and Plot the output from the CLI.](#2-Calculate-and-Plot-the-output-from-the-CLI)

3. [Simulation Trajectories.](#3-Simulation-Trajectories)

4. [Back-End Functionality.](#4-Back-End-Functionality)

5. [Compose the data story.](#5-compose-the-data-story)

---

## 1. Front-end Interface

![1](./Images/Recording%202022-06-08%20at%2020.20.03.gif)

* The CLI python script is located here **File:** [Crypto Porfolio CLI](/appy2.py)
* If then statement was built to personlize the type of investment to user wanted
    
  

## 2. Calculate and Plot the output from the CLI

* The output python script is located here **File:** [Crypto Results Porfolio](/results.py)

 ![2](./Images/Screen%20Shot%202022-06-09%20at%201.46.14%20PM.png))
* API used on this project are as follows
   * yfinance
   * sqlalchemy
   * requests
   * datetime
   * statistics 
   
* The website used for gather crypto data
   * alternative
   
* Create a new DataFrame named `stocks_dataframe` by creating these columns and display the appropiate date.
   * Coins	
   * Symbol	
   * Category	
   * Price	
   * 24Hr Volume	Market Caplization	
   * 1hr % Change	
   * 24hrs %Change	
   * 7days %Change	
   * Sharpe Ratio	
   * Variance
   
* Bar chart was created with predetermined currencies 
* The % this portfolio has made within 1 year period
* The line graph that shows how much money that would have been made if the user invested 1 year prior


## 3. Simulation Trajectories

* The output python script is located here **File:** [MC Database](/mc_database.ipynb.py)

These clips demonstrate the simulator running on our pre-selected portfolio data.
Careful usage of this functionality can enhance our users ability to make informed long term portfolio selections.

![3](./Images/MC-low_risk.gif)

---

![4](./Images/MC-Plot.gif)

---

* Create a new DataFrame that groups the original DataFrame by year and neighborhood. Aggregate the results by the `mean` of the groups.
* Filter out the “housing_units” column to create a DataFrame that includes only the `sale_price_sqr_foot` and `gross_rent` averages per year.
* Create an interactive line plot with hvPlot that visualizes both `sale_price_sqr_foot` and `gross_rent`. 
* Set the x-axis parameter to the year (`x="year"`). 
* Use the `groupby` parameter to create an interactive widget for `neighborhood`.
* Style and format the line plot to ensure a professionally styled visualization.
    * For the Anza Vista neighborhood, is the average sale price per square foot for 2016 more or less than the price that’s listed for 2012?
    ![3](./Images/Anza.png)

## 4. Back-End Functionality

![5](./Images/geoviews_plot.png)

* Read the `neighborhood_coordinates.csv` file from the `Resources` folder into the notebook, and create a DataFrame named `neighborhood_locations_df`. 
* Be sure to set the `index_col` of the DataFrame as “Neighborhood”.
* Using the original `sfo_data_df` Dataframe, create a DataFrame named `all_neighborhood_info_df` that groups the data by neighborhood. 
* Aggregate the results by the `mean` of the group.
* Review the two code cells that concatenate the `neighborhood_locations_df` DataFrame with the `all_neighborhood_info_df` DataFrame. 
* Using hvPlot with GeoViews enabled, create a `points` plot for the `all_neighborhoods_df` DataFrame. 
* Use the interactive map to answer the following question: 
    * Which neighborhood has the highest gross rent, and which has the highest sale price per square foot?

## 5. Compose the Data Story

* Based on the visualizations that you created, answer the following questions:
    * How does the trend in rental income growth compare to the trend in sales prices? Does this same trend hold true for all the neighborhoods across San Francisco?
    * What insights can you share with your company about the potential one-click, buy-and-rent strategy that they're pursuing? Do neighborhoods exist that you would suggest for investment, and why?
    * 

**File:** [San Fransisco Real Estate Market Analysis](/san_francisco_housing.ipynb)

## Contributors
Mykal Morton, Vicky Lee, Jay Wiley, Jeremy Pierce.
