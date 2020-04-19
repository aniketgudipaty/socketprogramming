from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.metrics import Precision , Recall
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score

dataset = loadtxt('annthyroid.csv' , delimiter = ',')

train_size = int((7200*(0.7)))
X_test = dataset[0:train_size,0:6]
Y_test = dataset[0:train_size,6]
X_val = dataset[train_size:,0:6]
Y_val = dataset[train_size:,6]

model = Sequential()
model.add(Dense(90 , input_dim = 6, activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss= 'binary_crossentropy', optimizer= 'adam', metrics= ['accuracy',Precision(name='precision') , Recall(name='recall')])
model.fit(X_test, Y_test, epochs= 150, batch_size=10)

classes = model.predict_classes(X_val)
classes = classes[:,0]

acc = accuracy_score(Y_val , classes)
print('Accuracy : ' ,acc)

pre = precision_score(Y_val , classes)
print("Precision : ",pre)

rec = recall_score(Y_val , classes)
print("Recall : ",rec)

f = f1_score(Y_val , classes)
print("F1_score : " , f)
