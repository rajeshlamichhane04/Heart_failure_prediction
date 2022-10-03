#usual imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.feature_selection import SelectKBest,RFE, f_regression
from sklearn.preprocessing import MinMaxScaler

plt.rc('figure', figsize=(8, 6))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)

def plot_pie(train):
    #plot pie charrt
    plt.title("death due to heart diease")
    labels = ["death", "no death"]
    plt.pie([(train.death_event ==1).sum(),(train.death_event ==0).sum()],labels = labels, autopct= '%.0f%%', explode = [0.2,0])
    plt.show()


def plot_age(train):
    #plot count plot, age vs death event
    plt.rc('figure', figsize=(16, 6))
    sns.countplot(x= "age", data =train, hue = "death_event")
    plt.xticks(rotation = 90)
    plt.title("age vs death event")
    plt.show()


def run_age_t_test(train):
    #Set null hypothesis
     null_hyp = 'mean age of people with death event == mean age of people with no death event '
     print("null_hyp:", null_hyp)
     #set alternate hypothesis
     alt_hyp = 'mean age of people with death event != mean age of people with no death event '
     print("alternate_hyp: ", alt_hyp)
     alpha = 0.05
     #make subsample
     death_age = train[train.death_event ==1].age
     no_death_age = train[train.death_event == 0].age
     #run t test
     t,p = stats.ttest_ind(death_age, no_death_age )
     if p < alpha:
         print()
         print("reject null hypothesis" )
         print("we conclude ", alt_hyp)
     else:
         print("fail to reject null hypothesis")
         print("we conclude", null_hyp)


def plot_creatinine(train):
    plt.figure(figsize = (16,15))
    #sub plot distribution plot, death event vs creatinine phosphokinase
    plt.subplot(221)
    plt.title("enzyme creatinine_phosphokinase vs death event")
    sns.distplot(train[train.death_event == 0].creatinine_phosphokinase,hist = False, color = 'green', label = "no death")
    sns.distplot(train[train.death_event == 1].creatinine_phosphokinase, hist = False, color = "red", label = "death")
    plt.legend()

    plt.subplot(222)
    plt.title("serum creatinine vs death event")
    #sub plot distribution plot, deatth event vs serrum creatinine
    sns.distplot(train[train.death_event == 0].serum_creatinine,hist = False, color = 'green', label = "no death")
    sns.distplot(train[train.death_event == 1].serum_creatinine, hist = False, color = "red", label = "death")
    plt.legend()
    plt.show()


def select_kbest(X,y,k=4):
    #X = train.drop(columns = ["death_event"])
    #y = train.death_event
    #make the thing
    kbest = SelectKBest(f_regression, k=k)
    #fit the thing
    kbest.fit(X,y)
    features = X.columns[kbest.get_support()]
    return features



def get_baseline(y_train):
    #print value count of target
    print(y_train.value_counts())
    print()
    #getbaseline accuracy
    baseline_accuracy = (y_train == 0).mean()
    print('baseline accuracy is:', round(baseline_accuracy,4))


def scale_data(train,validate,test,columns):
    #make the scaler
    scaler = MinMaxScaler()
    #fit the scaler at train data only
    scaler.fit(train[columns])
    #tranforrm train, validate and test
    train_scaled = scaler.transform(train[columns])
    validate_scaled = scaler.transform(validate[columns])
    test_scaled = scaler.transform(test[columns])
    
    # Generate a list of the new column names with _scaled added on
    scaled_columns = [col+"_scaled" for col in columns]
    
    #concatenate with orginal train, validate and test
    scaled_train = pd.concat([train.reset_index(drop = True),pd.DataFrame(train_scaled,columns = scaled_columns)],axis = 1)
    scaled_validate = pd.concat([validate.reset_index(drop = True),pd.DataFrame(validate_scaled, columns = scaled_columns)], axis = 1)
    scaled_test= pd.concat([test.reset_index(drop = True),pd.DataFrame(test_scaled,columns = scaled_columns)],axis = 1)
    
    return scaled_train,scaled_validate,scaled_test


def plot_age_vs_time(train):
    #plot scatter plot, age, time vs death event
    sns.scatterplot(x='age', y='time', hue ='death_event', data = train)
    plt.ylabel("time (follow up period,in days)")
    plt.title("age, time vs death event")


def plot_ejection_fraction_vs_sex(train):
    #plot swarrm plot, sex, ejection fraction vs death event
    sns.swarmplot(x = "sex", y = "ejection_fraction", hue = "death_event", data = train)
    plt.xticks([0,1],["female", "male"])
    plt.title("ejection fraction vs sex")
    plt.show()

def plot_add_ailments(train):
    #plot histplot, aliments vs death event
    sns.histplot(x = "add_ailments", data = train, hue = "death_event", multiple="stack" , kde = True)
    plt.xlabel("combination of ailments")
    plt.title("aliments vs death events")
    plt.show()