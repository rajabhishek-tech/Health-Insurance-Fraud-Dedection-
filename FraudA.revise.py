# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:27:39 2021

@author: RajabhishekAditya
"""
import pandas as pd
import streamlit as st 
from pickle import load
from pathlib import Path
import base64
from sklearn.preprocessing import LabelEncoder

# In[]:
    #create the color background & subtitle 

# In[]:
    
# Logo 

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
header_html = "<img src='data:Excelrlogo/png;base64,{}' class='img-fluid'>".format(
    img_to_bytes("Excelrlogo.png")
)
st.markdown(
    header_html, unsafe_allow_html=True,
)
    
# In[ ]:



# In[]:

# In[]:
st.header("Project Mentor : Vinod") 
  


# In[]:
if st.checkbox("Members of the Group"):
    
  # dispaly the text if the checkbox returns True value
  st.subheader("1)Rajabhishek Aditya, 2)Arpit Namdeo, 3)Darshan H.R, 4)Praveen, 5)Natarajan")

# In[]:

page_bg_img = '''
<style>
body {
background-image: url("https://klgflorida.com/wp-content/uploads/2018/04/Insurance-Fraud-is-a-Serious-Crime.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



      
# In[]:
    
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Insurance FRAUD Detection ML App</h1> 
    </div> 
    """
      
    

# In[]

    

def user_input_features():    
    
    # following lines create boxes in which user can enter data required to make prediction 
    Hospital_Id= st.number_input("Hospital_Id") 
    
    Age = st.selectbox("Age Group",('0 to 17','18 to 29','30 to 49','50 to 69','70 or Older'))
    Gender = st.selectbox('Sex',('Female','Male'))
    
    Days_spend_hsptl = st.number_input("Number of days in hospital")
    Admission_type =  st.selectbox('Admission Type',('Elective', 'Emergency', 
                                                      'Newborn', 'Not Available', 'Trauma','Urgent'))
   
    ccs_diagnosis_code = st.number_input("Enter Diagnosis Code")
    ccs_procedure_code = st.number_input("ccs_procedure_code")
    Home_or_selfcare=st.selectbox('Home or Selfcare',('Home/Self care','Another Type','Cancer Center','Court/Law Enforcement','Critical Access','Expired','Facility','Federal','HHS','Hosp-Medicare','Hospice-Home','Hospice-Medical','Inpatient','Lef-Advice','MedicAid-Nursing','Medicare-Long Term','Psychiatric','Short-term','Skilled'))
    apr_drg_description = st.selectbox('apr_drg_description',('Other pneumonia','Cellulitis','Other digestive system diagnoses','Bronchiolitis','Cardiac arrhythmia'))
    Code_illness = st.number_input("Code_illness")
    Mortalityrisk=st.selectbox('mortalityrisk',(1,2,3,4))
    Surg_Description = st.selectbox("Surg_Description",('Medical','Surgical'))
    Abortion = st.selectbox('Abortion',('Yes','No'))
    Emergency_dept= st.selectbox('Emergency Dept',('Yes','No'))
    
    Tot_charg =  st.number_input("Total Charge")
    Tot_cost = st.number_input("Tot_cost")
     
    Payment_Typology=st.selectbox('Payment Typology',(1,2,3,4,5))
    
    

  
    
    
    data = {
        'Hospital_Id':Hospital_Id,
        'Age':Age,
        'Gender':Gender,
        
        'Days_spend_hsptl':Days_spend_hsptl,
        'Admission_type':Admission_type,
        
        'ccs_diagnosis_code':ccs_diagnosis_code,
        'ccs_procedure_code':ccs_procedure_code,
        'Home_or_selfcare': Home_or_selfcare,
        'apr_drg_description':apr_drg_description,
        'Code_illness ':Code_illness,
        'Mortalityrisk':Mortalityrisk,
        'Surg_Description':Surg_Description,
        'Abortion':Abortion,
        'Emergency_dept':Emergency_dept,
        
        'Tot_charg':Tot_charg,
        'Tot_cost':Tot_cost,
        
        'Payment_Typology': Payment_Typology,

        }
    
    features = pd.DataFrame(data,index = [0])
    
    
    return features

df = user_input_features()

st.write(df)

lst = ['Hospital_Id','Age','Gender','Tot_charg','Admission_type','Days_spend_hsptl','apr_drg_description','Code_illness ','Abortion','Tot_cost',
       'ccs_diagnosis_code', 'Mortalityrisk','Surg_Description','Emergency_dept', 'Payment_Typology','Home_or_selfcare','ccs_procedure_code']

for i in lst:
   df[i] = LabelEncoder().fit_transform(df[i])
    

#loading model 
loaded_model = load(open('Final-ModelG6.sav', 'rb'))

prediction_proba = loaded_model.predict_proba(df)


prediction = loaded_model.predict(df)





if st.button("Predict"): 

 (('Claim: Genuine :thumbsup:' if  prediction_proba[0][1] > 0.25 else 'Claim: Fraud:thumbsdown:'))
 

st.write("\n")
st.write("\n")
    
# In[];

    