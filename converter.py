import numpy as numpy
import pandas as pd
import streamlit as st

#DATA_URL = (
#	    "data.csv"
#	)

#@st.cache(persist=True)
#def load_data():
#	data = pd.read_csv(DATA_URL)
#	return data

def write():
	DATA_URL = (
	    "data.csv"
	)

	st.title("Salary Converter")
	st.markdown("How much money would you need in London to buy the same things you would buy in New York? Convert salary using purchasing power parity.")

	#data = load_data()
	data = pd.read_csv(DATA_URL)

	source = st.selectbox("Source country", list(data.Country))
	salary = st.number_input("Salary in source country's currency")
	target = st.selectbox("Target country", list(data.Country))

	def convert_by_ppp(source_country, target_country, salary):
	    return salary / list(data[data["Country"]==source_country]["2019"])[0] * list(data[data["Country"]==target_country]["2019"])[0]

	val_ppp = convert_by_ppp(source, target, salary)
	val_ppp = round(val_ppp, 2)
	source_curr = data[data["Country"]==source]["Currency"].reset_index(drop=True)[0]
	source_curr_name = data[data["Country"]==source]["Currency Name"].reset_index(drop=True)[0]
	target_curr = data[data["Country"]==target]["Currency"].reset_index(drop=True)[0]
	target_curr_name = data[data["Country"]==target]["Currency Name"].reset_index(drop=True)[0]
	st.write("You will need", val_ppp, target_curr_name, "(", target_curr, ") in", target, "to buy the same things you would in", source, "with", salary, source_curr_name, "(", source_curr, ")")

	st.text("")
	st.write("Data source: https://data.worldbank.org/indicator/PA.NUS.PRVT.PP")