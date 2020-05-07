from numpy import loadtxt
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = loadtxt('annthyroid.csv' , delimiter = ',')
X_train, X_val , Y_train , Y_val = train_test_split(dataset[:,0:6],dataset[:,6], test_size = 0.3 , random_state= 1)

tree_clf = DecisionTreeClassifier(max_depth=10)
tree_clf.fit(X_train, Y_train)
print(tree_clf.classes_)
print("Depth of Decision Tree:",tree_clf.get_depth())

print("Performance on Training Set:")
train_predictions = tree_clf.predict(X_train)
print("Accuracy : ",accuracy_score(Y_train,train_predictions))
print("Precision : ",precision_score(Y_train,train_predictions))
print("Recall : ",recall_score(Y_train, train_predictions))
print("F1_score : ",f1_score(Y_train,train_predictions))

print("\nPerformance on Validation Set:")
predictions = tree_clf.predict(X_val)
print('Accuracy : ' ,accuracy_score(Y_val , predictions))
print("Precision : ",precision_score(Y_val , predictions))
print("Recall : ",recall_score(Y_val , predictions))
print("F1_score : " , f1_score(Y_val , predictions))

pos = []
neg = []

for i in range(len(Y_train)):
    if Y_train[i] == 1:
        pos.append(i)

    else:
        neg.append(i)

x_hist = tree_clf.predict_proba(X_train)

fig = plt.figure()
ax = fig.add_subplot()
plt.hist(x_hist[neg,1],bins = 20,alpha = 0.5 , label="Negetive")
plt.hist(x_hist[pos,1],bins = 20,alpha = 0.5 , label="Positive")
plt.title("Performance on Training Set")
plt.yscale('log')
plt.xlabel('Anomaly Score')
plt.ylabel('Occurances')
ax.set_xlim(0,1)
ax.legend()

plt.show()