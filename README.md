# Analyzing-public-companies-in-the-Life-Science-and-designing-an-investment-portfolio--Data-Scientist
The aim of this project is to predict whether the stock is in profit or loss by using today's price.
## Authors

- Langat Tito Kipkirui
- Poornima Devi K K
- Tanvi Mehta
- Joy Chakraborty
- Daphilarishisha Kharpuri
- Gunjan Sharma
- Santhosh Kumar M



## Content

1. Data Scrapping
2. Exploratory Data Analysis
3. Random Forest Classifier
4. Support Vector Machine Classifier
5. Deployment
6. Conclusion
## Data Collection
As per the project requirements, five Years of Data was collected from 1st Feb 2017 to 08th Feb 2022

[Link to Raw Data](https://finance.yahoo.com/)

The data was downloaded from Yahoo Finance.

Data include following columns:

All the files have the following columns: Date - in format: yy-mm-dd

- Date (Date of the stock)
- Open (Price of the stock at market open)
- High (Highest price reached in the day)
- Low (Lowest price reached in the day)
- Close (Price of the stock at market close)
- Adj Close (Adjusted close is the closing price after adjustments for all applicable splits and dividend distributions.)
- Volume

## EDA

In this EDA part we removed outliers and we have done visualization.

After removing outliers we got only 89929 rows instead of 108945 rows.
## Random Forest Classifier

Random Forest Classifier was trained and it got the accuracy of 87%
## Support Vector Machine Classifier 

Support Vector Machine Classifier was trained and it got the accuracy of 86%
## Model Deployement
Flask and Django used to deploy the Model

[Result Link](http://127.0.0.1:5000/)

If stock will be profit it will be show "Congragulations the stock will be in profit"

If stock will be loss it will be show "The stock will be in loss"
## Conclusion
- Conditions were the High value is higher than open value will lead to profit most of the times

- For further research and development work we must explore tools to incorporate rising and falling trends in legacy data and history of a particular stock's price.

- Random Forest Classifier may have limited applicability in a real world scenario.
