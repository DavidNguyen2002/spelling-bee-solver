def solve():
    file = open("30k.txt", "r")
    x = input("Give center letter: ")
    s = input("Give rest of letters: ")
    ans = list()

    for word in file:
        # Remove whitespace
        word = word.strip()

        # Only >3 letter words are valid
        if len(word) < 4:
            continue

        use_center = False
        for letter in word:
            if letter == x:
                use_center = True
            elif letter not in s:
                break
        else:
            if use_center:
                ans.append(word)
    file.close()
    return ans

if __name__ == "__main__":
    print(solve())