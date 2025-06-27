# Hindi to English Dictionary in this project when you enter a hindi word in english like pani it translates it to water

# Step 1: Get user input
word = input("Write a Hindi word: ") 


# Step 2: Create a dictionary
hindi_to_english = {
     "pani": "water",
     "aag": "fire",
     "ghar": "house",
     "billi": "cat",
     "kutta": "dog",
     "namaste": "hello",
     "dhanyavad": "thank you",
     "khushi": "happiness",
     "khana": "food",
     "kitab": "book"
}


# Step 3: Translate
if word in hindi_to_english:
    print("In English:", hindi_to_english[word])
else:
    print("Word not found in dictionary")
