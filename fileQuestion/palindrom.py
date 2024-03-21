def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def main(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        for line in f_input:
            # Remove leading/trailing whitespaces and newline characters
            word = line.strip()
            if is_palindrome(word):
                f_output.write(f"{word} is a palindrome.\n")
            else:
                f_output.write(f"{word} is not a palindrome.\n")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)
