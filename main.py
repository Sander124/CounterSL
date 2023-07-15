import streamlit as st

st.set_page_config(layout="wide") 

cols = st.columns(4)

@st.cache_data
def increment(name):
    if name not in st.session_state.counters:
        st.session_state.counters[name] = 0
    st.session_state.counters[name] += 1
    
@st.cache_data
def decrement(name):
    if name not in st.session_state.counters:
        st.session_state.counters[name] = 0
    st.session_state.counters[name] -= 1
   
def add_counter(name):
    
    if st.session_state.num_counters >= 4:
        st.error("Reached max of 4 counters")
    else:
        cols[st.session_state.num_counters].st.button("Increment "+name, on_click=increment, args=[name])
        cols[st.session_state.num_counters].st.button("Decrement "+name, on_click=decrement, args=[name])
        return

def get_column():
    if st.session_state.num_counters % 2 == 0:
        return st.columns(2) 
    else:
        return st.columns(1)

if "counters" not in st.session_state:
    st.session_state.counters = {}

if "num_counters" not in st.session_state:
    st.session_state.num_counters = 1 

with cols[0]:

    st.button("Increment Sander", key="inc", on_click=increment, args=["Sander"])
    st.button("Decrement Sander", key="dec", on_click=decrement, args=["Sander"])
    st.metric("Sander", st.session_state.counters.get("Sander", 0))

with st.sidebar:

    st.header("Options")
    name = st.text_input("Add User") 
    
    if st.session_state.num_counters < 4:
        add_btn = st.button("Add Counter")
    else:
        add_btn = st.button("Add Counter", disabled=True)
        
    if add_btn: 
        add_counter(name)

    col = get_column()
    
with col:
    st.button("Increment "+name, on_click=increment, args=[name])
    st.button("Decrement "+name, on_click=decrement, args=[name])
        st.metric(name, st.session_state.counters.get(name, 0))

    st.session_state.num_counters += 1
    
