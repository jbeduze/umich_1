import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def Holder_container_1(content_func):
    with stylable_container(
        key="Holder_container_1",
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
        content_func()



def Holder_container_2(content_func):
    with stylable_container(
        key="Holder_container_2",
        css_styles="""
            {
                background-color: #161d28;
                color: #161d28;
                border-radius: 10px;  
                margin: 0px;
                border: 2px solid #ff6c3a;
                box-shadow: 1px 1px 12px 10px #6a7483;
                height: 400px;   
            }
            """,
    ):
        content_func()

def data_container_1(content_func):
    with stylable_container(
        key="data_container_1",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                height: 50vh;
                width: 80vw;
            }
            """,
    ):
        content_func()

def Holder_container_3(content_func):
    with stylable_container(
        key="Holder_container_3",
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
        content_func ()