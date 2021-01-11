import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

def write():
	DATA_URL = (
		"capital.csv"
	)

	st.title("World Map")

	data = pd.read_csv(DATA_URL)

	feature = st.selectbox("Search by", [" ", "Country", "Capital", "Currency Name"])
	if feature != " ":
		feature_list = list(data[feature].value_counts().index)
		feature_list.sort()
		feature_name = st.selectbox(feature, feature_list)
		data = data[data[feature] == feature_name]
		fig = px.scatter_mapbox(data,
	                        lat="latitude", lon="longitude",
	                        hover_name="Country", hover_data=["Capital", "Currency"],
	                        color_discrete_sequence=["fuchsia"], zoom=10, height=500)
		fig.update_traces(marker_size=12.5)
		fig.update_layout(mapbox_style="open-street-map")
		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.write(fig)
	else:
		fig = px.scatter_mapbox(data,
	                        lat="latitude", lon="longitude",
	                        hover_name="Country", hover_data=["Capital", "Currency"],
	                        color_discrete_sequence=["fuchsia"], zoom=0, height=500)
		fig.update_traces(marker_size=8)
		fig.update_layout(mapbox_style="open-street-map")
		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.write(fig)