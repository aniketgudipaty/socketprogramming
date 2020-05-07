import os
import numpy
from numpy import loadtxt
from numpy.random import seed
from keras.models import Sequential
from keras.layers import Dense
from keras.metrics import Precision , Recall
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
from tensorflow.random import set_seed
import random
import matplotlib.pyplot as plt

os.environ['PYTHONHASHSEED'] = str(0)
set_seed(0)
seed(0)
random.seed(0)

dataset = loadtxt('annthyroid.csv' , delimiter = ',')

train_size = int((7200*(0.7)))
X_train = dataset[0:train_size,0:6]
Y_train = dataset[0:train_size,6]
X_val = dataset[train_size:,0:6]
Y_val = dataset[train_size:,6]

model = Sequential()
model.add(Dense(30 , input_dim = 6, activation='relu'))
model.add(Dense(30 , activation= 'relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss= 'binary_crossentropy', optimizer= 'adam', metrics= ['accuracy',Precision(name='precision') , Recall(name='recall')])
model.fit(X_train, Y_train, epochs= 100, batch_size=10)

classes = model.predict_classes(X_val)
classes = classes[:,0]

print("Performance on Validation Set:")

acc = accuracy_score(Y_val , classes)
print('Accuracy : ' ,acc)

pre = precision_score(Y_val , classes)
print("Precision : ",pre)

rec = recall_score(Y_val , classes)
print("Recall : ",rec)

f = f1_score(Y_val , classes)
print("F1_score : " , f)

X_neg = numpy.ndarray(shape=(1,6))
X_pos = numpy.ndarray(shape=(1,6))
for i in range(train_size):
    if Y_train[i] == 0:
        X_neg = numpy.append(X_neg,numpy.resize(X_train[i,:],(1,6)),axis=0)
    else:
        X_pos = numpy.append(X_pos,numpy.resize(X_train[i,:],(1,6)),axis=0)

fig = plt.figure()
ax = fig.add_subplot()

neg = model.predict_proba(X_neg)
for i in range(len(neg)):
    neg[i] = neg[i]*100
plt.hist(neg,bins = 20,alpha = 0.5,label="Negative Cases")

pos = model.predict_proba(X_pos)
for i in range(len(pos)):
    pos[i] = pos[i]*100
plt.hist(pos,bins = 20,alpha = 0.5,label="Positive Cases")

plt.title("Performance on Training Set")
plt.yscale('log')
plt.xlabel('Anomaly Score')
plt.ylabel('Occurances')
ax.set_xlim(0,100)
ax.legend()

plt.show()
