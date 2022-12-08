# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
import numpy as np
import pickle


def preprocessing(d):
    data = pd.DataFrame(np.zeros((1,38)), columns = ['CREDIT_SCORE', 'VEHICLE_OWNERSHIP', 'MARRIED', 'CHILDREN',
       'POSTAL_CODE', 'ANNUAL_MILEAGE', 'SPEEDING_VIOLATIONS', 'DUIS',
       'PAST_ACCIDENTS','IS_DUIS', 'DUIS2', 'IS_PAST_ACCIDENTS',
       'PAST_ACCIDENTS2', 'IS_SPEEDING_VIOLATIONS', 'SPEEDING_VIOLATIONS2',
       'POSTAL_CODE1', 'OFFENCE', 'IS_OFFENCE', 'AGE_26-39', 'AGE_40-64',
       'AGE_65+', 'GENDER_male', 'DRIVING_EXPERIENCE_10-19y',
       'DRIVING_EXPERIENCE_20-29y', 'DRIVING_EXPERIENCE_30y+',
       'EDUCATION_none', 'EDUCATION_university', 'INCOME_poverty',
       'INCOME_upper class', 'INCOME_working class',
       'VEHICLE_YEAR_before 2015', 'TYPE_OF_VEHICLE_SUV',
       'TYPE_OF_VEHICLE_Sedan', 'TYPE_OF_VEHICLE_Sports Car',
       'CREDIT_SCORE_CATEGORY_Low', 'CREDIT_SCORE_CATEGORY_Medium',
       'CREDIT_SCORE_CATEGORY_High', 'CREDIT_SCORE_CATEGORY_Very High'])


    data['CREDIT_SCORE'].iloc[0] = d['credit_score']
    data['VEHICLE_OWNERSHIP'].iloc[0] = d['vehicle_ownership']
    data['MARRIED'].iloc[0] = d['married']
    data['CHILDREN'] = d['children']
    data['ANNUAL_MILEAGE'].iloc[0] = d['annual_mileage']


    data['POSTAL_CODE'] = d['postal_code']
    if data['POSTAL_CODE'].iloc[0] == 10238:
        data['POSTAL_CODE1'].iloc[0] = 1

    data['PAST_ACCIDENTS'] = d['past_accidents']
    if data['PAST_ACCIDENTS'].iloc[0] > 0:
        data['IS_PAST_ACCIDENTS'].iloc[0] = 1
    if data['PAST_ACCIDENTS'].iloc[0] > 4:
        data['PAST_ACCIDENTS2'].iloc[0] = 4
    else:
        data['PAST_ACCIDENTS2'].iloc[0] = data['PAST_ACCIDENTS'].iloc[0]

    data['DUIS'].iloc[0] = d['duis']
    if data['DUIS'].iloc[0] > 0:
        data['IS_DUIS'] = 1
    if data['DUIS'].iloc[0] > 3:
        data['DUIS2'].iloc[0] = 3
    else:
        data['DUIS2'].iloc[0] = data['DUIS'].iloc[0]

    data['SPEEDING_VIOLATIONS'].iloc[0] = d['speeding_violations']
    if data['SPEEDING_VIOLATIONS'].iloc[0] > 0:
        data['IS_SPEEDING_VIOLATIONS'].iloc[0] = 1
    if data['SPEEDING_VIOLATIONS'].iloc[0] > 4:
        data['SPEEDING_VIOLATIONS2'].iloc[0] = 4
    else:
        data['SPEEDING_VIOLATIONS2'].iloc[0] = data['SPEEDING_VIOLATIONS'].iloc[0]

    data['OFFENCE'] = data['DUIS'] + data['PAST_ACCIDENTS'] + data['SPEEDING_VIOLATIONS']
    if data['OFFENCE'].iloc[0] > 0:
        data['IS_OFFENCE'].iloc[0] = 1

    if d['gender'] == 'male':
        data['GENDER_male'].iloc[0] = 1


    if d['income'] == 'poverty':
        data['INCOME_poverty'].iloc[0] = 1
    elif d['income'] == 'upper class':
        data['INCOME_upper class'].iloc[0] = 1
    elif d['income'] == 'working class':
        data['INCOME_working class'].iloc[0] = 1
    else:
        pass


    if d['driving_experience'] == '10-19y':
        data['DRIVING_EXPERIENCE_10-19y'].iloc[0] = 1
    elif d['driving_experience'] == '20-29y':
        data['DRIVING_EXPERIENCE_20-19y'].iloc[0] = 1
    elif d['driving_experience'] == '30y+':
        data['DRIVING_EXPERIENCE_30y+'].iloc[0] = 1
    else:
        pass


    if d['education'] == 'none':
        data['EDUCATION_none'].ilo[0] = 1
    elif d['education'] == 'university':
        data['EDUCATION_university'].iloc[0] = 1
    else:
        pass


    if d['age'] == '26-39':
        data['AGE_26-39'].iloc[0] = 1
    elif d['age'] == '40-64':
        data['AGE_40-64'].iloc[0] = 1
    elif d['age'] == '65+':
        data['AGE_65+'].iloc[0] = 1
    else:
        pass

    if d['vehicle_year'] == 'before 2015':
        data['VEHICLE_YEAR_before 2015'].iloc[0] = 1


    if d['type_of_vehicle'] == 'SUV':
        data['TYPE_OF_VEHICLE_SUV'].iloc[0] = 1
    elif d['type_of_vehicle'] == 'Sedan':
        data['TYPE_OF_VEHICLE_Sedan'].iloc[0] = 1
    elif d['type_of_vehicle'] == 'Sports Car':
        data['TYPE_OF_VEHICLE_Sports Car'].iloc[0] = 1
    else:
        pass




    if (data['CREDIT_SCORE'].iloc[0] > 0.2) & (data['CREDIT_SCORE'].iloc[0] <= 0.4):
        data['CREDIT_SCORE_CATEGORY_Low'].iloc[0] = 1
    elif (data['CREDIT_SCORE'].iloc[0] > 0.4) & (data['CREDIT_SCORE'].iloc[0] <= 0.6):
        data['CREDIT_SCORE_CATEGORY_Medium'] = 1
    elif (data['CREDIT_SCORE'].iloc[0] > 0.6) & (data['CREDIT_SCORE'].iloc[0] <= 0.8):
        data['CREDIT_SCORE_CATEGORY_High'].iloc[0] = 1
    elif data['CREDIT_SCORE'].iloc[0] > 0.8:
        data['CREDIT_SCORE_CATEGORY_Very High'].iloc[0] = 1
    else:
        pass


    return data




def get_prediction(data):
    f = open('final_model.pkl', 'rb')
    model = pickle.load(f)
    f.close()
    return model.predict(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("Vehicle Insurance Claim Predictor")
    form = st.form(key="user_input")
    d = {}
    with form:
        d['age'] = st.selectbox("Select Age", ('16-25', '26-39', '40-60', '65+'))
        d['gender'] = st.selectbox("Select Gender", ('female', 'male'))
        d['driving_experience'] = st.selectbox("Select Driving Experience", ('0-9y', '10-19y', '20-29y', '30+y'))
        d['education'] = st.selectbox("Select Education", ("university", "high school", "none"))
        d['income'] = st.selectbox("Select Income", ("upper class", "working class", "middle class", "poverty"))
        d['credit_score'] = st.number_input("Credit Score", min_value = 0.0, max_value = 1.0, step = .01)
        d['vehicle_ownership'] = st.selectbox("Select Vehicle Ownership", (0, 1))
        d['vehicle_year'] = st.selectbox("Vehicle Year", ("after 2015", "before 2015"))
        d['married'] = st.selectbox("Married", (0, 1))
        d['children'] = st.selectbox("Children", (0, 1))
        d['postal_code'] = st.number_input("Postal Code", min_value=10000, max_value = 99999)
        d['annual_mileage'] = st.number_input("Annual Mileage", 1000)
        d['speeding_violations'] = st.number_input("Speeding Violations", 0)
        d['duis'] = st.number_input("DUIS", 0)
        d['past_accidents'] = st.number_input("Past Accidents", 0)
        d['type_of_vehicle'] = st.selectbox("Type Of Vehicle", ("Hatchback", "Sedan", "SUV", "Sports Car"))

        submit = st.form_submit_button("Submit")
        if submit:
            st.write("Complete")



            print("Before button Type of d", type(d))
            print(d)
    btn = st.button("Get Prediction")
    if btn:
        print("After button Type of d", type(d))
        data = preprocessing(d)
        print(data)
        result = get_prediction(data)
        st.text_area("Prediction is", result[0])




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
