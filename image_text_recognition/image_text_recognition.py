import easyocr
import os
import logging
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import re

# Configure logging to log to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='image_text_recognition.log', 
    filemode='a'  
)

class ImageTextRecognizer:
    def __init__(self, lang='en'):
        self.reader = easyocr.Reader([lang], gpu=False)
        logging.info(f"Initialized EasyOCR with language: {lang}")

    def preprocess_image(self, image_path, resize=None, enhance_contrast=1.5, sharpen=True):
        logging.info(f"Preprocessing image: {image_path}")
        try:
            with Image.open(image_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                if resize:
                    img = img.resize(resize)
                
                if enhance_contrast != 1.0:
                    enhancer = ImageEnhance.Contrast(img)
                    img = enhancer.enhance(enhance_contrast)

                if sharpen:
                    img = img.filter(ImageFilter.SHARPEN)

                return np.array(img)
        except Exception as e:
            logging.error(f"Error preprocessing image: {str(e)}")
            
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Unable to open image: {image_path}")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return img

    def detect_text(self, image):
        logging.info("Detecting text in the image")
        result = self.reader.readtext(image)
        return result

    def visualize_detection(self, image, detections):
        output = image.copy()
        for detection in detections:
            bbox, text, _ = detection
            top_left = tuple(map(int, bbox[0]))
            bottom_right = tuple(map(int, bbox[2]))
            cv2.rectangle(output, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(output, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        return output

    def extract_alphanumeric(self, detections):
        logging.info("Extracting alphanumeric text")
        alphanumeric_results = []
        for detection in detections:
            bbox, text, prob = detection
            alphanumeric_text = re.sub(r'[^a-zA-Z0-9]', '', text)
            if alphanumeric_text:
                alphanumeric_results.append((bbox, alphanumeric_text, prob))
        return alphanumeric_results

    def post_process(self, detections, min_confidence=0.5, min_length=2):
        logging.info("Post-processing detected text")
        processed_results = []
        for detection in detections:
            bbox, text, prob = detection
            if prob >= min_confidence and len(text) >= min_length:
                processed_results.append((bbox, text, prob))
        return processed_results

    def recognize_text(self, image_path):
        if not os.path.exists(image_path):
            logging.error(f"Image file not found: {image_path}")
            return []

        try:
            preprocessed_image = self.preprocess_image(image_path)

            detections = self.detect_text(preprocessed_image)

            alphanumeric_results = self.extract_alphanumeric(detections)

            final_results = self.post_process(alphanumeric_results)
            
            logging.info(f"Recognized text: {final_results}")
            return final_results
        except Exception as e:
            logging.error(f"Error recognizing text: {str(e)}")
            return []

def main():
    recognizer = ImageTextRecognizer()
    image_path = "test/1.jpg"
    text_results = recognizer.recognize_text(image_path)
    
    if text_results:
        image = cv2.imread(image_path)
        visualized_image = recognizer.visualize_detection(image, text_results)
        cv2.imwrite("output.jpg", visualized_image)
        
        for (bbox, text, prob) in text_results:
            print(f"Text: {text}, Probability: {prob}")
    else:
        print("No text was recognized in the image.")

if __name__ == "__main__":
    main()
