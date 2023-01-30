def palindrome(word, left_index, right_index=-1):
    if left_index == len(word) // 2:
        return f"{word} is a palindrome"
    elif word[left_index] != word[right_index]:
        return f"{word} is not a palindrome"
    else:
        return palindrome(word, left_index + 1, right_index - 1)


# print(palindrome("abcba", 0))
# # print(palindrome("peter", 0))


# def palindrome(word, index=0):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))
# # print(palindrome("peter", 0))
