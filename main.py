import nltk
# download nltk data
nltk.download("wordnet")
nltk.download("punkt")
stemmer = nltk.stem.LancasterStemmer()

import numpy as np
import tensorflow as tf
import pickle
import random
import json
import matplotlib.pyplot as plt
from functions import updateEQ

# Intents
intents = json.load(open("intents.json", "r"))

# Vars
words = []
classes = []
documents = []
ignore_words = ["?"]

# loop sentence
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stemming
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# sorting class
classes = sorted(list(set(classes)))

# create training data
training = []
output_empty = [0] * len(classes)

# train set
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
epochs = 120

# train x, y
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Create model
def trainAndSave():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))

    adam = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6, amsgrad=True)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    history = model.fit(np.array(train_x), np.array(train_y), epochs=epochs, batch_size=32, verbose=1)
    
    # Plotting
    loss = history.history['loss']
    accuracy = history.history['accuracy']
    epochs_ranges = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_ranges, accuracy, label='Training Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_ranges, loss, label='Training Loss')
    plt.legend(loc='upper right')
    plt.title('Training Loss')
    
    plt.savefig("plot.png")
    
    model.save("models/tensor_model.h5")
    pickle.dump({ "words": words, "classes": classes, "train_x": train_x, "train_y": train_y }, open(f"models/data.pkl", "wb"))

