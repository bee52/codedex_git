problem = "problem6"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

import pandas as pd
import string
from collections import deque
import random
#import networkx as nx

def text_analyser(user_text):
    # your code here, takes a user's text and 
    # displays a list of options for analysing the 
    # input text

    # Read file
    with open(user_text, "r", encoding="utf-8") as file:
        text = file.read()

    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()

    word_graph = {}
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        if word1 not in word_graph:
            word_graph[word1] = set()
        word_graph[word1].add(word2)

    # computing word frequency
    word_freq = pd.Series(words).value_counts()

    df = pd.DataFrame({
        "Frequency": word_freq,
        "Unique Neighbours": [len(word_graph.get(word, set())) for word in word_freq.index]        
    })

    def find_shortest_path(word_graph, word1, word2):
        if word1 not in word_graph or word2 not in word_graph:
            return "One or both words are not in the text."

        queue = deque([(word1, [word1])])
        visited = set([word1])

        while queue:
            current_word, path = queue.popleft()

            if current_word == word2:
                return path
            
            for neighbour in word_graph.get(current_word, []):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))
                    visited.add(neighbour)
        
        return "No such path exixsts."
    
    def generate_sentence(word_graph, start_word=None, max_length=20):
        if start_word not in word_graph:
            return "The start word is not in the text."

        if not start_word:
            start_word = random.choice(list(word_graph.keys()))

        sentence = [start_word]
        current_word = start_word

        for _ in range(max_length - 1):
            neighbours = list(word_graph.get(current_word, []))
            if not neighbours:
                break

            current_word = random.choice(neighbours)
            sentence.append(current_word)

        return " ".join(sentence) + "."
    
    def longest_word_chain(word_graph):
        def dfs(word, visited):
            if word in visited:
                return visited
            longest_path = visited
            for neighbour in word_graph.get(word, []):
                new_path = dfs(neighbour, visited + [neighbour])
                if len(new_path) > len(longest_path):
                    longest_path = new_path
            return longest_path
        
        longest_chain = []
        for word in word_graph:
            path = dfs(word, [word])
            if len(path) > len(longest_chain):
                longest_chain = path

        return longest_chain if longest_chain else "No word chain found."

    print("\nChoose between the following options: ")
    print("1) Number of distinct words")
    print("2) Most frequent word in the text")
    print("3) Word with the largest number of unique neighbours")
    print("4) Word with the least number of unique neighbours")
    print("5) Other descriptive statistics")
    print("6) Find Shortest path between two words")
    print("7) Generate a random sentence")
    print("8) Find the longest word chain")

    choice = input("\n Enter your choice: ")

    result = None

    if choice == "1":
        result = len(word_freq)
    
    elif choice == "2":
        most_freq_word = word_freq.idxmax()
        result = (most_freq_word, word_freq[most_freq_word])
    
    elif choice == "3":
        max_neighbour_word = df["Unique Neighbours"].idxmax()
        result = (max_neighbour_word, df.loc[max_neighbour_word, "Unique Neighbours"])
    
    elif choice == "4":
        min_neighbour_word = df[df["Unique Neighbours"] > 0]["Unique Neighbours"].idxmin()
        result = (min_neighbour_word, df.loc[min_neighbour_word, "Unique Neighbours"])
    
    elif choice == "5":
        result = df.describe()
    
    elif choice == "6":
        word1 = input("Enter the first word: ").lower()
        word2 = input("Enter the second word: ").lower()
        result = find_shortest_path(word_graph, word1, word2)
    
    elif choice == "7":
        start_word = input("Enter a start word: ").lower()
        start_word = None if start_word == "" else start_word
        result = generate_sentence(word_graph, start_word)
    
    elif choice == "8":
        result = longest_word_chain(word_graph)

    else:
        return "Invalid choice"

    print(result)


    #print('text_analyser not implemented')

text_analyser("RedAndBlack.txt")