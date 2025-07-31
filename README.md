# bigram-model



Neural Bigram Language Model

This project is a simple Neural Bigram Language Model built using PyTorch. It takes a starting word and a desired output length, then generates text one word at a time — trained on just 3 lines of text.

## What It Does

Learns bigram (2-word) relationships from a small dataset

Uses an embedding layer and a fully connected layer

Predicts the next word based on the current one

Generates a complete sequence of words using the trained model


## Example Features

Input: starting word (e.g., "Once")

Input: length (e.g., 10)

Output: "Once upon a time there was a little dog that..."

Trained on minimal text — perfect for learning and experimentation


## Built With

Python

PyTorch

Neural Networks (Embedding + Linear layers)

Custom tokenizer and vocabulary builder


## How It Works

1. Build vocabulary from the text


2. Create bigram pairs (current word → next word)


3. Convert words to tensors using embeddings


4. Train a small neural network


5. Generate words step-by-step





## Future Ideas

Trigram or n-gram extension

Train on larger story/text datasets

Add punctuation handling

Web interface using Gradio or Flask


## Author

Made by ### DINESH RAMPA 



