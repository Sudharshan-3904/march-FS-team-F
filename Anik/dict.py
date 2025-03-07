class DictionaryApp:
    def __init__(self):
        self.dictionary = {
            "apple": "A round fruit with red, green, or yellow skin.",
            "banana": "A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.",
            "cat": "A small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws.",
            "dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.",
            "elephant": "A large herbivorous mammal with a trunk, native to Africa and southern Asia."
        }

    def get_meaning(self, word):
        return self.dictionary.get(word.lower(), "Word not found in dictionary.")

if __name__ == "__main__":
    app = DictionaryApp()
    while True:
        word = input("Enter a word to find its meaning (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting dictionary app. Goodbye!")
            break
        meaning = app.get_meaning(word)
        print(f"{word.capitalize()}: {meaning}\n")