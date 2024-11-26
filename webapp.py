import streamlit as st
import functions

st.title("My Todo App")
st.subheader("Your Tool for your tasks")

st.write("This app will increase your productivity")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a Todo: ',placeholder="Add a new todo")