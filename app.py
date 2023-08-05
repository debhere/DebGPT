import streamlit as st
from assistant.DigiAssist import ask_anything


def mybot():
    st.title('DebGPT (powered by Bard)')
    st.write('How may I help you today?')

    conversation = []
    counter = 0

    while True:
        user_input = st.text_input('Ask me anything', key=f'user_input_{counter}')

        if user_input:
            conversation.append({'role': 'user', 'content': user_input})
            generated_output = ask_anything(user_input)
            #generated_output = bardResponse(user_input)
            conversation.append({'role': 'model', 'content': generated_output})

            st.write('Response: ')
            st.write(conversation[-1]['content'])
            counter += 1

        else:
            break


if __name__ == "__main__":
    mybot()
