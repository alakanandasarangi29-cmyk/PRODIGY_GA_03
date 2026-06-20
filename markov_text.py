import random

with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

markov_chain = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in markov_chain:
        markov_chain[word] = []

    markov_chain[word].append(next_word)

current_word = random.choice(words)
generated_text = [current_word]

for _ in range(20):
    if current_word in markov_chain:
        current_word = random.choice(markov_chain[current_word])
        generated_text.append(current_word)
    else:
        break

result = " ".join(generated_text)

print("\nGenerated Text:\n")
print(result)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(result)
