import streamlit as st
import pandas as pd
import pickle


##reading dataset
housing = pd.read_csv("housing.csv")
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]

st.title("Housing Price Predictions")  


st.image(
    "https://www.architectureartdesigns.com/wp-content/uploads/2015/07/713.jpg",
    width=700)

st.write("Predicting the median value of a house in California district.")

##Displaying data
st.write("# Displaying Data")
##display dataframe
##add column selector
col_names = housing.columns.tolist()
st.dataframe(housing[st.multiselect("Columns to display",col_names, default = col_names)])

st.write("Locations on Map")

st.map(housing, zoom = 4.5)

##ML Model
st.write("# User Preferences for House")
ml_model = pickle.load(open("model.pkl", "rb")) #loading the model

##create function for User input
def get_user_input():
    housing_median_age = st.slider("How old is the median house in the district?",0,50,1)

    households = st.slider("How many households are in the district?",
                          15,
                          5000,
                          1)
    median_income = st.slider("What is the median income in the district?",
                           0.5,
                           2.5,
                           1.0)
    ocean_proximity = st.selectbox("What is the ocean proximity? (0->Island and 4->Inland)",[0,1,2,3,4])
    features = pd.DataFrame({"housing_median_age": int(housing_median_age),
                             "households": int(households),
                             "median_income": median_income,
                             "ocean_proximity": int(ocean_proximity)}, index = [0])
    return features


input_df = get_user_input() #get user input from sidebar
prediction = ml_model.predict(input_df) #get predicitions

frm = st.button("Submit")
if frm: 
    st.write("**The median price of a house is: $**",str(round(prediction[0],2)))
