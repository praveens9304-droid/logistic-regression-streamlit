import streamlit as st
from pickle import load
import pandas as pd




st.title('My Classification Model')
st.write('Patient having diabetes or not?')

def get_input():
	
	Preg = st.sidebar. number_input ('Enter the numper of pregnancies')
	Gluc= st.sidebar. number_input ('Glucose')
	BP= st.sidebar. number_input ('BloodPressure')
	SkinT= st.sidebar. number_input ('SkinThickness')
	Insul= st.sidebar. number_input ('Insulin')
	BMIs= st.sidebar. number_input ('BMI')
	DPFunction= st.sidebar. number_input ('DPFunction')
	age = st.sidebar.slider('Age',min_value=1,max_value=100)
	

	data_dict =  {
		'Pregnancies'	: Preg,
		'Glucose'	:Gluc,
		'BloodPressure'	:BP,
		'SkinThickness'	:SkinT,
		'Insulin'	:Insul,
		'BMI'	:BMIs,
		'DiabetesPedigreeFunction'	:DPFunction,
		'Age'      :age
	}

	df = pd.DataFrame(data_dict, index=[0])
	return df

data = get_input()

loaded_model = load(open('clf.pkl','rb'))

if st.sidebar.button('Submit'):
	st.write(data)

	res = loaded_model.predict(data)

	if res == 0:
		st.write('No, they does not have diabetes')
	else:
		st.write('Yes, they have diabetes')


