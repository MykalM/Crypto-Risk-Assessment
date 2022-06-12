# README
## Background

**Smart exposure to digital currencies**, This application uses an interactive command line interface to collect investment information from the user; it then recomends a cryptocurrency portfolio based on risk levels, and by analyzing real-time data using API calls.  This Crypto porfolio analyzer is an innovative addition to the fintech industry. We want to offer optimized cryptocurrency porfolios to everyone, even those who lack the financial knowledge and understanding of cryptocurrencies. We plan to build additional features into this like the ability to link to cryptocurrency wallets, and buying/selling with a cryptocurrency trading bot using machine learning.


## Table of Contents
1. [Front-end Interface](#1-Front-end-Interface)

2. [Calculate and plot the average prices per square foot.](#2-calculate-and-plot-the-average-sale-prices-per-square-foot)

3. [Compare the average prices by neighborhood.](#3-compare-the-average-sale-prices-by-neighborhood)

4. [Build an interactive neighborhood map.](#4-build-an-interactive-neighborhood-map)

5. [Compose your data story.](#5-compose-your-data-story)

---

## 1. Front-end Interface

![1](./Images/Recording%202022-06-08%20at%2020.20.03.gif)

* Use the `groupby` function to group the data by year. 
* Aggregate the results by the `mean` of the groups.
* Use the `hvplot` function to plot the `housing_units_by_year` DataFrame as a bar chart. 
* Make the x-axis represent the `year` and the y-axis represent the `housing_units`.
* Style and format the line plot to ensure a professionally styled visualization.
    * What’s the overall trend in housing units over the period that you’re analyzing?
    
  

## 2. Calculate and Plot the Average Sale Prices per Square Foot

 ![2](./Images/Screen%20Shot%202022-06-09%20at%201.46.14%20PM.png))
* Group the data by year, and then average the results. 
* What’s the lowest gross rent that’s reported for the years that the DataFrame includes?
* Create a new DataFrame named `prices_square_foot_by_year` by filtering out the “housing_units” column.
* The new DataFrame should include the averages per year for only the sale price per square foot and the gross rent.
* Use hvPlot to plot the `prices_square_foot_by_year` DataFrame as a line plot.
* This single plot will include lines for both `sale_price_sqr_foot` and `gross_rent`.
* Style and format the line plot to ensure a professionally styled visualization.
    * Did any year experience a drop in the average sale price per square foot compared to the previous year?
        * If so, did the gross rent increase or decrease during that year?


## 3. Compare the Average Sale Prices by Neighborhood

* Create a new DataFrame that groups the original DataFrame by year and neighborhood. Aggregate the results by the `mean` of the groups.
* Filter out the “housing_units” column to create a DataFrame that includes only the `sale_price_sqr_foot` and `gross_rent` averages per year.
* Create an interactive line plot with hvPlot that visualizes both `sale_price_sqr_foot` and `gross_rent`. 
* Set the x-axis parameter to the year (`x="year"`). 
* Use the `groupby` parameter to create an interactive widget for `neighborhood`.
* Style and format the line plot to ensure a professionally styled visualization.
    * For the Anza Vista neighborhood, is the average sale price per square foot for 2016 more or less than the price that’s listed for 2012?
    ![3](./Images/Anza.png)

## 4. Build an Interactive Neighborhood Map

![4](./Images/geoviews_plot.png)

* Read the `neighborhood_coordinates.csv` file from the `Resources` folder into the notebook, and create a DataFrame named `neighborhood_locations_df`. 
* Be sure to set the `index_col` of the DataFrame as “Neighborhood”.
* Using the original `sfo_data_df` Dataframe, create a DataFrame named `all_neighborhood_info_df` that groups the data by neighborhood. 
* Aggregate the results by the `mean` of the group.
* Review the two code cells that concatenate the `neighborhood_locations_df` DataFrame with the `all_neighborhood_info_df` DataFrame. 
* Using hvPlot with GeoViews enabled, create a `points` plot for the `all_neighborhoods_df` DataFrame. 
* Use the interactive map to answer the following question: 
    * Which neighborhood has the highest gross rent, and which has the highest sale price per square foot?

## 5. Compose Your Data Story

* Based on the visualizations that you created, answer the following questions:
    * How does the trend in rental income growth compare to the trend in sales prices? Does this same trend hold true for all the neighborhoods across San Francisco?
    * What insights can you share with your company about the potential one-click, buy-and-rent strategy that they're pursuing? Do neighborhoods exist that you would suggest for investment, and why?
    * 

**File:** [San Fransisco Real Estate Market Analysis](/san_francisco_housing.ipynb)

## Contributors
Mykal Morton, Vicky Lee, Jay Wiley, Jeremy Pierce.
