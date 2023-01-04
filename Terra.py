# import neccesary packages

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

#allows you to import graph objects for making more customized plots

import plotly.graph_objects as go

st.title("TERRA Megadashboard")
st.sidebar.header("Overview")
st.sidebar.button("TRANSACTIONS")
st.sidebar.button("DEVELOPMENT")
st.sidebar.button("SUPPLY")