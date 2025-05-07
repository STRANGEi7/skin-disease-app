import os
import sys
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
from tensorflow.keras.preprocessing import image # type: ignore

# Load the model (update the path to your model)
model = load_model('model/model.h5')
class_names =['Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis-like lesions',
                    'Dermatofibroma', 'Melanocytic nevi', 'Melanoma', 'Vascular lesions']
def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(64, 64))  # Change target size as per your model
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0   #normalize 
    img_array = np.expand_dims(img_array, axis=0)
    
    
     # 🔥 FLATTENING the image array to match model input shape
  #  img_array = img_array.reshape((1, -1))  # From (1, 224, 224, 3) to (1, 224*224*3)
    print("Model Input Shape:", model.input_shape)

    # Predict the disease
    prediction = model.predict(img_array)
    
    # Map prediction to disease name (this should match your model's output classes)
    # disease_name = np.argmax(prediction)
    disease_name = class_names[np.argmax(prediction)] 
    return disease_name
# # For manual testing
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python predict.py path_to_image.jpg")
#     else:
#         img_path = sys.argv[1]
#         disease, confidence = predict_disease(img_path)
#         print(f"Predicted: {disease} ")

    
# If script is run directly from command line
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python predict.py path_to_image.jpg")
#         sys.exit(1)

#     img_path = sys.argv[1]

    # if not os.path.exists(img_path):
    #     print(f"File not found: {img_path}")
    #     sys.exit(1)

    # result = predict_disease(img_path)
    # print("Predicted Disease:", result)
