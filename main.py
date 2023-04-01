import requests
import csv

# Define the API endpoint URL and your API key
apiEndpoint = "https://api.random.org/json-rpc/2/invoke"
apiKey = "API_KEY_HERE"

# Define the parameters for the API request
apiParams = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": apiKey,
        "n": 5,  # Roll 5 dice at a time
        "min": 1,
        "max": 6,
        "replacement": True,
    },
    "id": 1,
}

# Load the wordlist from the EFF website
wordlistUrl = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
wordlistResponse = requests.get(wordlistUrl)
wordlistText = wordlistResponse.text
wordlistLines = wordlistText.split("\n")
wordlistLines.pop()  # Remove the last empty line
wordlist = {}
for line in wordlistLines:
    index, word = line.split("\t")
    wordlist[index] = word

# Prompt the user to enter the desired number of words in the passphrase
num_words = int(input("How many words do you want in your passphrase? "))

# Roll the dice and index words from the wordlist
passphrase = []
while len(passphrase) < num_words:
    # Make the API request
    response = requests.post(apiEndpoint, json=apiParams)
    jsonResponse = response.json()
    diceRolls = jsonResponse["result"]["random"]["data"]

    # Index words from the wordlist using the dice rolls
    wordIndex = "".join(str(roll) for roll in diceRolls)
    passphrase.append(wordlist[wordIndex])

# Print the passphrase to the console
for word in passphrase[:num_words]:
    print(word)
