from vega_datasets import data
import matplotlib.pyplot as plt
import altair as alt
import pandas as pd
import numpy as np

import streamlit as st

st.title("Building apps with streamlit")

st.write("## Basic Outputs")

st.write("### Strings")
# st.markdown("## Header 2")
st.write("Hello world!")

st.write("### Numbers")
st.write(42)
st.write(42.42)

st.write("### Booleans")
st.write(True)
st.write(False)

st.write("### Lists & Dictionaries")
st.write([1, 2, 3, 4])
st.write({
    "a": "A",
    "b": "B"
    })


cars_df = data.cars()

st.write("## Dataframes")

st.write("### Interactive Dataframes")

cars_df

st.write("### Static tables")
st.table(cars_df.head())


st.write("## Charts")

st.write("### Inbuilt charting")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.write("### matplotlib")

# Plot the horsepower vs. weight
plt.scatter(cars_df['Horsepower'],cars_df['Weight_in_lbs'])
plt.xlabel('Horsepower')
plt.ylabel('Weight')

st.pyplot(plt)


st.write("### Vega-Altair")
chart = alt.Chart(cars_df).mark_point().encode(
            x="Miles_per_Gallon:Q",
            y="Weight_in_lbs:Q"
        ).interactive()

chart


st.write("## Maps")
map_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
    )

st.map(map_data)
