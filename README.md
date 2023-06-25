# Hospital Readmission Prediction using Random Forest 🩺

![image](https://github.com/keerthikkn/Hospital_Readmission_Prediction/assets/42544473/69bd4333-f5bb-4740-9b77-11fa860eec1d)

This repository contains a machine learning model trained on healthcare data to predict hospital readmission. The goal of the model is to predict whether a patient will be readmitted to the hospital within a certain time period after discharge.

The model utilizes the Random Forest algorithm, which is an ensemble learning method that combines multiple decision trees to make predictions. Random Forest is a popular choice for classification tasks due to its ability to handle complex relationships and avoid overfitting.

## Dataset 📂

The dataset used for training and evaluation contains various features related to patients' demographics, medical history, and treatment details. Each record in the dataset represents a patient's information along with a binary label indicating whether they were readmitted to the hospital or not.

### EDA 📊

![image](https://github.com/keerthikkn/Hospital_Readmission_Prediction/assets/42544473/e358449b-8ae2-400b-b096-7148a40aa3dc)
![image](https://github.com/keerthikkn/Hospital_Readmission_Prediction/assets/42544473/938182b5-2a4e-473d-987d-11a2b32942c2)


## Model Architecture

The Random Forest model is composed of a collection of decision trees. Each decision tree is built using a subset of the features and data samples. The final prediction is made by aggregating the predictions of all the individual trees.

The model can handle both categorical and numerical features. For categorical features, appropriate encoding techniques such as one-hot encoding or label encoding are applied.

## Model Training 🛰️

The model training process involves the following steps:

1. Data preprocessing: The dataset is preprocessed by handling missing values, encoding categorical features, and scaling numerical features as required.

2. Splitting the dataset: The dataset is split into training and testing sets to evaluate the model's performance on unseen data. A common split is 80% for training and 20% for testing.

3. Model initialization: The Random Forest classifier is initialized with hyperparameters such as the number of trees, maximum tree depth, and feature sampling strategy.

4. Model training: The Random Forest model is trained on the training set using the `fit` method. This process involves growing multiple decision trees based on different subsets of the data.

5. Model evaluation: The trained model is evaluated on the testing set using various evaluation metrics such as accuracy, precision, recall, and F1-score.

## Model Usage

To use the trained model for hospital readmission prediction, follow these steps:

1. Install the required dependencies mentioned in the `requirements.txt` file.

2. Load the trained model using the provided file or by training the model from scratch.

3. Preprocess the input data to match the required format, including handling missing values and encoding categorical features.

4. Feed the preprocessed data to the model and obtain the predicted readmission labels.

An example usage code snippet is provided in the repository to guide you through the process.

## Repository Contents

- `readmission_prediction.ipynb`: Contains the implementation of the Random Forest model architecture, training, and evaluation procedures.
- `requirements.txt`: Lists the required dependencies for running the code.
- `model.pkl`: Pretrained model file in pickle format.
- `train.csv` : training dataset.
- `README.md` : description and procedure about the repository. 

## Conclusion 💡

![image](https://github.com/keerthikkn/Hospital_Readmission_Prediction/assets/42544473/5f567711-ba57-435b-826f-3881bd33dbcf)


The Random Forest model showcased in this repository enables hospital readmission prediction based on patient information. You can use this model for readmission risk assessment or as a starting point for further research and development in the healthcare domain.

Please refer to the original source or consult the documentation for more detailed information about the implementation and usage of the model.
