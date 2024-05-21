import streamlit as st
from streamlit_extras.stylable_container import stylable_container

import stylable as styl
import stylable_layout as styll

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

colA1, colA2, colA3, colA4, colA5 = st.columns([1, 16, 1, 24, 1])

with colA2:
    styl.Holder_container_1(styll.fill_colA2)

with colA4:
    styl.Holder_container_2(styll.fill_colA4)

colB1, colB2, colB3, colB4 = st.columns([8, 4, 4, 1])

with colB1:
    styl.Holder_container_3(styll.fill_colB1)

with colB2:
    styl.data_container_1(styll.fill_colB2)

with colB3:
    styl.data_container_1(styll.fill_colB3)

# Athlete_Profile, Team_veiw, AI_Assistant = st.tabs(["Athlete Profile", "Team Veiw", "AI Assistant"])
# colA1, colA2, colA3, colA4, colA5 = st.columns([1,16,1,24,1])
# with colA2:
#     with styl.Holder_container_1(styll.fill_col1a):
#         col1a, col1b = st.columns([1,2])
#         with col1a:
#             with styl.data_container_1(styll.fill_col1a):
#                 st.markdown("Profile picture")
#         with col1b:
#             with st.container(height=100, border= True):
#                 st.markdown("Athlete Name")
#         with col1b:
#             with st.container(height=200, border=True):
#                 st.markdown("Health info/ if recovering form injury")
#         with st.container(height=235, border=True):
#             st.markdown("general Athlete profile info")
# with colA4:
#     with st.container(height=700, border=True):
#         col2a, col2b, col2c, col2d, col2e = st.columns([1,24,1,16,1])
#         with col2b:
#             with st.container(height=400, border=True):
#                 st.markdown("upper left box in right large container")
#         with col2d:
#             with st.container(height=400, border=True):
#                 st.markdown("upper box on left in right large container")
#         with st.container(height=235, border=True):
#             st.markdown("bottom box in right large container")
# colB1, colB2, colB3, colB4 = st.columns([8,4,4,1])
# with colB1:
#     with st.container(height=500, border=True):
#         with st.container(height=225, border=True):
#             st.markdown("bottom left top")
#         with st.container(height=225, border=True):
#             st.markdown("bottom left bottom")
# with colB2:
#     with st.container(height=400, border=True):
#         st.markdown("bottom right left")
# with colB3:
#     with st.container(height=400, border=True):
#         st.markdown("bottom right right")


# # st.header("Wrestling app")

# col1, col2 = st.columns([7,10])

# with col1:
#     vartitle_1 = "Profile information"
#     styl.Holder_container_1(vartitle_1)
#     styl.Holder_container_2(vartitle_1)
#     styl.data_container_1(vartitle_1)

# with col1:
#     vartext = "Coach and AI Analysis"
#     styl.Holder_container_2(vartext)

# import streamlit as st
# import plotly.graph_objects as go
# import pandas as pd

# # Sample data
# data = {
#     "Date": ["2024-04-07", "2024-03-29", "2023-09-24", "2023-09-17", "2023-08-31", "2023-05-28", "2023-05-28", "2023-05-21", 
#              "2023-04-08", "2023-04-08", "2023-04-07", "2023-04-07", "2023-02-04", "2023-01-07", "2023-01-07"],
#     "Tournament": ["2024 Last Chance OTT Qualifier", "PAUSAW Warrior Run FS/GR Qualifi", "Tyrant Nationals", "Elite 8 Duals- Folk 2023", 
#                    "High School Boys Season", "PNL Pennsylvania", "PNL Pennsylvania", "2023 PAUSAW FS State Championshi", 
#                    "PAUSAW Freestyle and Greco Bisho", "PAUSAW Freestyle and Greco Bisho", "PAUSAW Freestyle and Greco Warri", 
#                    "PAUSAW Freestyle and Greco Warri", "MHSA AA Eastern Divisional", "Bozeman Schools JV 2023 JV Tourn", 
#                    "2023 East Coast Catholic Classic"],
#     "Weight Class": ["Freestyle 65", "Boys Junior", "High School", "132", "114", "Junior 120-1", "Test Group T", "Boys Junior", 
#                      "Boys Junior", "Boys Junior", "Boys Junior", "Boys Junior", "132", "JV 132B", "120"],
#     "Place": ["2nd", "1st", "1st", None, None, "2nd", "4th", "1st", "1st", "1st", "1st", "1st", "DNP", "7th", "1st"]
# }

# # DataFrame creation
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# # Convert places to numerical values
# place_mapping = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "6th": 6, "7th": 7, "8th": 8, "DNP": None}
# df['Place'] = df['Place'].map(place_mapping)

# # Visualization 1: Line Chart with Scatter Points
# fig1 = go.Figure()

# for weight_class in df['Weight Class'].unique():
#     class_data = df[df['Weight Class'] == weight_class]
#     fig1.add_trace(go.Scatter(
#         x=class_data['Date'], 
#         y=class_data['Place'], 
#         mode='lines+markers', 
#         name=weight_class,
#         text=class_data['Tournament']
#     ))

# fig1.update_layout(
#     title='Wrestler Performance Over Time',
#     xaxis_title='Date',
#     yaxis_title='Placement',
#     yaxis=dict(autorange='reversed'), # Reverse y-axis to show 1st place at the top
#     hovermode='x unified'
# )

# # Visualization 2: Box Plot
# fig2 = go.Figure()

# for weight_class in df['Weight Class'].unique():
#     class_data = df[df['Weight Class'] == weight_class]
#     fig2.add_trace(go.Box(
#         y=class_data['Place'], 
#         name=weight_class,
#         boxpoints='all', # show all points
#         jitter=0.3, # spread out points for better visibility
#         pointpos=-1.8 # offset points to the left
#     ))

# fig2.update_layout(
#     title='Distribution of Placements by Weight Class',
#     xaxis_title='Weight Class',
#     yaxis_title='Placement',
#     yaxis=dict(autorange='reversed') # Reverse y-axis to show 1st place at the top
# )

# # Streamlit app
# st.title('Wrestler Dashboard')

# with st.container():
#     st.header("Performance Over Time")
#     st.plotly_chart(fig1, use_container_width=True)

# with st.container():
#     st.header("Distribution of Placements by Weight Class")
#     st.plotly_chart(fig2, use_container_width=True)




# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# from folium.plugins import MarkerCluster
# from datetime import datetime

# # Sample data for upcoming events
# data = {
#     "Date": ["2024-05-15", "2024-05-17", "2024-05-17", "2024-05-17", "2024-05-17", "2024-05-17", "2024-05-17", "2024-05-17", "2024-05-18", "2024-05-18"],
#     "Tournament": ["May 15 Event", "University of Wrestling SUMMER SEASON 2024", "2024 CAUSA Assoc Duals - Schoolboys", "2024 CAUSA Association Duals - BOYS", "2024 CAUSA Association Duals - GIRLS", "PAUSAW State FS/GR Championship", "AZ-USAW `State Freestyle Tournament`", "2024 Dynamic Friday Night Throw Down / Canceled", "2024 USA Wrestling Central Regional Champ - FS", "2024 Brady Strong National Duals (HS)"],
#     "Location": ["Allen, TX 75002", "Bountiful, UT 84010", "Fresno, CA 93721", "Fresno, CA 93721", "Fresno, CA 93721", "State College, PA 16803", "Phoenix, AZ 85048", "Raleigh, NC 27603", "Fort Wayne, IN 46805", "Whitesboro, NY 13492"],
#     "Latitude": [33.1032, 40.8894, 36.7378, 36.7378, 36.7378, 40.7934, 33.3076, 35.7715, 41.1239, 43.1251],
#     "Longitude": [-96.6706, -111.8802, -119.7871, -119.7871, -119.7871, -77.8616, -112.0144, -78.6401, -85.1413, -75.3451]
# }

# # Convert to DataFrame
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# # Function to get color based on date proximity
# def get_color(date):
#     days_to_event = (date - datetime.now()).days
#     if days_to_event <= 7:
#         return 'red'
#     elif days_to_event <= 14:
#         return 'orange'
#     else:
#         return 'green'

# # Create map
# map_center = [39.8283, -98.5795] # Center of the USA
# m = folium.Map(location=map_center, zoom_start=4)

# # Add marker cluster
# marker_cluster = MarkerCluster().add_to(m)

# # Add markers to map
# for idx, row in df.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         popup=f"{row['Tournament']}<br>{row['Date'].strftime('%Y-%m-%d')}<br>{row['Location']}",
#         icon=folium.Icon(color=get_color(row['Date']))
#     ).add_to(marker_cluster)

# # Streamlit app
# st.title('Upcoming Events')
# # from PIL import IMG

# # IMG = image.open(Profile_pic.png)

# # with st.container():
# #     st.write("**Bo Bassett**")
# #     st.write("**Windber, PA**")
# #     st.write("**Weight:** 65")
# #     st.write("**Record:** 26 - 1")
# #     st.write("**Pins:** 0")
# #     st.write("**Techs:** 23")
# #     st.write("**Majors:** 1")
# #     st.write("**Rank Value:** 1.119167")
# #     st.write("**Rank Date:** 04/02/2024")
# #     st.write("**Stats since 05/17/2023**")
# #     st.image("Profile_pic.png", caption="Bo Bassett", use_column_width=True)

#     # Display the map
# st_folium(m, width=700, height=500)





# import streamlit as st
# import plotly.express as px
# import pandas as pd

# # Sample data for significant wins
# data = {
#     "Date": ["2023-05-28", "2023-09-17", "2023-05-21", "2024-03-29", "2023-09-17", "2023-09-17", "2023-09-24", "2024-04-07", "2023-09-24", "2023-05-28", "2023-05-28"],
#     "Tournament": ["PNL Pennsylvania", "Elite 8 Duals- Folk 2023", "2023 PAUSAW FS State Championshi", "PAUSAW Warrior Run FS/GR Qualifi", "Elite 8 Duals- Folk 2023", "Elite 8 Duals- Folk 2023", "Tyrant Nationals", "2024 Last Chance OTT Qualifier", "Tyrant Nationals", "PNL Pennsylvania", "PNL Pennsylvania"],
#     "Match": ["Josh Vazquez (TF)", "Cooper Hilton (Maj)", "Josef Garshnick (TF)", "Griffin Walizer (TF)", "Casen Roark (TF)", "Elias Navida (TF)", "Kai Vielma (TF)", "Aden Valencia (Dec)", "William Sakoutis (TF)", "Adrian Meza (Dec)", "Nathan Desmond (TF)"],
#     "Result": ["TF", "Maj", "TF", "TF", "TF", "TF", "TF", "Dec", "TF", "Dec", "TF"]
# }

# # DataFrame creation
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# # Define bubble sizes based on match result
# result_size_mapping = {"TF": 40, "Maj": 30, "Dec": 20}
# df['Size'] = df['Result'].map(result_size_mapping)

# # Define bubble color based on match result
# result_color_mapping = {"TF": 'blue', "Maj": 'green', "Dec": 'red'}
# df['Color'] = df['Result'].map(result_color_mapping)

# # Plotly bubble chart
# fig = px.scatter(df, x='Date', y='Tournament', size='Size', color='Result', 
#                  hover_name='Match', title='Significant Wins',
#                  labels={'Date': 'Date', 'Tournament': 'Tournament', 'Size': 'Type of Win'},
#                  color_discrete_map={"TF": 'blue', "Maj": 'green', "Dec": 'red'})

# fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')),
#                   selector=dict(mode='markers'))

# # Streamlit app
# st.title('Wrestler Dashboard - Significant Wins')

# with st.container():
#     st.plotly_chart(fig, use_container_width=True)

