problem = "problem4"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

import string

def make_change(coin_vals, change):
    # your code here, returns an int which represents num_coins
    dp = [float('inf')] * (change + 1)
    dp[0] = 0 # Base case 

    for amount in range(1, change + 1):     #iterating throught the table
        for coin in coin_vals:      # iterating through the coin_vals
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)     #updating the table with the minumum coin value

    return dp[change]

    print('make_change not implemented')
    

def make_change2(coin_vals, change):
    # your code here, returns a list of 
    # the coins that make the optimal change
    dp = [float('inf')] * (change + 1)
    dp[0] = 0

    coin_used = [0] * (change + 1)

    for amount in range(1, change + 1):
        for coin in coin_vals:
            if amount >= coin and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                coin_used[amount] = coin

    coins = []
    curr_amount = change
    while curr_amount > 0:
        coin = coin_used[curr_amount]
        coins.append(coin)
        curr_amount -= coin
    
    return dp[change], coins

    print('make_change2 not implemented')
    

def word_break(dictionary, string_to_segment):
    # your code here
    n = len(string_to_segment)
    dp = [False] * (n + 1)
    dp[0] = True

    backtrack = [None] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and string_to_segment[j:i] in dictionary:
                dp[i] = True
                backtrack[i] = j
                break
    
    if not dp[n]:
        print(string_to_segment, " cannot be segmented into words.")
        return False
    
    # Reconstructing the segmented words by backtracking through the list

    result = []
    index = n
    while index > 0:
        prev_index = backtrack[index]
        result.append(string_to_segment[prev_index:index])
        index = prev_index

    print(string_to_segment, " can be segmneted into: ", ", ".join(result))

    return True
    
    print('word_break not implemented')


#print(make_change([1, 5, 8], 11))
print(make_change2([1, 5, 8], 11))


def test_word_break():
    dictionary1 = {"apple", "pen"}
    string1 = "applepenapple"
    print(word_break(dictionary1, string1))  # Expected: True (can be segmented as "apple pen apple")

    dictionary2 = {"cats", "dog", "sand", "and", "cat"}
    string2 = "catsandog"
    print(word_break(dictionary2, string2))  # Expected: False (no valid segmentation)

    dictionary3 = {"leet", "code"}
    string3 = "leetcode"
    print(word_break(dictionary3, string3))  # Expected: True (can be segmented as "leet code")

    dictionary4 = {"a", "aa", "aaa", "aaaa"}
    string4 = "aaaaaaa"
    print(word_break(dictionary4, string4))  # Expected: True (can be segmented as "aaaa aa a")

    dictionary5 = {"hello", "world"}
    string5 = "helloworld"
    print(word_break(dictionary5, string5))  # Expected: True (can be segmented as "hello world")

    dictionary6 = {"quick", "brown", "fox"}
    string6 = "thequickbrownfox"
    print(word_break(dictionary6, string6))  # Expected: False (missing "the" in dictionary)

test_word_break()
