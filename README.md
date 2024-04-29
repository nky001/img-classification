
# Image Classification Project

## Overview

This project focuses on image classification using OpenCV for face and eye detection, and machine learning algorithms for classification tasks. The project utilizes Haar cascades for face and eye detection, and various machine learning models for classification.

## Dependencies

- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nky001/img-classification.git
   cd img-classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have Python and the required libraries installed.
2. Run the image classification script:
   ```bash
   python image_classification.py
   ```

## Components

### Face and Eye Detection

The project uses Haar cascades for face and eye detection:

```python
import cv2

face_cascade = cv2.CascadeClassifier("server/opencv/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("server/opencv/haarcascades/haarcascade_eye.xml")
```

### Machine Learning Models

The project employs various machine learning models for classification, including:

- Support Vector Machine (SVM)
- Random Forest Classifier
- Logistic Regression

```python
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
```


## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand upon this template to better fit your project's specific details and requirements! Let me know if there's anything else you'd like to include or if you have any specific preferences.