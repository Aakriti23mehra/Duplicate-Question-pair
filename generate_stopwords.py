from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import pickle

# Save the stopwords
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(ENGLISH_STOP_WORDS, f)

print("stopwords.pkl created successfully.")
