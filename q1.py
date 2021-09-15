##imports
import streamlit as st
import pandas as pd
import pickle


##read in data
housing = pd.read_csv("housing.csv")
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]

### Displaying text
##The title of your App can be displayed with st.title
st.title("Housing Price Predictions")  # you could also use st.write("# YOURTITLE")

### Displaying an image
## st.image allows you to display an image from a url or numpy array, a BytesIO object and more
st.image(
    "https://storage.googleapis.com/kaggle-datasets-images/24824/31630/a5f5ce1e4b4066d1f222e79e8286f077/dataset-cover.jpg?t=2018-05-03-00-52-48",
    width=700)

##st.write allows you to write text either with single quotes for one line in markdown format
st.write("Predicting the median value of a house within a district.")
##or with triple quotes for multiple lines
###Displaying data
st.write("# Displaying Data")
##display dataframe
##add column selector
col_names = housing.columns.tolist()
st.dataframe(housing[st.multiselect("Columns to display",col_names, default = col_names)])

st.write("Locations on Map")

st.map(housing, zoom = 4.5)


###Machine Learning
st.write("# Machine Learning App")
ml_model = pickle.load(open("model.pkl", "rb")) #load the model

##create the sidebar
st.sidebar.header("User Input Parameters")

##create function for User input
def get_user_input():
    housing_median_age = st.sidebar.slider("How old is the median house in the district?",
                          int(housing["housing_median_age"].min()),
                          int(housing["housing_median_age"].max()),
                          1)

    households = st.sidebar.slider("How many households are in the district?",
                          int(housing["households"].min()),
                          int(housing["households"].max()),
                          1)
    median_income = st.sidebar.slider("What is the median income in the district?",
                           housing["median_income"].min(),
                           housing["median_income"].max(),
                           1.0)
    ocean_proximity = st.sidebar.slider("What is the ocean proximity? (0->Island and 4->Inland)",
                                      0,
                                      4,
                                      1)
    features = pd.DataFrame({"housing_median_age": housing_median_age,
                             "households": households,
                             "median_income": median_income,
                             "ocean_proximity": ocean_proximity}, index = [0])
    return features

input_df = get_user_input() #get user input from sidebar
prediction = ml_model.predict(input_df) #get predicitions

#display predictions
st.subheader("Prediction")
st.write("**The median price of a house in the district is: $**",str(round(prediction[0],2)))
