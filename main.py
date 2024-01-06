import streamlit as st
import subprocess

def run_chat_app():
    subprocess.Popen(["streamlit", "run", "community.py"])

def run_mood_o_meter_app():
    subprocess.Popen(["streamlit", "run", "mood-o-meter.py"])

def main():
    st.title("Welcome to Mood-O-Meter with Community Chat")

    st.subheader("Community Chat")
    if st.button("Open Community Chat"):
        run_chat_app()

    st.subheader("Mood-O-Meter")
    if st.button("Open Mood-O-Meter"):
        run_mood_o_meter_app()

if __name__ == '__main__':
    main()
