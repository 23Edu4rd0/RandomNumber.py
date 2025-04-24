import streamlit as st
import random

st.set_page_config(
    page_title="Adivinhe o Número", 
    page_icon="favicon.ico",                
    layout="centered",              
)

if 'numero_aleatorio' not in st.session_state:
    st.session_state.numero_aleatorio = 3
    st.session_state.acertou = False
    st.session_state.tentativas = 0
    st.session_state.numeros_tentados = []

def reiniciar_jogo():
    st.session_state.numero_aleatorio = random.randint(1, 15)
    st.session_state.acertou = False
    st.session_state.tentativas = 0
    st.session_state.numeros_tentados = []

st.title('Loteria - Adivinhe o número!')

numero = st.number_input('Digite um número entre 1 e 15:', min_value=1, max_value=15, step=1)

col1, col2 = st.columns([1, 1])

st.html("""
    <style>
        div.stButton > button {
            width: 100%;
            height: 100%;
        }
    </style>
""")

with col1:
    if st.button('Enviar', disabled=st.session_state.acertou or st.session_state.tentativas == 3):
        verificacao = True
        st.session_state.tentativas += 1
        st.session_state.numeros_tentados.append(numero)

        if st.session_state.tentativas > 3:
            verificacao = False
            st.warning('Você já tentou 3 vezes! O jogo foi reiniciado, tente novamente.')
            reiniciar_jogo()

        if numero == st.session_state.numero_aleatorio:
            st.session_state.acertou = True
            st.balloons()  
            st.success(f'Parabéns! Você acertou o número secreto: {st.session_state.numero_aleatorio}')
        elif numero < st.session_state.numero_aleatorio and verificacao:
            st.warning('O número secreto é maior que o número digitado.')
        elif numero > st.session_state.numero_aleatorio and verificacao:
            st.warning('O número secreto é menor que o número digitado.')

        if st.session_state.tentativas >= 3 and not st.session_state.acertou:
            st.error(f'Você não acertou o número secreto: {st.session_state.numero_aleatorio}')

with col2:
    if st.button('Reiniciar', disabled=not (st.session_state.tentativas >= 3 or st.session_state.acertou)):
        reiniciar_jogo()
        st.success('O jogo foi reiniciado!')
