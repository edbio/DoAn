import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Lay du lieu mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# Normalize hinh anh tu [0,255] thanh [-0.5,0.5] 
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

# Lam phang truoc khi truyen vao Neural Network.
train_images = train_images.reshape((-1, 784))
test_images = test_images.reshape((-1, 784))

# Xay dung mo hinh su dung Sequential vi mang la cac lop tuyen tinh
model = Sequential([
  Dense(64, activation='relu', input_shape=(784,)),
  Dense(64, activation='relu'),
  Dense(10, activation='softmax'),
])

# Bien dich mo hinh
model.compile(
  optimizer='adam',
  loss='categorical_crossentropy',
  metrics=['accuracy'],
)

# Train mo hinh
model.fit(
  train_images,
  to_categorical(train_labels),
  epochs=5,
  batch_size=32,
)

# Danh gia mo hinh.
model.evaluate(
  test_images,
  to_categorical(test_labels)
)

# Luu mo hinh
model.save_weights('model.h5')


# Du doan 5 hinh anh dau tien
predictions = model.predict(test_images[:5])

# In ra mo hinh du doan
print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

# Kiem tra nhan chuan
print(test_labels[:5]) # [7, 2, 1, 0, 4]