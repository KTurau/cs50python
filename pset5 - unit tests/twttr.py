# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str
# as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose
# names should begin with test_ so that you can execute your tests with:


def main():
    x = input("Input: ")
    x = shorten(x)
    print(x)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # vowels = ['a','e','i','o','u',]
    for i in vowels:
        if i in word:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
