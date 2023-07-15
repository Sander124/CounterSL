import streamlit as st

counters = ["Counter 1", "Counter 2", "Counter 3", "Counter 4"]
col = st.columns(4)

if "cvalues" not in st.session_state:
    st.session_state.cvalues = [0, 0, 0, 0]

def increment_counter(i):
    st.session_state.cvalues[i] += 1

def enable_counter(i):
    col[i][0].disabled = False
    col[i][1].disabled = False
    
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
    counter2 = st.checkbox(f"Enable {counters[1]}")
    counter3 = st.checkbox(f"Enable {counters[2]}")
    counter4 = st.checkbox(f"Enable {counters[3]}")
    
    if counter2:
        enable_counter(1)
    if counter3:
        enable_counter(2)
    if counter4:
        enable_counter(3)
            
        custom_name = st.text_input(f"New name for {counters[i]}")
        if custom_name:
            counters[i] = custom_name

def enable_counter(i):
    col[i][0].disabled = False
    col[i][1].disabled = False
    
    
