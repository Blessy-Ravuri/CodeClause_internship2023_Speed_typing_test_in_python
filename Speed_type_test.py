import time

def speed_typing_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    
    print("Welcome to the Speed Typing Test!")
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    
    user_input = input(f"\nType the following text:\n{prompt_text}\n")
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = (len(prompt_text.split()) / elapsed_time) * 60
    
    if user_input == prompt_text:
        print(f"\nCongratulations! You typed it correctly.")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
    else:
        print("\nOops! Your typing is not correct. Please try again.")

if __name__ == "__main__":
    speed_typing_test()
