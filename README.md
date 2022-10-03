# Heartfaliure_prediction

# Project Goal
> - The goals of this project are the predict the factors the lead to death event of patient having heart failure symptoms, to produce a prediction model using ML algorithms and to offer recommendation to reduce such deah event

# Project Description
> - I will conduct an in depth analysis to his heart faliure data that I acquired from Kaggle. The data in Kaggle was based on a dataset of 299 patients with heart faliure collected in 2015 at Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015. I will used exploratory analysis followed by some statiscal testing to find some important factors leading to heartfaliure deaths and then apply classiifcation ML algorithms to make model that can predict the death event.

# Initial Questions
> - How likely is death due to heart failure?
> - How is age related?
> - Is there is any link age and time?
> - How does creatinine affect death event?
> - How does ejection fraction relate?
> - Does all combined ailemnts create higher chances of death event?

# Data Dictionary
Feature|Description
-------|------------
age |Age of the patient 
anaemia|Haemoglobin level of patient (Boolean)
creatinine_phosphokinase|Level of the CPK enzyme in the blood (mcg/L)
diabetes|If the patient has diabetes (Boolean)
ejection_fraction| Percentage of blood leaving the heart at each contraction
high_blood_pressure| If the patient has hypertension (Boolean)
platelets|Platelet count of blood (kiloplatelets/mL)
serum_creatinine| Level of serum creatinine in the blood (mg/dL)
serum_sodium|Level of serum sodium in the blood (mEq/L)
sex|Sex of the patient (Male = 1, Female =0)
smoking|If the patient smokes or not (Boolean)
time|Follow-up period (days)
DEATH_EVENT| If the patient deceased during the follow-up period (Boolean)

# Steps to Reproduce
> - To clone this repo, use this command in your terminal git clone https://github.com/rajeshlamichhane04/Heart_faliure_prediction
> - You will need the copy of data from Kaggle using https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data
> - You do not need Kaggle account

# The plan
> - I set up our initial questions during this phase. I made the outline of possible exploration techniques and hypothesis testing that we can use.

# Acquisition
I obtained this data from Kaggle via https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data. It is in downloaded csv format which you can save it locally in your repository.

# Preparation
I retrived a total of 299 rows with 13 columns.
> - column names were industry standard
> - changed a upper case column to lower case
> - there was no null values in data
> - as our dataset is small, I ignored the outliers
> - split data into train (56%), validate(24%), test(20%), stratified on death_event

# Exploration
I conducted an initial exploration of the data by examining correlations between each of the potential features and the target. I also combined aliments into new column to determine if all ailments combined gave me good information. I also employed Select_kbest to find my drivers of death  event.

# Modeling
I scaled our top features using MinMax Scaler. Baseline accuray was calucalated using the mode of our target. I used Decision Tree, Randon Forest and KNN to compare the accuracy of my train and validate and chose KNN. The baseline accuracy was 68% while model accuracy from KNN on train, validate, test were 85%,86% and 85% respectively.

# Prediction delivery
Using our top model, KNN, I able to predict the on our data.







 









