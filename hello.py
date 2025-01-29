# deep.py

def main():
    # Prompt the user for input
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip()
    
    # Check if the input matches '42', 'forty-two', or 'forty two' (case-insensitive)
    if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
        print("Yes")
    else:
        print("No")

# Call the main function if this script is run
if __name__ == "__main__":
    main()

