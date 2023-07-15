import streamlit as st

counters = ["Counter 1", "Counter 2", "Counter 3", "Counter 4"]

for i in range(4):
    col = st.columns(1)[i]
    with col:
        st.button(f"Increment {counters[i]}", disabled=True)
        st.metric(counters[i], 0, disabled=True)

with st.sidebar:
    for i in range(4):
        if st.checkbox(f"Enable {counters[i]}"):
            enable_counter(i)
            
        custom_name = st.text_input(f"New name for {counters[i]}")
        if custom_name:
            counters[i] = custom_name

def enable_counter(i):
    col = st.columns(4)[i]
    col[0].disabled = False
    col[1].disabled = False
    
    
