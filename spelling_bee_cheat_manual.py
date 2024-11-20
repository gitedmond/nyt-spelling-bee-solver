from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import nltk
from nltk.corpus import words

nltk.download('words')

letters = ['T', 'R', 'C', 'E', 'Y', 'I', 'K'] #input your own ([0] has to be the important letter)

def find_valid_words(letters):
    important_letter = letters[0].lower()
    letters = [c.lower() for c in letters]
    word_list = words.words()
    
    valid_words = []
    for word in word_list:
        word = word.lower()
        if len(word) >= 4 and important_letter in word and all(c in letters for c in word):
            valid_words.append(word)

    valid_words.sort(key=len, reverse=True)
    
    return valid_words

print("Letters:", letters)

if letters:
    valid_words = find_valid_words(letters)
    print(f"Valid words: {valid_words}")
else:
    print("No letters were found.")
