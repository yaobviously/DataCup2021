# Data Cup 2021

This repository contains code and data related to the OHL's Data Cup 2021 competition. I wasn't able to submit my entry, but I did do an analysis several months later while completing the Lambda/BloomTech Data Science program.

# Overview
I created three separate models to predict three outcomes relevant to hockey success: 1) The probability of a goal conditional on a shot; 2) The probability of a pass completion; 3) The expected number of shots in the next ten events. In the case of the passing model I also computed 'passes completed over expectation' for OHL players with large enough samples. 

# Data
The data was provided by the OHL. It was in the standard hockey play-by-play format. I added several features for each model including the events n-steps back and forward, passing distance and angle, and other details like the interval between events. 

# Approach
In each case I began by fitting either a simple linear classifier (proba goal, proba pass) or linear regressor. Afterwards I tuned the appropriate xgboost models on the same features. SHAP was used to iteratively assess feature importance. 

# Evaluation
A confusion matrix and the receiver response characteristic were chosen to evaluate the classification models.  In both cases the gradient boosting tree significantly outperformed the linear classifier (see Notebooks). For the shots in the next ten events model I chose Mean Absolute Error and Poisson Deviance to assess model fit. 

# Results
All of the models performed well and were in agreement with what a hockey fan might expect. The shots most likely to go in are in front of the net, the passes most likely to be completed are passes towards your own net that aren't across the center of the ice, and the expected number of shots in the next 10 events increases dramatically on a zone entry. Comparing my result with conteset submissions, I was able to achieve predictive accuracy for the goal model that was comparable to a finalist's entry.
