import streamlit as st
import functions

print("herre")
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app is going to increase you productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a todo...", on_change=add_todo, key="new_todo")

print("hello")
print("hi")


st.session_state