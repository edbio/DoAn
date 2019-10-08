import numpy as np 
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras import losses
from keras import optimizers

# 1. Tao du lieu
X = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 
              2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# 2. Xay dung mo hinh 
model = Sequential()
model.add(Dense(1, input_shape=(1,)))
model.add(Activation('sigmoid'))

# 3. gradient descent optimizer va loss function 
sgd = optimizers.SGD(lr=0.05)
model.compile(loss=losses.binary_crossentropy, optimizer=sgd)

# 4. Train mo hinh 
model.fit(X, y, epochs=3000, batch_size=1)

[[[a],],[b,]]=model.get_weights()
print(a,b)
