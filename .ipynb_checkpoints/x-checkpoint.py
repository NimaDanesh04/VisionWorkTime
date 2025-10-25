import streamlit as st
import sqlite3
import pandas as pd

FPS = 5
conn = sqlite3.connect('presence_log_multi.db')

df = pd.read_sql_query("SELECT * FROM presence_log", conn)

st.title("Presence Log Viewer")

st.subheader("Full Table")
st.dataframe(df)

input_id = st.number_input("Enter ID to calculate total frame and time", min_value=0, step=1)

if st.button("Calculate Sum and Time"):
    filtered_df = df[df['camera_id'] == input_id]
    
    if not filtered_df.empty:
        total_frame = filtered_df['frame_count'].sum()
        total_seconds = total_frame / FPS
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        
        st.success(f"Total frame for ID {input_id}: {total_frame}")
        st.success(f"Total time: {minutes} minutes and {seconds} seconds ({total_seconds:.2f} seconds)")
        
        st.subheader("Filtered Data")
        st.dataframe(filtered_df)
    else:
        st.warning(f"No data found for ID {input_id}")

conn.close()
