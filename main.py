# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

#Frameworks tipicos
#Streamlit
#Flask
#Django
#FastAPI

# streamlit - frontend e backend
# a IA que vamos usar: OpenAI
# pip install openai streamlitpi

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

#Titulo
st.write("### ChatBot com *IA* :sunglasses:")
st.markdown("### **ChatBot** com :red[**IA**]")

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")
#campo para enviar arquivo
#arquivo = st.file_uploader("Selecione um arquivo")
#em caso de audio ... ele le o audio, converte para texto e envia para a IA

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    # posso passar Nome, user, assistant
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    #cookies nada mais é do que a lista de mensagens

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


