import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random

# Download NLTK data (run this only once)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

def read_activities_from_file(file_name):
    with open(file_name, 'r') as file:
        activities = file.readlines()
    return [activity.strip() for activity in activities]

def mood_o_meter(user_mood, activities):
    # Analyze sentiment
    sentiment_score = sia.polarity_scores(user_mood)
    compound_score = sentiment_score['compound']

    # Display mood-repairing activities only when the mood score is less than or equal to 5
    if compound_score <= 0:
        st.write("\nIt seems like you're feeling a bit down. Here are some mood-repairing activities:")
        # Randomly select 3 mood-repairing activities
        random_activities = random.sample(activities, 3)

        # Display 3 random mood-repairing activities
        for i, activity in enumerate(random_activities):
            st.write(f"{i + 1}. {activity}")
    else:
        st.write("\nYour mood seems positive today! Keep it up!")

# Streamlit app layout
def main():
    st.title("Welcome to Mood-O-Meter!")
    
    # Read activities from the file
    activities_file = "Activities.txt"
    activities = read_activities_from_file(activities_file)

    # Ask user for their mood
    user_mood = st.text_input("How are you feeling today? Please describe your mood:")
    if user_mood != "":
        # Check mood and show results when user clicks the button
        if st.button("Check Mood"):
            mood_o_meter(user_mood, activities)

# Run the Streamlit app
if __name__ == "__main__":
    main()
