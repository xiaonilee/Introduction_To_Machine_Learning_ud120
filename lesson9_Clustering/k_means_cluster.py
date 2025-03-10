#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("./")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("./final_project/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
pred = kmeans.fit_predict(finance_features)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")


# Now rerun clustering using 3 features
### The input features we want to use 
### Can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)

for f1, f2, _ in finance_features:
    plt.scatter(f1, f2)
plt.savefig('13_K-MeansClustering2a.png')
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
pred = kmeans.fit_predict(finance_features)

try:
    Draw(pred, finance_features, poi, mark_poi=False, name="13_K-MeansClustering2b.png", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("No predictions object named pred found, no clusters to plot")


stocks = []
for key, value in data_dict.items():
    if value['exercised_stock_options'] != 'NaN':
        stocks.append(value['exercised_stock_options'])

print(min(stocks), max(stocks))


stocks = []
for key, value in data_dict.items():
    if value['salary'] != 'NaN':
        stocks.append(value['salary'])

print(min(stocks), max(stocks))



from sklearn.preprocessing import MinMaxScaler

salary = []
ex_stock = []

for users in data_dict:
    val = data_dict[users]["salary"]
    if val == 'NaN':
        continue
    salary.append(float(val))
    val = data_dict[users]["exercised_stock_options"]
    if val == 'NaN':
        continue
    ex_stock.append(float(val))
    
salary = [min(salary), 200000.0, max(salary)]
ex_stock = [min(ex_stock), 1000000.0, max(ex_stock)]

print('Salary: {}'.format(salary))
print('Exercised stock options: {}'.format(ex_stock))

salary = numpy.array([[e] for e in salary])
ex_stock = numpy.array([[e] for e in ex_stock])

scaler_salary = MinMaxScaler()
scaler_stock = MinMaxScaler()

rescaled_salary = scaler_salary.fit_transform(salary)
rescaled_stock = scaler_salary.fit_transform(ex_stock)

print('Rescaled salary: {}'.format(rescaled_salary))
print('Rescaled exercised stock options: {}'.format(rescaled_stock))