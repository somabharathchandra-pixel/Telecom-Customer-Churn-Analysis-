import pandas as pd 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.set_option('display.max_rows', None)      # Show all rows
# pd.set_option('display.max_columns', None)   # Show all columns
# pd.set_option('display.width', None)         # Auto-adjust width
# pd.set_option('display.max_colwidth', None)  # Show full column content
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/soma/OneDrive/Desktop/Churn Prediction Project/Telco_Customer_Churn_Dataset  (3).csv")
# print(pd.isnull(data["customerID"]),)
# print(data.columns)
data["InternetService"]=data["InternetService"].replace("No","No InternetService")

# print(pd.Shape(data))
# data=pd.DataFrame(data)
# print(df.shape(data))
# print(data.shape)
# print(data.info())
# print(data.isnull().sum())
# print(data["customerID"].duplicated().sum())
# print(data.columns)
# print(data.to_records)
# print(data.nunique())
# print(f"{data["PhoneService"],data["customerID"]}")
data["MultipleLines"]=data["MultipleLines"].replace("No phone service","No")
# print(data["PhoneService"])

data["OnlineSecurity"]=data["OnlineSecurity"].replace("No internet service","No")
# print(data["OnlineSecurity"].unique())
data["OnlineBackup"]=data["OnlineBackup"].replace("No internet service","No")
# print(data["OnlineBackup"].unique())
# print(data.duplicated().sum())
# print(data.describe())
# print(data.isnull().sum())
# print(data["MultipleLines"].duplicated().sum())

data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)

data["TotalCharges"]=data["TotalCharges"].astype("float")
# print(data["TotalCharges"].describe())
# print(data["TotalCharges"].median())
# print(data[data["tenure"]==0])
data["SeniorCitizen"]=data["SeniorCitizen"].replace({0:"No",1:"Yes"})
# print(data["Churn"].value_counts())  # The number of people leaving the service and number of people need the service 
# print(data[data["Churn"]=="Yes"].shape[0])
# print(data[(data["Churn"]=="Yes")&(data["gender"]=="Male")].shape[0])
# print(data[(data["Churn"]=="Yes")& (data["gender"]=="Female")].shape[0])
senior_citzen_male=(data[(data["Churn"]=="Yes") & (data["gender"]=="Male")&(data["SeniorCitizen"]=="Yes")].shape[0])
# print(senior_citzen_male)
senior_citzen_Female=data[(data["Churn"]=="Yes")&(data["SeniorCitizen"]=="Yes")&(data["gender"]=="Female")].shape[0]
# print(senior_citzen_Female)
partner=data[(data["Partner"]=="Yes")&(data["gender"]=="Female")&(data["SeniorCitizen"]=="Yes")].shape[0]
# print(partner)/
# print(data["InternetService"])

churn_Yes=data[data["Churn"]=="Yes"].shape[0]
churn_No=data[data["Churn"]=="No"].shape[0]

# print(churn)
# churn_rate=(churn/data.shape[0])*100


Churn_count=data["Churn"].value_counts()
# print(Churn_count)
# churn_rate=data["Churn"].value_counts(normalize=True)*100  #here it caluculates percentage of staying and leaving 
# print(churn_rate)
# plt.figure(figsize=(5,4))
# 
# plt.pie(Churn_count.values,labels=Churn_count.index,  autopct="%1.1f%%") # index tells have the unique values and the values no of unique values
# and autopct tells 1.1f show the  one digiy after decimal point and %% display the percentage symbol
# plt.title("over all Churn Rate")
# plt.show()

# data.to_csv("cleaned_Churn_prediction.csv",index=False)
# C:\Users\soma\OneDrive\Desktop\Churn Prediction Project\cleaned_Churn_prediction.csv
# gender_count=data["gender"].value_counts()
# plt.bar(gender_count.index,gender_count.values,color=["skyblue", "lightcoral"])
# plt.xlabel("Gender")
# plt.ylabel("No Customers")
# plt.title("Customer Distribution by Gender")
# plt.show()
partner_status=data["Partner"].value_counts()
# plt.bar(partner_status.index,partner_status.values,color=["seagreen", "orange"])
# plt.title("Partner Status Disrtibution")
# plt.xlabel("Partner")
# plt.ylabel("No of Customers")
# plt.show()
dependents_dist=data["Dependents"].value_counts()
# plt.bar(dependents_dist.index,dependents_dist.values,color=["steelblue","orange"])
# plt.title("Dependents Distributions")
# plt.xlabel("Dependent Status")
# plt.show()
# plt.hist(data["tenure"],bins=20,color="skyblue",edgecolor="black")
# plt.title("Customer Tenure Distribution")
# plt.xlabel("Tenure (Months)")
# plt.ylabel("Number of Customers")
# plt.show()
plt.figure(figsize=(5,4))
# sns.boxplot(x=data["Churn"],y=data["tenure"],palette=["skyblue", "salmon"])
# plt.title("Tenure vs Churn")
# plt.xlabel("Churn")
# plt.ylabel("Tenure (Months)")

# plt.show()
# sns.boxplot(x="Churn",y="MonthlyCharges",data=data,hue="Churn",palette=["skyblue", "salmon"],legend=False)

# plt.title("Monthly Charges vs Churn")
# plt.xlabel("Churn")
# plt.ylabel("Monthly Charges")
# plt.show()
# sns.boxplot(x="Churn",y="TotalCharges",data=data,hue="Churn",palette=["lightgreen", "orange"],legend=False
# )

# plt.title("Total Charges vs Churn")
# plt.xlabel("Churn")
# plt.ylabel("Total Charges")
# plt.show()
# sns.countplot(x="Contract",hue="Churn",data=data,palette=["seagreen", "orange"])
# plt.title("Contract Type vs Churn")
# plt.xlabel("Contract Type")
# plt.ylabel("Number of Customers")
# plt.show()
# sns.countplot(
# x="PaymentMethod",hue="Churn",data=data,palette=["skyblue", "salmon"]
# )

# plt.title("Payment Method vs Churn")
# plt.xlabel("Payment Method")
# plt.ylabel("Number of Customers")
# plt.xticks(rotation=45)
# plt.show()
# sns.countplot(x="InternetService",hue="Churn",data=data,palette=["salmon","lightgreen"])
# plt.title("InternetService vs Churn")
# plt.xlabel("Internet Service")
# plt.ylabel("Number of Customers")
# plt.xticks(rotation=45)
# plt.show()
# plt.show()
# print(data["InternetService"].value_counts())


# print(data.columns)
# sns.countplot(
# x="TechSupport",hue="Churn",data=data,palette=["skyblue", "salmon"]
# )

# plt.title("Tech Support vs Churn")
# plt.xlabel("Tech Support")
# plt.ylabel("Number of Customers")
# plt.show()
# sns.countplot(x="StreamingTV",hue="Churn",data=data,palette=["seagreen","salmon"])

# plt.title("Streaming TV vs Churn")
# plt.xlabel("Streaming TV")
# plt.ylabel("Number of Customers")
# plt.show()
# sns.countplot(x="PaperlessBilling",hue="Churn",data=data,palette=["salmon", "lightgreen"]
# )

# plt.title("Paperless Billing vs Churn")
# plt.xlabel("Paperless Billing")
# plt.ylabel("Number of Customers")
# plt.show()
# Segmentation of Customers by Tenure...........................................................................
bins=[0,18,29,48,72]
labels=["New Customer","Medium Term Customer","Long Term Customer","Loyal Customer"]
data["Tenure_Group"]=pd.cut(data["tenure"],bins=bins,labels=labels)
include_lowest=True
# print(data["Tenure_Group"].value_counts())
# print(data.columns)


tenure_churn=pd.crosstab(
    data["Tenure_Group"],
    data["Churn"],
    normalize="index"
)*100
tenure_churn["Yes"].plot(
    kind="bar",
    color="salmon"
)

# plt.title("Churn Rate by Tenure Group")
# plt.xlabel("Tenure Group")
# plt.ylabel("Churn Percentage")
# plt.xticks(rotation=0)
# plt.show()

# Segmentation Of Customers by Monthly Charges ...................................................................
bins=[0,30,83,122]
labels=["Low Charges","Medium Charges","High Charges"]
data["Monthly_Charges_Group"]=pd.cut(data["MonthlyCharges"],bins=bins,labels=labels)
# print(data["Monthly_Charges_Group"].value_counts())
monthly_charges_Churn=pd.crosstab(data["Monthly_Charges_Group"],data["Churn"],normalize="index")*100
# # print(montly_charges_Churn)
# monthly_charges_Churn["Yes"].plot(kind="bar",color="seagreen")
# plt.title("Churn Rate by monthly_charges_group")
# plt.xlabel("monthly_charges_group")
# plt.ylabel("Churnrate percentage")
# plt.xticks(rotation=0)
# plt.show()
#Segmentation by Contract Type......................................................................................
contract_churn_rate=pd.crosstab(data["Contract"],data["Churn"],normalize="index")*100
# print(contract_churn_rate)
contract_churn_rate["Yes"].plot(kind="bar",color="purple")
plt.title("Contract Type Churn Rate")
plt.xlabel("Contract Type")
plt.ylabel("Churn Percentage")
plt.xticks(rotation=0)
# plt.show()

high_value_Customer=data[(data["MonthlyCharges"]>=70)&(data["Churn"]=="Yes")&(data["tenure"]>=46)]
print(high_value_Customer.shape)
print(high_value_Customer.head(40))
data.to_csv("cleaned_churn_data.csv", index=False)

# print(max(data["tenure"]))
# print(data.columns)
print(data)