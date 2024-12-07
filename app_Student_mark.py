
import pickle
import streamlit as sl

# Load the model when the script runs
with open('student_marks.pkl', 'rb') as file:
    model = pickle.load(file)

sl.title("Student Mark Predictor")

# Get input from the user
a = sl.text_input("Enter the number of courses:")
b = sl.text_input("Enter the time spent studying (hours):")
sl.balloons()
# Check for input values and perform prediction
if sl.button("Submit"):
    try:
        # Convert input to appropriate type
        a = float(a)
        b = float(b)
        inp = [[a, b]]  # input should be in the form of a 2D array
        pre = model.predict(inp) 
        sl.write('Prediction : ', pre[0])
    except ValueError:
        sl.write("Please enter valid numbers for both fields.")
       