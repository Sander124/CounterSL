import streamlit as st

counters = ["Counter 1", "Counter 2", "Counter 3", "Counter 4"]
col = st.columns(4)

if "cvalues" not in st.session_state:
    st.session_state.cvalues = [0, 0, 0, 0]

def increment_counter(i):
    st.session_state.cvalues[i] += 1
    
with col[0]:
    st.button(f"Increment {counters[0]}", on_click=increment_counter, args=[0]) 
    st.metric(counters[0], st.session_state.cvalues[0])
    
with col[1]:
    st.button(f"Increment {counters[1]}", on_click=increment_counter, args=[1]) 
    st.metric(counters[1], st.session_state.cvalues[1])

with col[2]:
    st.button(f"Increment {counters[2]}", on_click=increment_counter, args=[2]) 
    st.metric(counters[2], st.session_state.cvalues[2])

with col[3]:
    st.button(f"Increment {counters[3]}", on_click=increment_counter, args=[3]) 
    st.metric(counters[3], st.session_state.cvalues[3])

with st.sidebar:
    custom_name1 = st.text_input(f"New name for {counters[0]}")
    custom_name2 = st.text_input(f"New name for {counters[1]}")
    custom_name3 = st.text_input(f"New name for {counters[2]}")
    custom_name4 = st.text_input(f"New name for {counters[3]}")
    
    if custom_name1:
        counters[0] = custom_name1
    if custom_name2:
        counters[1] = custom_name2
    if custom_name3:
        counters[2] = custom_name3
    if custom_name4:
        counters[3] = custom_name4
    
    
