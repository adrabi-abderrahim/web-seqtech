import streamlit as st
from quantum_dna_encoding import is_valid_dna_seq
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

st.title('DNA Data Analytics')
st.markdown('---')

dna_seq = st.text_area('DNA squence')

st.markdown('---')


if dna_seq:
    dna_seq = dna_seq.upper()
    dna_seq = ''.join(dna_seq.split())

    if is_valid_dna_seq(dna_seq):
        base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

        for base in dna_seq:
            if base in base_counts:
                base_counts[base] += 1
            else:
                base_counts['Other'] += 1

        # Task 1: Pie chart of base counts
        st.markdown('## Task 1: Pie chart of base counts')
        labels = base_counts.keys()
        counts = list(base_counts.values())

        fig = plt.figure(figsize=(6, 6))
        plt.pie(counts, labels=labels, autopct='%1.1f%%')
        plt.title('Base Counts')

        st.pyplot(fig)
        st.markdown('---')

        # Task 2: Bar graph of base probabilities
        st.markdown('## Task 2: Bar graph of base probabilities')
        total_bases = sum(counts)
        probabilities = [count / total_bases for count in counts]

        fig = plt.figure(figsize=(8, 6))
        plt.bar(labels, probabilities)
        plt.xlabel('Bases')
        plt.ylabel('Probability')
        plt.title('Base Probability Distribution')

        st.pyplot(fig)
        st.markdown('---')

        # Task 3: Count of other symbols or numbers
        #st.markdown('## Task 3: Count of other symbols or numbers')
        #other_count = base_counts['Other']
        #st.markdown(f'Count of other symbols or numbers: **{other_count}**.')

        # Task 4: Line graph of base counts
        st.markdown('## Task 4: Line graph of base counts')
        fig = plt.figure(figsize=(8, 6))
        x = np.arange(len(labels))
        plt.plot(x, counts, marker='o', linestyle='-', linewidth=2)
        plt.xticks(x, labels)
        plt.xlabel('Bases')
        plt.ylabel('Count')
        plt.title('Base Count Distribution')
        st.pyplot(fig)
        st.markdown('---')

        # Task 5: Expectation value of each base
        st.markdown('## Task 5: Expectation value of each base')
        expectation_values = {base: count / total_bases for base, count in base_counts.items()}
        for i, (k, v) in  enumerate(expectation_values.items()):
            st.markdown(f'Expectation value of {k}: **{v:0.2f}**.')

        # Task 6: Variance
        st.markdown('## Task 6: Variance')
        variance = np.var(counts)
        st.markdown(f'Variance: **{variance:0.2f}**.')

        # Task 7: Standard deviation
        st.markdown('## Task 7: Standard deviation')
        std_deviation = np.std(counts)
        st.markdown(f'Standard deviation: **{std_deviation:0.2f}**.')

        # Task 8: Covariance
        st.markdown('## Task 8: Covariance')
        covariance = np.cov(counts)
        st.markdown(f'Covariance: **{covariance:0.2f}**.')

        # Task 9: Correlation
        st.markdown('## Task 9: Correlation')
        correlation = np.corrcoef(counts)
        st.markdown(f'Correlation: **{correlation:0.2f}**.')

        # Task 10: Skewness
        st.markdown('## Task 10: Skewness')
        data_skewness = skew(counts)
        st.markdown(f'Skewness: **{data_skewness:0.2f}**.')

        # Task 11: Kurtosis
        st.markdown('## Task 11: Kurtosis')
        data_kurtosis = kurtosis(counts)
        st.markdown(f'Kurtosis: **{data_kurtosis:0.2f}**.')
    else:
        st.markdown('**The DNA sequence is invalid.**')
        
    