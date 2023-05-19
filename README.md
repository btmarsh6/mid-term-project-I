# Mid-Term Project
This repository cointains all the information you need to work on the Mid-Term project.

## Hello and Welcome!!!

The goal is to predict arrival delays of commercial flights. Often, there isn't much airlines can do to avoid the delays, therefore, they play an important role in both profits and loss of the airlines. It is critical for airlines to estimate flight delays as accurate as possible because the results can be applied to both, improvements in customer satisfaction and income of airline agencies.

### Files

- **exploratory_analysis.ipynb**: this file contains 10 questions we need to answer during the data exploration phase. They will help us to understand the data and become familiar with different variables.
- **modeling.ipynb**: this file contains instructions for modeling part of the project. We recommend to split modeling tasks into more notebooks.
- **data_description.md**: when you need to look for any information regarding specific attributes in the data this is the file to look in.
- **sample_submission.csv**: this file is the example of how the submission of the results should look like.

### Data

We will be working with data from air travel industry. We will have four separate tables:

1. **flights**: The departure and arrival information about flights in US in years 2018 and 2019.
2. **fuel_comsumption**: The fuel comsumption of different airlines from years 2015-2019 aggregated per month.
3. **passengers**: The passenger totals on different routes from years 2015-2019 aggregated per month.
5. **flights_test**: The departure and arrival information about flights in US in January 2020. This table will be used for evaluation. For submission, we are required to predict delays on flights from first 7 days of 2020 (1st of January - 7th of January). We can find sample submission in file _sample_submission.csv_

The data are stored in the Postgres database. You can see the information about the hostname and credentials [in Compass](https://data.compass.lighthouselabs.ca/23284197-327b-4c82-84fa-f220a40a7d1a). 


### Presentation Guidelines

The main goal of this presentation is to prepare you for your **Demo Day** at the end of the bootcamp where your time will be capped. Therefore, it's important to keep the duration of the presentation to **max 5 minutes** (number of slides doesn't necessarily determine the duration of the presentation). Focus on explaining what you did, how you approached the problem, what you achieved, and, if appropriate, suggest what else could be done. Don't speak to every single task and step there is, focus more on the highlights and interesting findings instead. If you struggled with something, feel free to mention it, but do not undermine your work by highlighting that part.

1. Spend **1 min** on project flow structure.
    Which steps does your project have?
2. Spend **1 min** on showing insights and relationships you found in the data during exploratory data analysis.
3. Results (**1 min**):
    - what modeling and sampling techniques did you use?
    - evaluation metrics
4. **1 min** on Feature Importance
    - mention interesting features you have created
    - what are the most important features?
5. Explain the biggest challenges in **1 min**.
    - what would you do if you have a bit more time?


### Submission Guidelines

1. Share the link to your project repository through Compass.
2. The file with the same format as _sample_submission.csv_,  named **submission.csv** , that contains the predictions of delays for the first week of the year 2020 should be included in the repository as well.


### How to Start

You should spend some time with the datasets on your own. Try to look for interesting relationships and information inside the tables. Once you are familiar with the data and information in there you can move on to the EDA tasks from us that will further help you to get familiar with the datasets. Afterward, you can move onto the data preparation and modeling steps. Make sure you have enough time to prepare you slides and presentation at the end.


### Process

1. Import the data sets from the Postgres DB
2. Data Cleaning and EDA
3. Feature Engineering Discussion
4. Sample Data
5. Encode Categorical Variables
6. Train/Test Split
7. Add Engineered Features
8. Scale/Normalize Data
9. Train and Evaluate Model (repeated for various model types)
10. Predictions Based on Best Model

### Feature Engineering
After an initial exploration of the data, we discussed other possible features we could engineer from the different datasets. We considered what sorts of things could potentially lead to flight delays and created several additional features to use in our modeling:
* **Average Monthly Passengers** - the average number of passengers each month on a given route.
    Our hypothesis: Flights along popular routes with more passengers may have more delays .
* **Average Monthly Fuel** - the average amount of fuel each carrier consumes each month. We calculated both the quantity in gallons and cost.
    Our hypothesis: There may be a correlation because airlines sometimes attempt to make up for delays by flying faster, hence using more fuel.
* **Average Taxi Times** - Calculated by hour, the average amount of time planes spend taxiing along the tarmac. We calculated both departure and arrival taxi times.
    Our hypothesis: Flights at times with more traffic spend more time between the gate and the air, leading to more delays.
* **Average Carrier Arrival Delay** - Calculated the average arrival delay for each operating carrier.
    Our hypothesis: Some delays are caused by staffing shortages, overbooking, or other operational issues. Airlines that have a history of longer delays will continue to have longer delays.

To ensure the integrity of our validation process, these features were added in after the train/test split. Average taxi times and delays were calculated just based on the training dataset, then mapped to the test set based on scheduled flight times. The passenger and fuel averages were calculated from separate datasets and therefore were not impacted by the train/test split. 

### Sampling and Model Building
Because of the large size of the flights dataset (over 15 million observations) and the limits of our resources, we were only able to work with a small fraction of the data. Our models were train on random samples of only a few hundred thousand rows.

Once we had our sample data prepared, we each selected a handful of different models to train and compare. The results of those models are below.

### Results
| Modeler | Model | RMSE | R^2 Score |
| ------- | ----- | ---- | --------- |
| Ben     | RidgeCV| 49.16 | .014    |
| Ben     | XGBoost| 50.99 | -.061   |
| Ben     | AdaBoost| 51.59 | -.087  |
| Ben     | RandomForest| 50.91 | -.058  |
| Ben     | ElasticNet| 49.13 | .014    |
| Nasir   | Linear Reg| 50.75 | .064 |
| Nasir   | SVM | 49.1 | .12 |
| Nasir   | AdaBoost | 149.1 | -9.33 |

### Challenges
The biggest challenge with this project was dealing with our limited computing resources. The enormous file size of the original data set meant that it took a long time to export from the SQL database and then import into our notebooks. We tried rerunning things, chopping our samples down to smaller and smaller sizes until the operations were manageable.

As a result, our models are all built on a small subset of the data. They would likely be more accurate if we were able to train them using significantly larger datasets.

Our models also do not include weather data. This is a major factor in flight delays, but difficult to predict accurately a week in advance, so we excluded it from our feature engineering.