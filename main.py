
import streamlit as st

counters = {}

st.title("Multi Counter App")

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

def reset_all():
    st.session_state.count = 0
    counters.clear()

col1, col2 = st.columns(2)

with col1:
    st.button("Increment", on_click=increment_counter)
    st.metric("Default Counter", st.session_state.count)

with col2:
    name = st.text_input("Counter Name")
    if name:
        if name not in counters:
            counters[name] = 0
        counters[name] += 1
        st.metric(name, counters[name])
        st.button("Delete "+name, on_click=counters.pop, args=[name])

st.button("Reset All Counters", on_click=reset_all)

if 'reset_confirm' not in st.session_state:
    st.session_state.reset_confirm = False

st.checkbox("Check to confirm reset", key="reset_confirm")

if st.session_state.reset_confirm:
    st.button("Reset All Counters", on_click=reset_all)
else:
    st.warning("Check the box to confirm reset")
