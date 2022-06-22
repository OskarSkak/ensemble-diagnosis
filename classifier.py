from PIL import Image
from matplotlib import pyplot as plt
from tensorflow import keras
import numpy as np
from tensorflow.keras.utils import to_categorical
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2800)])

class Classifier:
    def __init__(self) -> None:
        self.load_ISIC_classifiers()
        self.load_rad_classifier()


    def load_ISIC_classifiers(self):
        self.isic_1 = keras.models.load_model('./prot_models/derm/InceptionResNetV2')
        self.isic_2 = keras.models.load_model('./prot_models/derm/ResNet152V2')
        self.isic_3 = keras.models.load_model('./prot_models/derm/Xception')
    

    def load_rad_classifier(self):
        self.rad = keras.models.load_model('./prot_models/rad/Xception')
    

    def prepare_img(self, img, x=100, y=100):
        #Make img conform to training data
        img = Image.open(img)
        
        rezised_img = img.resize((x, y))

        #Transform to legal numpy array
        data = np.asarray(rezised_img)
        # extra_dim = []
        # extra_dim.append(data)
        data = np.expand_dims(data, axis=0)
        # un_norm_data = np.array(data)
        data = data.astype('float32')
        normalized_data = data / 255.0
        return normalized_data
    

    def prepare_img_rad(self, img, x=100, y=100):
        img = Image.open(img)
        rezised_img = img.resize((x, y))
        data = np.asarray(rezised_img)
        if data.shape == (x, y):
            d3 = np.stack((data,)*3, axis=-1)
            d3 = d3[np.newaxis, ...]

        d3 = d3.astype('float32')
        normalized_data = d3/255.0
        return normalized_data
    

    def classify_image(self, img, model, x=100, y=100) -> int:
        normalized_data = self.prepare_img(img, x, y)

        num_class = model.predict(normalized_data)

        return num_class
    

    def classify_rad(self, img):
        normalized_data = self.prepare_img_rad(img, 100, 100)
        result = self.rad.predict(normalized_data)
        num_class = result.argmax(axis=-1)[0]
        prob = np.max(result)*100
        return num_class, prob
    

    def classify_ISIC(self, img) -> int:
        probs_1 = self.classify_image(img, self.isic_1, x=150, y=250)
        probs_2 = self.classify_image(img, self.isic_2, x=150, y=250)
        probs_3 = self.classify_image(img, self.isic_3, x=150, y=250)
        averages = np.mean(np.array([probs_1, probs_2, probs_3]), axis=0)
        prob = np.max(averages)*100
        return averages.argmax(axis=-1)[0], prob


    def lime(self, img, name):
        import lime
        from lime import lime_image
        explainer = lime_image.LimeImageExplainer()
        from skimage.segmentation import mark_boundaries

        explanation = explainer.explain_instance(self.prepare_img(img, 150, 250), self.isic_1.predict, top_labels=5, hide_color=0, num_samples=2000)
        temp, mask = explanation.get_image_and_mask(explanation.top_labels[0], positive_only=True, num_features=5, hide_rest=False)

        plt.imshow(mark_boundaries(temp, mask))
        path = f'./images/LIME{name}'
        plt.savefig(path)
        path += '.png'
        return path
    
    def score_function_cov(output):
        return (output[0][1])


    def smooth_saliency(self, img, name):
        from tf_keras_vis.utils.model_modifiers import ReplaceToLinear
        replace2linear = ReplaceToLinear()
        from tensorflow.keras import backend as K
        from tf_keras_vis.saliency import Saliency

        saliency = Saliency(self.isic_1,
                            model_modifier=replace2linear,
                            clone=True)
        X = np.asanyarray([self.prepare_img(img)])
        saliency_map = saliency(self.score_function_cov, X, smooth_samples=20, smooth_noise=0.3)
        plt.imshow(saliency_map[0], cmap='jet')
        path = f'./images/SALIENCY{name}.png'
        plt.savefig(path)
        return path
