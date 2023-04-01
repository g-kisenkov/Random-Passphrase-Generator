# Random Passphrase Generator (fully ChatGPT-generated codebase)

This script generates a random passphrase consisting of a specified number of words chosen from the Electronic Frontier Foundation's (EFF) large wordlist ([https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)). The passphrase is generated by rolling a set of dice using the Random.org API and using the resulting numbers to index words from the wordlist.

## Usage

1. Make sure that you have created and activated a Python virtual environment.
2. Install the required `requests` library by running `pip install -r requirements.txt`.
3. Obtain a free API key for the Random.org API by signing up for a Random.org account at [https://api.random.org/api-keys/beta](https://api.random.org/api-keys/beta).
4. Set the `apiKey` variable in the script to your API key.
5. Run the script.
6. Enter the desired number of words in the passphrase when prompted.

The script will generate a set of random numbers by rolling virtual dice using the Random.org API. These numbers are used to index words from the EFF wordlist, resulting in a passphrase consisting of the specified number of words.

## About

This script is based on the idea of using random words from a large wordlist to create strong and memorable passphrases, as advocated by the EFF in their blog post "New Wordlists for Random Passphrases" ([https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)).
