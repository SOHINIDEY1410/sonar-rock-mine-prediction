\# SONAR Rock vs Mine Prediction API



\## Project Description



This project builds a \*\*Machine Learning model\*\* that predicts whether an object detected by SONAR signals is a \*\*Rock\*\* or a \*\*Mine\*\*.



The model is trained using the \*\*SONAR dataset\*\* and deployed using \*\*FastAPI\*\*, allowing predictions to be made through an API.



\---



\## Technologies Used



\* Python

\* NumPy

\* Scikit-learn

\* FastAPI

\* Uvicorn



\---



\## Project Structure



sonar-project

│

├── main.py

├── sonar\_model.sav

├── requirements.txt

├── train\_model.ipynb

└── README.md



\---



\## How the Model Works



1\. The dataset contains \*\*60 sonar signal values\*\*.

2\. A \*\*Logistic Regression model\*\* is trained using Scikit-learn.

3\. The trained model is saved using \*\*pickle\*\* as `sonar\_model.sav`.

4\. FastAPI loads the saved model and provides a \*\*prediction API endpoint\*\*.



\---



\## How to Run the Project



\### 1. Install dependencies



pip install -r requirements.txt



\### 2. Start the FastAPI server



uvicorn main:app --reload



\### 3. Open API documentation



http://127.0.0.1:8000/docs



\---



\## Prediction



Send \*\*60 sonar values\*\* to the `/predict` endpoint.



The API will return:



\* \*\*Rock\*\*

\* \*\*Mine\*\*



\---



\## Author



Sohini Dey



