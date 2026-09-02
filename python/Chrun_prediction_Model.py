import pandas as pd 
# pd.set_option("display.max_columns",None)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
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
# print(X_train.shape,"Trained In put features")
# print(X_test.shape,"Test In put features")
# print(y_train.shape,"Trianed out put feature")
# print(y_test.shape,"test out put feature")
model=LogisticRegression(max_iter=5000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
# print(y_pred)
accuracy=accuracy_score(y_test,y_pred)
conf_mat=confusion_matrix(y_test,y_pred)
# print(conf_mat)
clsf_r=classification_report(y_test,y_pred)
# print(clsf_r)
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

coefficients = coefficients.sort_values(
    by="Coefficient",
    ascending=True
)

# print(coefficients)
print(pd.crosstab(data["Contract"], data["Churn"], normalize="index")*100)