import pandas as pd
import streamlit as st
import altair as alt
#from PIL import Image

#page title
#image= Image.open("C:\Users\rdrl\testsl\dna.jpeg")
#st.image(image,use_column_width=True)
st.write("""
         # app to count nucleotide composition
         """)

#input text box
st.header("enter DNA sequence")
sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGT"
#sequence_input = input()
sequence = st.text_area("Enter sequence in FASTA format:", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] #skips first line
sequence = ''.join(sequence) #concatenates list to string
st.write("""***""")

#prints input DNA sequence
st.header('Input (DNA Query)')
sequence

#DNA nucleotide count
st.header('Output (DNA Nucleotide Count)')

#1. print dictionary
st.subheader('1. Dictionary')
with st.expander("display dictionary"):
    def DNA_nucleo_count(seq):
        d = dict([('A',seq.count('A')),
                  ('T',seq.count('T')),
                  ('G',seq.count('G')),
                  ('C',seq.count('C'))])
        return d

    X = DNA_nucleo_count(sequence)
    X_label = list(X)
    X_values = list(X.values())
    X
#2. print text
st.subheader('2. Text')
with st.expander("display text"):
    st.write('No. of adenine bases is', str(X['A']))
    st.write('No. of thymine bases is', str(X['T']))
    st.write('No. of guanine bases is', str(X['G']))
    st.write('No. of cytosine bases is', str(X['C']))

#3. Display dataframe
st.subheader("3. DataFrame")
with st.expander("display dataframe"):
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0:'count'},axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'nucleotide'})
    st.write(df)

#4. Bar chart using  Altair
st.subheader("4. Bar Chart")
with st.expander("display bar chart"):
    p = alt.Chart(df).mark_bar().encode(x='nucleotide',y='count')
    p = p.properties(width=alt.Step(80))  #width of bar
    st.write(p)

#5. G+C content
st.header("5. G+C Content")
with st.expander("calculate G+C content"):
    atgc= len(sequence)
    gc=X['G']+X['C']
    gc_cont= (gc/atgc)*100
    st.write('G+C content in input sequence is',gc_cont,"%")