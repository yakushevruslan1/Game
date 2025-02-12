import random
import streamlit as st

st.title("Играем в угадай число")
st.write("Мы уже загадали число, попробуйте отгадать его")

if st.button("Начать новую игру"):
    hidden_number = random.randint(1, 100)
    st.session_state.hidden_number = hidden_number
    st.session_state.count = 0
else:
    hidden_number = st.session_state.get('hidden_number', None)
    count = st.session_state.get('count', 0)

if hidden_number is not None:
    number = st.number_input("Введите число от 1 до 100", min_value=1, max_value=100, step=1)
    if st.button("Проверить"):
        count += 1
        st.session_state.count = count
        if hidden_number > number:
            st.write("Ваше число меньше, чем мы загадали")
        elif hidden_number < number:
            st.write("Ваше число больше, чем мы загадали")
        else:
            st.write(f"Ура, вы угадали с {count} попыток!")
            st.session_state.hidden_number = None
else:
    st.write("Нажмите 'Начать новую игру', чтобы начать.")