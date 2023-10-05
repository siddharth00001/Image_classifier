import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class Classifier:
    def __init__(self,filename):
        self.filename = filename
    
    def predict_class(self):
        model = load_model(os.path.join("model","classifier.h5"))
        image_file = self.filename
        # test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.load_img(image_file, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        if result[0] == 1:
            prediction = 'dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]
