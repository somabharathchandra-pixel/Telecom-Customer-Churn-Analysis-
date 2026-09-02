import pandas as pd 
# pd.set_option("display.max_columns",None)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
data=pd.read_csv("C:/Users/soma/OneDrive/Desktop/Churn Prediction Project/cleaned_churn_data.csv")
data["TotalCharges"] = data["TotalCharges"].fillna(0)
data = data.drop(
    ["Tenure_Group", "Monthly_Charges_Group"],
    axis=1
)
data["Churn"]=data["Churn"].map({"Yes":1,"No":0})
# print(data["Churn"].value_counts())
X=data.drop("Churn",axis=1)
X=X.drop("customerID",axis=1) # In put X featuers

X=pd.get_dummies(X,drop_first=True) # Converted the Categorical columns into Numerical
# print(X.isnull().sum())

X=X.astype(int) # if any bollean velus converted to integer
# print(X.dtypes)
y=data["Churn"] # Out Put feature 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(accuracy_score(y_test,y_pred))