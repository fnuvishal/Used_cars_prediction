# Final Project: Prediction of Price (Linear Regression Model using Python)

## Executive Summary

**Do you want to take your business to NEXT level?** It can be achieved by upgrading the business strategies with the help of innovative technologies. Determining appropriate price of the vehicle plays a crucial role in car brokerage. The growth of the organization depends on customer’s trust in the company. If it is not done correctly, it creates a bad impression about the company and affects the sales rate if the prices are fixed too high and causes significant losses when the prices are fixed below the mark.

The challenge is, how to predict the correct price for the vehicle. It is very much important to understand the market trends and customer needs, which helps to increase the sales rate. **How to predict the correct price?**

**Sit back and relax!** We have the best possible solution for you. As a vehicle brokerage company you should analyse the important factors to determine the vehicle price. Don't worry! We will do that for you. A machine learning technique is used to predict the price, a large dataset on vehicles are collected, cleaned and analysed. From the data analysis it is found that the price depends mostly on factors such as vehicle type, model, year of registration, kilometers and gearbox type. Several machine learning models are built, trained and tested. The Random Forest model shows the best accuracy(74%) for unseen data, among all other models. It is also useful for the companies which prefer to buy used vehicles for domestic purposes.

Now you are aware of the major factors which affect the price of the vehicle. It will greatly minimize your loss due to inappropriate price determination .

We love to collaborate with an esteemed organization like yours. We will help your customers to get a desired vehicle at an affordable and appropriate price.

**PRICE is what you pay, VALUE is what you get!**

### Purpose

- The aim of this project is to create a regression model based on the vehicle price Dataset. This model will predict the price of a vehicle.


### Problem Statement
- As the objective or purpose, we want to identify which features are the best for predicting the price of the vehicle.
- We have to create a regression model that will help us to predict the best vehicle price.
- We have received the data called autos.csv for this project. We have to split the data into train and test. The model will build based on the training dataset and test our model with the test dataset as unseen data.
- We have to clean the dataset first and fit the model into it to make our predictions.
- Based on the model and the prediction, we have to find what are some significant predictors that play a vital role in the project.

### Data Source
- [Used_cars](https://data.world/data-society/used-cars-data)

## How It was Carried out
### Data Cleaning and EDA
- The dataset contains 371528 rows and 20 columns
- We have started by generating a list of null values in each feature after the initial import into the DataFrame.
- It helps us to understand the data and gives a broad overview of which features have so many missing values.
- After that, we have checked all the datatypes of all columns and used .isnull() to give a rough sense of the distribution for each non-numeric feature.
- It helps us to understand if the data is nominal or ordinal.
- Then we have moved towards several visualizations of the data to check the outliers and treatment of missing values. All actions are given below
    - Dropped rows where the price is more than 40000
    - Dropped rows where the price is less than 10
    -  No missing value in the price or target column so no missing value treatment is applied.
    -  Dropped some not important columns such as name, monthOfRegistration, and lastSeen
- Based on that we have dropped several rows and columns that are not at all important. The final share of the data is 356769, 20 at the end of cleaning process.

### Bivariate Analysis
- Changed datatypes of columns wherever required.
- Dropped such columns that have high co-relation. Such columns are dateCrawled, Abtest, fuelType, Brand, nrOfPictures, postalCode,seller, offerType, notRepairedDamage and dateCreated.

### Feature Engineering
- Created one feature called power_km (powerPS/ kilometer).
- Removed powerPS column.
- Final dataset has 6 columns. Those are vehicleType, yearOfRegistration, gearbox, Model, Kilometer, price.

### Preprocessing and Modeling
Here, we have divided the target (Y) and actual data (x) from the cleaned/updated dataset.
- We have processed columns and applied LabelEncoder to fit and transform on features.
- Then I have converted features into dummies for expansion. Feature names are vehicleType, yearOfRegistration, gearbox, Model and Kilometer.
- We have finally moved towards the train and test split with (70% and 30% ratios).
- Finally, we move towards the regression model.

### Evaluation and Conceptual Understanding
It focused on the RMSE (Root Mean Square Error, the lower the better) for grading. Various model results are given below

### Performance Summary
|Model	|Testing RMSE| R2 Training| R2 Testing|
| --- | ---| --- | ---|
|Linear Regression | 4463.84 |0.5621 | 0.5582 |
|Ridge Regression | 4463.85 |0.5621 | 0.5582 |
| Lasso Regression | 4465.95 |0.5617 | 0.5578 |
| k-Nearest Neighbors | 3682.11 |0.6978 |0.6596 |
| Decision Tree | 3425.86 |0.8283 | 0.7398 |
| Bagging Decision Trees | 3296.04 |0.8215 | 0.7591 |
| Random Forest | 3277.08 |0.8243 | 0.7619 |
| AdaBoost | 4592.47 |0.5325 | 0.5324 |
| Gradient Boosting | 3441.97 |0.7403 | 0.7373 |


### Prediction of the test set
Due to the linear model is the best one, we have tested test data on that model. Based on that we have predicted the price of vehicles on that test data and shown the actual vs predicted graph in the notebook.

### Features to consider
- Price will increase through various factors such as vehicleType, yearOfRegistration, gearbox, Model and Kilometer.
- Price will decrease through none of the factors because there all factors have a positive impact to predict the vehicle price.

### Conclusion and Recommendations
 - The Random Forest regressor is found to be the best suitable model to predict the price of the vehicle.
 - It has Less RMSE and more accuracy than all other models comparatively.
 - As per the model of the car, it is predicting the best match of its price.
 - If the kilometer is high, then the price will be low,
 - If the gearbox is automatic, the vehicle price will between 10,000 to 40,000.
 - more recent the yearOfRegistration is , higher the price.
 - The SUV type vehicles are valued more at almost all conditions.
