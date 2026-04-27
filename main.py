import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Мой Мессенджер", page_icon="💬")
st.title("💬 Простой Чат")

# Хранилище сообщений (чтобы они не пропадали при обновлении)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Отображение всех сообщений
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле для ввода сообщения
if prompt := st.chat_input("Напиши сообщение..."):
    # Добавляем сообщение пользователя
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Ответ (пока автоматический, потом заменим на настоящего друга)
    response = f"Ты написал: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
