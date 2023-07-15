import streamlit as st

counters = ["Counter 1", "Counter 2", "Counter 3", "Counter 4"]
col = st.columns(4)[i]

with col[0]:
    st.button(f"Increment {counters[0]}", disabled=False)
    st.metric(counters[0], 0, disabled=True)
    
with col[1]:
    st.button(f"Increment {counters[1]}", disabled=True)
    st.metric(counters[1], 0, disabled=True)

with col[2]:
    st.button(f"Increment {counters[2]}", disabled=True)
    st.metric(counters[2], 0, disabled=True)

with col[3]:
    st.button(f"Increment {counters[3]}", disabled=True)
    st.metric(counters[3], 0, disabled=True)

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
    
    
