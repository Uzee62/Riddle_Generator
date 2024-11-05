import csv
import random
import streamlit as st

def load_riddles():
    riddles = []
    try:
        with open('Riddles.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if all(field in reader.fieldnames for field in ['Riddle', 'Hint', 'Answer']):
                for row in reader:
                    riddles.append(row)
            else:
                st.write("CSV file is missing one or more required columns: 'Riddle', 'Hint', 'Answer'")
    except Exception as e:
        st.write(f"Error loading riddles: {e}")
    return riddles

def get_random_riddle(riddles):
    return random.choice(riddles) if riddles else None
