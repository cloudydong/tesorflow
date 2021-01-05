import tensorflow as tf

from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 데이터 라벨링
categories = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, 3, input_shape=(32, 32, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Conv2D(64, 3, input_shape=(32, 32, 3), activation='relu'),
    tf.keras.layers.Conv2D(64, 3),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128)
score = model.evaluate(x_test, y_test)
# print(f' loss {score[0]}')
# print(f' accuracy {score[1]}')

model.save('./model/model')

prd = model.predict(x_test)
with PdfPages('./images/multipage.pdf') as pdf:
    for i, v in enumerate(prd):
        predict = v.argmax()
        y = y_test[i][0]
        x = x_test[i]
        if predict != y:
            plt.suptitle(f'predicted: {categories[predict]}, actual: {categories[y]}')
            plt.imshow(x)
            pdf.savefig()
            plt.close()

# model.load_weights()
