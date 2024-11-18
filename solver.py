from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import nltk
from nltk.corpus import words

nltk.download('words')

def get_spelling_bee_letters():
    service = Service(r"path/to/chromdriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.nytimes.com/puzzles/spelling-bee")

        try:
            play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'pz-moment__button') and text()='Play']"))
            )
            play_button.click()
            print("Play button clicked!")
        except Exception as e:
            print("Could not find or click the 'Play' button:", e)
            return []

        time.sleep(1)
        letter_elements = driver.find_elements(By.CLASS_NAME, "cell-letter")
        letters = [letter.text.lower() for letter in letter_elements]

    finally:
        driver.quit()

    return letters

def find_valid_words(letters):
    important_letter = letters[0]
    word_list = words.words()
    
    valid_words = []
    for word in word_list:
        word = word.lower()
        if len(word) >= 4 and important_letter in word and all(c in letters for c in word):
            valid_words.append(word)
    
    return valid_words

letters_list = get_spelling_bee_letters()
print("Letters:", letters_list)

if letters_list:
    valid_words = find_valid_words(letters_list)
    print(f"Valid words: {valid_words}")
else:
    print("No letters were found.")
