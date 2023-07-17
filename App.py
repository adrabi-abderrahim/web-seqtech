import streamlit as st
from qiskit import *
import numpy as np
from quantum_dna_encoding import *


st.title('Classical-to-Quantum App Sequence Encoding App: NZ-SeQTech')
st.markdown('Zaiku Group Ltd. / Quantum Formalism')
st.markdown("7th Floor, 4 St Paul's Square, Liverpool L3 9SJ, United Kingdom")

st.markdown('----')
st.write('This is an early prototype to have a general overview of the most **important** features the final product.')
st.markdown('----')

dna_seq = st.text_input('Enter the DNS sequence')
encoding_options = ('Amplitude Encoding', 'Cosine Encoding')
encoding_type = st.selectbox('Select the encoding', options=range(len(encoding_options)), format_func=lambda x: encoding_options[x])
visualizations_options = ('Bloch Multivector', 'State Hinton', 'State City', 'State Paulivec')
visualizations_type = st.selectbox('Select the visualization type', options=range(len(visualizations_options)), format_func=lambda x: visualizations_options[x])

st.markdown('----')

qc = None

if dna_seq:
    dna_seq = dna_seq.upper()
    if is_valid_dna_seq(dna_seq):
        if encoding_type == 0:
            qc = amplitude_encoding(dna_seq.upper())
        elif encoding_type == 1:
            qc = cosine_encoding(dna_seq.upper())
    else:
        st.write('**Invalid DNA sequence! Please check the sequence again.**')

if qc:

    st.markdown('---')
    st.markdown(f'The quantum circut of the encoding: **{encoding_options[encoding_type]}**')
    fig = qc.draw('mpl', scale=0.5)
    st.pyplot(fig, use_container_width=False)
    
    st.markdown('---')
    st.markdown(f'The visualization of type: **{visualizations_options[visualizations_type]}**')
    state_vec = get_statevector(qc)
    if visualizations_type == 0:
        fig = visualize_bloch_multivector(state_vec)
        #fig.set_figheight(2)
        #fig.set_figwidth(value_width)
    elif visualizations_type == 1:
        fig = visualize_state_hinton(state_vec)
    
    elif visualizations_type == 2:
        fig = visualize_state_city(state_vec)

    elif visualizations_type == 3:
        fig = visualize_state_paulivec(state_vec)

    st.pyplot(fig)


    
    







