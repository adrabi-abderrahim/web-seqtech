import streamlit as st

st.title('Facts About Quantum Computation')
st.markdown('---')


st.markdown("""
   <p>Here are some interesting facts about Quantum Computing:</p>
        <ul>
			<li>Quantum computing is a field of computing that utilizes principles of Quantum Mechanics to perform calculations.</li>
			<li>Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits, 
			which can represent 0s, 1s, or a superposition of both simultaneously.</li>
			<li>Superposition is a fundamental property of quantum systems that allows qubits to exist in multiple states at the same time, 
			exponentially increasing computational power.</li>
			<li>Quantum computers leverage another principle called entanglement, where the states of multiple qubits become correlated and interconnected.</li>
			<li>Entanglement enables quantum computers to perform certain computations much faster than classical computers.</li>
			<li>Quantum algorithms, such as Shor's algorithm, have the potential to solve complex mathematical problems exponentially faster than classical algorithms.</li>
			<li>Quantum computers have the potential to revolutionise fields such as Cryptography, Optimisation, Drug Discovery, Material Science, and Machine Learning.</li>
			<li>Building and maintaining stable qubits is a significant challenge due to the delicate nature of quantum systems and the effects of noise and decoherence.</li>
			<li>Several companies and research institutions are actively working on developing practical quantum computers, 
			and prototypes with a small number of qubits have been built.</li>
			<li>Quantum computing is still an emerging field, and there are many open questions and challenges to overcome before fully realising its potential.</li>
		</ul>
""", unsafe_allow_html=True)