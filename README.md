#  Regression Model with Random Forest (Flask Deployment)

A machine learning project that builds a **Random Forest Regression Model** with **hyperparameter tuning**, serializes it using **Pickle**, and deploys it via a **Flask backend** for real-time predictions.

##  Features  
✅ **Hyperparameter tuning** for optimal model performance  
✅ **Pickle serialization** for efficient model storage and retrieval  
✅ **Flask API** for real-time predictions  
✅ **JSON-based API responses**  

##  Tech Stack  
- **Machine Learning:** Scikit-Learn, Random Forest  
- **Backend:** Flask (Python)  
- **Deployment:** Pickle, Flask-Restful  

##  Setup & Installation  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-username/random-forest-flask.git
   cd random-forest-flask
2. **Create a virtual environment (optional but recommended): **
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
   
4. **Train & Pickle the Model:**
     ```bash
      python train.py


5.  **Run the Flask API:**
     ```bash
      python app.py
