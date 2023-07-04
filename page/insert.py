import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    
    
    with st.form(key='insert'):
        input_id = st.number_input(label= 'insira o id', format='%i')
        input_name = st.text_input(label='Insira o nome')
        input_endereco = st.text_input(label='insira um endereço')
        input_telefone = st.text_input(label ='insira o telefone' ) 

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir( int(input_id), input_name, input_endereco, input_telefone)
            st.success('Cliente incluido com sucesso')