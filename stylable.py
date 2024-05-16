import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def Holder_container_1(vartitle):
    with stylable_container(
        key="pazazz",
        css_styles="""
            {
                background-color: #6a7483;
                color: #f0f0f0;
                border-radius: 10px;
                padding: -3px;
                margin: 0px;
                border: 2px solid #f0f0f0;
                box-shadow: 1px 1px 15px 8px #ff6c3a;  
            }
            """,
    ):
        st.container(height=300)



def Holder_container_2(vartitle):
    with stylable_container(
        key="simple_box",
        css_styles="""
            {
                background-color: #161d28;
                color: #161d28;
                border-radius: 10px;
               
                margin: 0px;
                border: 2px solid #ff6c3a;
                box-shadow: 1px 1px 6px 3px #6a7483;
                height: 400px;   
            }
            """,
    ):
        with st.container(height=400):
            st.markdown(vartitle)

def data_container_1(data):
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                height: 50vh;
                width: 80vw;
            }
            """,
    ):
        st.markdown(data)

def Holder_container_3(vartitle):
    with stylable_container(
        key="pazazz",
        css_styles="""
            {
                background-color: #f0f0f0;
                color: #161d28;
                border-radius: 10px;
                padding: -3px;
                margin: 0px;
                border: 2px solid #f0f0f0;
                box-shadow: 1px 1px 15px 8px #ff6c3a;  
            }
            """,
    ):
        st.container(height=300)