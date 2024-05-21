import streamlit as st
import contents as co

def fill_col1a():
    with st.container(height=300, border=True):
        co.profile_picture_content()

def fill_col1b():
    with st.container(height=100, border=True):
        co.athlete_name_content()
    with st.container(height=200, border=True):
        co.health_info_content()

def fill_colA2():
    col1a, col1b = st.columns([1, 2])
    with col1a:
        fill_col1a()
    with col1b:
        fill_col1b()
    with st.container(height=235, border=True):
        co.general_athlete_profile_content()

def fill_col2b():
    with st.container(height=400, border=True):
        co.upper_left_box_content()

def fill_col2d():
    with st.container(height=400, border=True):
        co.upper_right_box_content()

def fill_colA4():
    col2a, col2b, col2c, col2d, col2e = st.columns([1, 24, 1, 16, 1])
    with col2b:
        fill_col2b()
    with col2d:
        fill_col2d()
    with st.container(height=235, border=True):
        co.bottom_right_large_box_content()

def fill_colB1():
    with st.container(height=225, border=True):
       co.bottom_left_top_content()
    with st.container(height=225, border=True):
        co.bottom_left_bottom_content()

def fill_colB2():
    with st.container(height=400, border=True):
        co.bottom_right_left_content()

def fill_colB3():
    with st.container(height=400, border=True):
        co.bottom_right_right_content()
