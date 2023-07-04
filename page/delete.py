import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title('deletar Dados')
    
    
    with st.form(key='delet'):
        input_id = st.number_input(label= 'insira o id', format='%i')
        

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.deletar(int(input_id))
            st.success('Cliente excluido com sucesso')
