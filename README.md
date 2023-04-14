# Data Cup 2021

This repository contains code and data related to the OHL's Data Cup 2021 competition. I wasn't able to submit my entry, but I did do an analysis several months later while completing the Lambda/BloomTech Data Science program.

# Overview
I created three separate models to predict three outcomes relevant to hockey success: 1) The probability of a goal conditional on a shot; 2) The probability of a pass completion; 3) The expected number of shots in the next ten events. In the case of the passing model I also computed 'passes completed over expectation' for OHL players with large enough samples. 

# Data
The OHL provided the data in the standard hockey play-by-play format. To augment the data, I engineered additional features such as events n-steps back and forward, passing distance and angle, and the time interval between events.

# Approach
In each case I began by fitting either a simple linear classifier (proba goal, proba pass) or linear regressor. Afterwards I tuned the appropriate xgboost models on the same features. SHAP was used to iteratively assess feature importance. 

# Evaluation
To evaluate the classification models, I used a confusion matrix and the receiver response characteristic. The gradient boosting tree outperformed the linear classifier significantly in both cases, as shown in the notebooks.

For the shots in the next ten events model, I used Mean Absolute Error and Poisson Deviance to assess model fit. 

# Results
All of the models performed well and yielded results consistent with what a hockey fan might expect. For instance, shots in front of the net were found to be most likely to result in a goal, and passes towards one's own net that weren't across the center of the ice were most likely to be completed. Additionally, the expected number of shots in the next 10 events increased substantially upon entering the opposing team's zone.

My models compared favorably with those of several contest finalist's.  
