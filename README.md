# OCR Text Recognition Project

This project implements Optical Character Recognition (OCR) using `easyocr` and integrates data augmentation techniques for image preprocessing, model evaluation, and potential fine-tuning (though note that EasyOCR does not support training out-of-the-box).

## Project Features
- **Text Recognition:** Detects text from images using EasyOCR.
- **Model Evaluation:** Provides evaluation metrics such as accuracy, precision, recall, and F1-score.

---

## Getting Started

### Prerequisites
Before starting, ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)

### File Structure
```
itr_ml/
│
├── image_text_recognition/
│   ├── __init__.py
│   ├── generate.py              # Generates Testing and Training images
│   ├── evaluate.py              # Evaluates model accuracy using test dataset
│   └── image_text_recognizer.py # Handles text recognition and image preprocessing
│
├── train_images/                # Folder containing training images
├── test_images/                 # Folder containing test images
├── requirements.txt             # Required Python packages
├── setup.py                     # Setup configuration file
└── README.md                    # This file
```

### Clone the Repository
To clone the project repository, run:

```bash
git clone https://github.com/AJAmit17/ITR_ML.git
cd itr_ml
```

### Set up Virtual Environment

1. **Create the virtual environment**:
   - On **Windows**:
     ```bash
     python -m venv venv
     ```
   - On **macOS/Linux**:
     ```bash
     python3 -m venv venv
     ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Project

### Setup the Project
First, run the `setup.py` file to ensure the environment is configured correctly:

```bash
python setup.py sdist bdist_wheel
pip install .
```

This will install any required modules and set up the project environment.

### Running OCR Text Recognition

1. **Recognizing text from an image**:
   To run the `image_text_recognition` script that recognizes text from a specific image, execute:

   ```bash
   image_text_recognition test/1.jpg
   ```

2. **Generate Results**:
   To generate text recognition results and process images, you can run:

   ```bash
   python image_text_recognition/generate.py
   ```

   This will process images and generate the recognized text as output.

3. **Evaluating the Model**:
   To evaluate the OCR model against a ground truth dataset:

   ```bash
   python image_text_recognition/evaluate.py
   ```

   The evaluation script will calculate metrics like accuracy, precision, recall, and F1-score based on test images and ground truth data.

---
