import streamlit as st

counters = ["Counter 1", "Counter 2", "Counter 3", "Counter 4"]
col = st.columns(4)

if "cvalues" not in st.session_state:
    st.session_state.cvalues = [0, 0, 0, 0]

if 'cnames' not in st.session_state:
    st.session_state.cnames = counters


def increment_counter(i):
    st.session_state.cvalues[i] += 1
    
with col[0]:
    st.button(f"Increment {st.session_state.cnames[0]}", on_click=increment_counter, args=[0]) 
    st.metric(st.session_state.cnames[0], st.session_state.cvalues[0])
    
with col[1]:
    st.button(f"Increment {st.session_state.cnames[1]}", on_click=increment_counter, args=[1]) 
    st.metric(st.session_state.cnames[1], st.session_state.cvalues[1])

with col[2]:
    st.button(f"Increment {st.session_state.cnames[2]}", on_click=increment_counter, args=[2]) 
    st.metric(st.session_state.cnames[2], st.session_state.cvalues[2])

with col[3]:
    st.button(f"Increment {st.session_state.cnames[3]}", on_click=increment_counter, args=[3]) 
    st.metric(st.session_state.cnames[3], st.session_state.cvalues[3])


with st.sidebar:
    #custom_name1 = st.text_input(f"New name for {st.session_state.cnames[0]}")
   #custom_name2 = st.text_input(f"New name for {st.session_state.cnames[1]}")
    #custom_name3 = st.text_input(f"New name for {st.session_state.cnames[2]}")
    #custom_name4 = st.text_input(f"New name for {st.session_state.cnames[3]}")

    with st.form():
        name = st.selectbox('Name to replace', st.session_state.cnames)
        to_name = st.text_input(f"Replace with:")
        apply = st.form_submit_button("Apply changes")
        if apply:
            idx = st.session_state.cnames.index(name)
            st.session_state.cnames[idx] = to_name


    
        #st.session_state.cnames[0] = custom_name1
   # if custom_name2:
     #   st.session_state.cnames[1] = custom_name2
   # if custom_name3:
  #      st.session_state.cnames[2] = custom_name3
  #  if custom_name4:
    #    st.session_state.cnames[3] = custom_name4
    
    
