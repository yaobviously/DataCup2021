# Data Cup 2021

This repository contains code and data related to the OHL's Data Cup 2021 competition. I wasn't able to submit my entry, but I did do an analysis several months later

Overview
I created three separate models to predict three outcomes relevant to hockey success: 1) The probability of a goal conditional on a shot; 2) The probability a pass will be completed; 3) The expected number of shots in the next ten events. In the case of the passing model I also computed 'passes completed over expectation' for the players in the dataset with large enough samples. 

Data
The data was provided by the OHL. It was in the standard hockey play-by-play format. I added several features for each model including the events n-steps back and forward, passing distance and angle, and other details like the interval between events. 

Approach
In each case I began by fitting either a simple linear classifier (proba goal, proba pass) or linear regressor. Afterwards I tuned the appropriate xgboost models on the same features. SHAP was used to iteratively assess feature importance. 

Evaluation
A confusion matrix and the receive response characteristic were chosen to evaluate the classification models. In both cases the gradient boosting trees significantly outperformed the linear classifier (see Notebooks). For the shots in the next ten events model I chose Mean Absolute Error and Poisson Deviance to assess model fit. 

Results
Summarize the results of your solution and highlight any key findings. Include any visualizations or tables that help to communicate your results.

Getting Started
Provide instructions on how to reproduce your results, including any dependencies or libraries needed. If applicable, provide a link to a demo or hosted version of your solution.

Contributing
Provide information on how others can contribute to your project, such as reporting issues or suggesting improvements. You can also outline any guidelines or requirements for contributions.
