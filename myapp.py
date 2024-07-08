import streamlit as st
import pickle

model = pickle.load(open('mymodel.pkl','rb'))

st.title("Iris Flower Classification using Decision Tree")

sl = st.number_input("Sepal Length")
sw = st.number_input("Sepal Width")
pl = st.number_input("Petal Length")
pw = st.number_input("Petal Width")

def prediction():
    output = model.predict([[sl,sw,pl,pw]])
    return output[0]

if st.button("Predict Class"):
    output = prediction()
    st.write("Class of Flower:")
    if output ==0:
        st.write("Iris-Setosa")
    elif output==1:
        st.write("Iris-Versicolour")
    else:
        st.write("Iris-Virginica")