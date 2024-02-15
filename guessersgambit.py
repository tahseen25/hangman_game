import random
import time

flower_words = ["rose", "tulip", "sunflower", "lily", "lotus", "jasmine", "hibiscus", "daisy", "gazania", "aster", "marigold", "orchid","carnation","dahlia","anemone","chrysanthemum","cactus","poppy","iris","periwinkle"]
hangman_figures = ['''
    ''',
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    '''
]

def select_word():
    return random.choice(flower_words)

def get_hints(word):
    hints = {
        "rose": [
            "It comes in various colors, including red, pink, white, yellow, and even black.",
            "It is a classic flower often associated with love and romance.",
            "It is commonly used in cosmetic and skincare products due to its soothing and moisturizing properties.",
            "It imparts a delicate floral flavor to ice cream.",
            "It has been the subject of poetry, literature, and art throughout history."
        ],
        "tulip": [
            "It is known for its vibrant colors and cup-shaped blooms.",
            "It can be found in a range of colors, such as red, pink, yellow, purple, and white.",
            "It is commonly associated with the Netherlands and is their national flower.",
            "It is known for its characteristic shape, with six petals and a long, slender stem.",
            "The name of this flower is derived from a Persian word meaning 'turban'."
        ],
        "sunflower": [
            "Bees are attracted to this flower due to its abundant nectar.",
            "This flower can grow to be very tall, often reaching heights of 6 to 12 feet.",
            "It is often associated with happiness, positivity, and the arrival of summer.",
            "Van Gogh famously painted a series of still-life paintings featuring this flower.",
            "Its scientific name is 'Helianthus annuus.'"
        ],
        "lily": [
            "It is commonly associated with purity and innocence.",
            "The flowers of this plant are often trumpet-shaped.",
            "It is often used in floral arrangements and bouquets.",
            "Some species of this flower are native to Asia, Europe, and North America.",
            "It is a popular choice for gardens and landscaping."
        ],
        "lotus": [
            "It is often depicted in art and mythology.",
            "The flower has symbolic significance in Buddhism and Hinduism.",
            "It is associated with purity, enlightenment, and spiritual growth.",
            "The flower has large, showy petals that are typically pink or white.",
            "It is known for its ability to grow in muddy or murky waters."
        ],
        "jasmine": [
            "This flower is often used in religious ceremonies and symbolizes purity and divinity.",
            "It is known as the 'Queen of the Night' due to its intense fragrance that becomes more potent after dark.",
            "The name of this flower is derived from the Persian word meaning 'gift from God.'",
            "These flowers are often used to make essential oils that have been used in traditional medicine for centuries.",
            "This flower's fragrance is commonly used in perfumes and teas, and it blooms at night."
        ],
        "hibiscus": [
            "This flower is famous for its vibrant and eye-catching colors, including shades of red, pink, and yellow.",
            "It is the national flower of several countries and is often used in herbal teas.",
            "The flower has trumpet-shaped blooms and is associated with beauty and delicate femininity.",
            "This plant thrives in warm climates and is commonly found in tropical regions.",
            "Hummingbirds and butterflies are often attracted to this flower due to its nectar-rich blossoms."
        ],
        "daisy": [
            "Known for its simple and cheerful appearance, this flower has a yellow center and white petals.",
            "It symbolizes innocence and is associated with new beginnings.",
            "This flower is commonly found in meadows, fields, and gardens.",
            "The name of this flower comes from an Old English word meaning 'day's eye.'",
            "It is often used to create chains and flower crowns."
        ],
        "gazania": [
            "This flower hails from South Africa and is renowned for its vibrant and striking colors.",
            "It blooms during the day and closes at night or on cloudy days.",
            "This plant is known for its ability to thrive in harsh environmental conditions.",
            "Its colorful blooms are often used as ground cover or in rock gardens.",
            "This flower symbolizes resilience and strength."
        ],
        "aster": [
            "This flower stands out with its star-shaped blooms in various colors.",
            "It is commonly seen during the fall season.",
            "Associated with love and elegance, it attracts butterflies and bees.",
            "The name of this flower is derived from a Greek word meaning 'star.'",
            "They are often used to celebrate fond remembrance and the joy of life."
        ],
        "marigold": [
            "This flower is known for its bright and vibrant colors, including shades of orange and yellow.",
            "It is often used in religious ceremonies and festivals.",
            "This plant is believed to have protective properties in gardens, keeping pests away.",
            "The name of this flower is associated with the Virgin Mary.",
            "It symbolizes warmth, happiness, and positive energy."
        ],
        "orchid": [
            "This flower is renowned for its exotic beauty and comes in thousands of different species.",
            "They are found in diverse habitats, from tropical rainforests to deserts.",
            "They have intricate patterns and vibrant colors, making them highly desirable.",
            "Someof these flowers are epiphytes, growing on trees without harming them.",
            "They have a long lifespan and can bloom for weeks or even months."
        ],
        
        "carnation": [
            "It is known for its ruffled petals and spicy fragrance.",
            "It is a popular cut flower and is often used in bouquets and floral displays.",
            "In some cultures, it is associated with Mother's Day and is given as a symbol of love and gratitude.",
            "It has been cultivated for thousands of years and has a rich history.",
            "It is available in a wide range of colors, including red, pink, white, and yellow."
        ],
        "dahlia": [
            "It is native to Mexico and is the national flower of Mexico.",
            "It comes in a wide variety of shapes, sizes, and colors.",
            "It is known for its intricate and symmetrical flower heads.",
            "It is a popular choice for gardeners and is often grown for its showy blooms.",
            "It is a member of the Asteraceae family, which also includes sunflowers and daisies."
        ],
        "anemone": [
            "It is a perennial flower that belongs to the buttercup family.",
            "It is often found in shades of white, pink, purple, and blue.",
            "Its name is derived from the Greek word meaning 'windflower'.",
            "It is known for its delicate, daisy-like flowers.",
            "It is associated with anticipation and is sometimes called the 'flower of expectation'."
        ],
        "chrysanthemum": [
            "It is native to Asia and is particularly popular in Japan and China.",
            "It symbolizes autumn and is often associated with longevity and joy.",
            "It is available in a wide range of colors and flower forms.",
            "It is often used in floral arrangements, especially during festivals and celebrations.",
            "It is one of the 'Four Gentlemen' in traditional East Asian art, along with plum, orchid, and bamboo."
        ],
        "cactus": [
            "This plant is known for its ability to store water in its thick, fleshy stems.",
            "It is adapted to survive in arid and desert regions.",
            "This plant comes in various shapes and sizes, with some species having spines or thorns.",
            "It is a low-maintenance plant and requires minimal watering.",
            "This plant is commonly found in dry and sandy environments."
        ],
        "iris": [
            "This flower is known for its striking blooms and sword-like leaves.",
            "It comes in various colors, including purple, blue, and white.",
            "This flower is associated with wisdom, valor, and faith.",
            "It is commonly used in gardens, floral arrangements, and as a symbol of royalty.",
            "This flower has been admired for its beauty and elegance since ancient times."
        ],
        "poppy": [
            "This flower is known for its vibrant red petals and black center.",
            "It is associated with remembrance, peace, and sleep.",
            "This flower is commonly used in gardens, floral arrangements, and as a symbol of fallen soldiers.",
            "It is also the source of opium, which has both medicinal and recreational uses.",
            "This flower has cultural significance in various countries around the world."
        ],
        "periwinkle":[
            "This flower is often used as ground cover due to its trailing growth habit and dense foliage.",
            "It is known for its small, star-shaped flowers that come in shades of blue, purple, or white.",
            "They are resilient plants that can tolerate various soil and light conditions.",
            "The leaves of this flower are glossy and dark green, providing an attractive contrast to the blooms.",
           "It is a popular choice for borders, rock gardens, and landscaping due to its low maintenance nature."
        ]
    }
    return hints.get(word, [])

def play_hangman():
    print("\nLet's play Hangman game!\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\n")
    time.sleep(1)

    score = 0

    while True:
        word = select_word()
        hint_list = get_hints(word)
        hint_count = 0
        guesses = []
        attempts = 7
        guessed_word = ['_'] * len(word)
        hangman_state = 0

        print(f"\nWelcome to Hangman - Flower Edition, {name}!")
        print("Guess the letters to uncover the flower name.")
        print("You have 7 attempts to guess the word.")
        time.sleep(2)

        while True:
            print("\nWord:", " ".join(guessed_word))
            print("Attempts Remaining:", attempts)
            print("Guessed Letters:", " ".join(guesses))
            print(hangman_figures[hangman_state])

            if attempts == 0:
                print("You ran out of attempts! The flower was", word)
                break

            if '_' not in guessed_word:
                score += 1
                print("Congratulations! You guessed the flower correctly:", word)
                print(f"Your score is {score}")
                break

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue

            if guess in guesses:
                print("You already guessed that letter!")
                continue

            guesses.append(guess)

            if guess in word:
                print("Correct guess!")
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
            else:
                attempts -= 1
                hint_count += 1
                hangman_state += 1
                print("Incorrect guess!")
                if hint_count <= len(hint_list):
                    print("Hint: ", "\033[1m" + hint_list[hint_count - 1] + "\033[0m")
                    time.sleep(3)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print(f"\nThank you for playing Hangman, {name}!")
    print(f"Your final score is {score}.")

play_hangman()
