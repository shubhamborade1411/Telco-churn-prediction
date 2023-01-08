import streamlit as st
import pickle
import pandas as pd

Gender = ['0','1']
Senior_Citizen = ['0','1']
Partner = ['0','1']
Dependents = ['0','1']
PhoneService = ['0','1']
MultipleLines = ['0','1','2']
InternetService = ['0','1','2']
OnlineSecurity = ['0','1','2']
OnlineBackup = ['0','1','2']
DeviceProtection = ['0','1','2']
TechSupport = ['0','1','2']
StreamingTV = ['0','1','2']
StreamingMovies = ['0','1','2']
Contract = ['0','1','2']
PaymentMethod = ['0','1','2','3']
PaperlessBilling = ['0','1']
Tenure = [ ]
MonthlyCharges = [ ]
TotalCharges = [ ]
Churn = ['0','1']







telco = pd.read_pickle('telco.pkl')
#pipe = pickle.load(open('pipe.pkl','rb'))
st.title('Telecom Customer Churn Predictor')
#Tenure = st.number_input('**Tenure**', min_value = 1, max_value = 72)

col1,col2,col3,col4 = st.columns(4)

with col1:
    Gender = st.selectbox('**Select Gender** (0 for Male,1 for Female)',sorted(Gender))
with col2:
    Senior_Citizen = st.selectbox('**Is Senior Citizen?** (0 for No, 1 for Yes)',sorted(Senior_Citizen))
with col3:
    Partner = st.selectbox('**Partner** (0 for Yes, 1 for No         )', sorted(Partner))
with col4:
    Dependents = st.selectbox('**Dependents** (0 for Yes, 1 for No)', sorted(Dependents))

col5,col6,col7,col8 = st.columns(4)

with col5:
    PhoneService = st.selectbox('**PhoneService** (0 for Yes, 1 for No)', sorted(PhoneService))
with col6:
    MultipleLines = st.selectbox('**MultipleLines** (0 for Yes, 1 for No,2 for No Phone Service)', sorted(MultipleLines))
with col7:
    InternetService = st.selectbox('**InternetService** (0 for Fiber Optic, 1 for DSL,2 for No Service)',sorted(InternetService))
with col8:
    OnlineSecurity = st.selectbox('**OnlineSecurity** (0 for Yes, 1 for No,2 for No Internet Service)',sorted(OnlineSecurity))

col9,col10,col11,col12 = st.columns(4)

with col9:
    OnlineBackup = st.selectbox('**OnlineBackup** (0 for Yes, 1 for No,2 for No Internet Service)',sorted(OnlineBackup))
with col10:
    DeviceProtection = st.selectbox('**DeviceProtection** (0 for Yes, 1 for No,2 for No Internet Service)',sorted(DeviceProtection))
with col11:
    TechSupport = st.selectbox('**TechSupport** (0 for Yes, 1 for No,2 for No Internet Service)',sorted(TechSupport))
with col12:
    StreamingTV = st.selectbox('**StreamingTV** (0 for Yes, 1 for No,2 for No Internet Service)', sorted(StreamingTV))

col13,col14,col15,col16 = st.columns(4)

with col13:
    StreamingMovies = st.selectbox('**StreamingMovies** (0 for Yes, 1 for No,2 for No Internet Service)', sorted(StreamingMovies))
with col14:
    Contract = st.selectbox('**Contract** (0 for Month to Month, 1 for Two Year,2 for One Year)', sorted(Contract))
with col15:
    PaymentMethod = st.selectbox('**PaymentMethod** (0 for Electronic cheque, 1 for Mailed cheque,2 for Bank Transfer, 3 for Credit Card)', sorted(PaymentMethod))
with col16:
    PaperlessBilling = st.selectbox('**PaperlessBilling** (0 for Yes, 1 for No)', sorted(PaperlessBilling))

col17,col18,col19 = st.columns(3)
with col17:
    Tenure = st.number_input('Tenure')
with col18:
    MonthlyCharges = st.number_input('MonthlyCharges')
with col19:
    TotalCharges = st.number_input('TotalCharges')

if st.button('Churn Prediction'):


        input_df = pd.DataFrame(
        { 'Gender' : [Gender], 'Senior_Citizen' : [Senior_Citizen], 'Partner' : [Partner], 'Dependents' : [Dependents],
       'Tenure' : [Tenure], 'PhoneService' : [PhoneService], 'MultipleLines' : [MultipleLines], 'InternetService' : [InternetService],
       'OnlineSecurity' : [OnlineSecurity], 'OnlineBackup' : [OnlineBackup], 'DeviceProtection' : [DeviceProtection], 'TechSupport' : [TechSupport],
       'StreamingTV' : [StreamingTV], 'StreamingMovies' : [StreamingMovies], 'Contract' : [Contract], 'PaperlessBilling' : [PaperlessBilling],
       'PaymentMethod' : [PaymentMethod], 'MonthlyCharges' : [MonthlyCharges], 'TotalCharges' : [TotalCharges]})

        result = telco.predict(input_df)
        st.write('1 Means will not churn, 0 Means will Churn')
        st.header(result)