import tensorflow as tf

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 데이터 라벨링
categories = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

model = tf.keras.models.load_model('./model/model')

prd = model.predict(x_test)

with PdfPages('./images/multipage.pdf') as pdf:
    for i, v in enumerate(prd):
        predict = v.argmax()
        y = y_test[i][0]
        x = x_test[i]
        if predict != y:
            fig, ax = plt.subplots(nrows=2, ncols=2)
            for j, axi in enumerate(ax.flat):
                axi.set_title(f'predicted: {categories[predict]}, actual: {categories[y]}')
                axi.imshow(x)
            pdf.savefig()
            plt.close()
