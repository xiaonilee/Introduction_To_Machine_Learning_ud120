

import pickle
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("./final_project_dataset.pkl", "rb"))

features_list = ["poi", "salary"]
data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import tree
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.3,
    random_state = 42)
    
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print(clf.score(features_test, labels_test))