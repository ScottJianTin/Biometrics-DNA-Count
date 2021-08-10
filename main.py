import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

########## PAGE TITLE ##########
image = Image.open("dna-logo.jpg")
st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

########## INPUT TEXT BOX ##########
st.header("Enter DNA sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250) # place text_area at the side
sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = sequence.splitlines() # split sequence_input with "\n"
# sequence
sequence = sequence[1:] # ignore first element (">DNA Query 2")
# sequence
sequence = "".join(sequence) # combine the rest of lines into one string of text
# sequence

st.write("""
***
""")

## Print the input DNA sequence
st.header("INPUT (DNA Query)")
sequence

st.write("""
***
""")

## DNA Nucleotide Count
st.header("OUPUT (DNA Nucleotide Count)")

## 1. Print Dictionary
st.subheader("1. Print Dictionary")
def DNA_Nucleotide_Count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C"))
    ])
    return d

X = DNA_Nucleotide_Count(sequence)
X

## 2. Print Text
st.subheader("2. Print Text")
st.write(f"""
The DNA sequence consists of:
* {X["A"]} *Adenine (A)* 
* {X["T"]} *Thymine (T)*
* {X["G"]} *Guanine (G)*
* {X["C"]} *Cytosine (C)*
""")

## 3. Display Dataframe
st.subheader("3. Display Dataframe")
df = pd.DataFrame.from_dict(X, orient="index")
# df
df = df.rename({0:"count"}, axis=1)
# df
df.reset_index(inplace=True)
# df
df = df.rename({"index": "nucleotide"}, axis=1)
df

## 4. Display Bar Chart
st.subheader("4. Display Bar Chart")
graph = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)
# graph
graph = graph.properties(
    width=alt.Step(50) # control bar width
)
graph