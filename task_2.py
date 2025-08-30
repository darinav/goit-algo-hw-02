from collections import deque

def check_palindrome(word) -> bool:
    cleaned = "".join(ch.lower() for ch in word if ch.isalnum())
    de_queue = deque(cleaned)

    while len(de_queue) > 1:
        if de_queue.popleft() != de_queue.pop():
            return False
    return True


def main():
    user_input = input("Enter word or phrase: ")
    if check_palindrome(user_input):
        print("Palindrome!")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    main()