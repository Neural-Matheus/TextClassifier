# -*- coding: utf-8 -*-

"""# **Importação inicial das bibliotecas**

####Fazer a instalação das bibliotecas

```
# !pip install transformers
```
"""

!pip install transformers

!pip install jsonlines

!pip install scikit-learn

!pip install nltk

!pip install transformers[torch]

!pip install accelerate -U

"""####Fazer a importação das bibliotecas


"""

from transformers import RobertaTokenizer

import torch
import pandas as pd
import numpy as np
import tensorflow as tf
import numpy as np
import math
import re
import os
import pandas as pd
from bs4 import BeautifulSoup
import random
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

!pip install bert-for-tf2

!pip install sentencepiece

import tensorflow_hub as hub

from tensorflow.keras import layers
import bert

tf.__version__

"""## Part 1 - Data Preprocessing"""

def read_and_concatenate_dataframes(directory, new_column_name, value):
    """
    Read JSONL files in the specified directory, add a new column to each DataFrame,
    and concatenate all DataFrames into a single DataFrame.

    Parameters:
    - directory: The path to the directory containing JSONL files.
    - new_column_name: The name of the new column to be added.
    - value: The value to be assigned to the new column.

    Returns:
    A DataFrame containing all the concatenated data.
    """

    # List to store DataFrames
    data_frames_list = []

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.jsonl'):
            file_path = os.path.join(directory, file_name)

            # Read the JSONL file and add to the DataFrame list
            temp_df = pd.read_json(file_path, lines=True, encoding='latin1')

            # Add a new column with specified name and value
            temp_df[new_column_name] = value

            data_frames_list.append(temp_df)

    # Concatenate all DataFrames into a single DataFrame
    result_df = pd.concat(data_frames_list, ignore_index=True)

    return result_df

# Example usage
directory_pathG = '/content/drive/MyDrive/opengpttext-clean/chatgpt/'
directory_pathH = '/content/drive/MyDrive/opengpttext-clean/openweb/'
new_column = 'value'

# Call the function with value 1 for GPT data and value 0 for human data
data_gpt = read_and_concatenate_dataframes(directory_pathG, new_column, value=1)
data_human = read_and_concatenate_dataframes(directory_pathH, new_column, value=0)

data_human

data_gpt

data_human.shape

data_gpt.shape

# Concatenar os DataFrames em uma única variável
combined_data = pd.concat([data_gpt, data_human], ignore_index=True)
combined_data = combined_data.drop(combined_data.columns[0], axis=1)

combined_data

combined_data.head()

combined_data.tail()

def clean_text(text):
    # Remover menções a usuários
    text = re.sub(r"@[A-Za-z0-9_]+", '', text)
    # Remover URLs
    text = re.sub(r"https?://[A-Za-z0-9./]+", '', text)
    # Manter apenas letras, pontos de exclamação, interrogação e ponto final
    text = re.sub(r"[^A-Za-z.!?']", ' ', text)
    # Remover espaços extras
    text = re.sub(r" +", ' ', text)
    return text

data_clean = [clean_text(tweet) for tweet in combined_data.text]

data_clean[0:3]

data_labels = combined_data.value.values
data_labels

FullTokenizer = bert.bert_tokenization.FullTokenizer
bert_layer = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/1",
                            trainable=False)
vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
do_lower_case = bert_layer.resolved_object.do_lower_case.numpy()
tokenizer = FullTokenizer(vocab_file, do_lower_case)

def encode_sentence(sent):
  return ["[CLS]"] + tokenizer.tokenize(sent) + ["[SEP]"]

encode_sentence("I love before")

data_inputs = [encode_sentence(sentence) for sentence in data_clean]

print(data_inputs[0:2])

"""## Criação da Base de Dados"""

def get_ids(tokens):
  return tokenizer.convert_tokens_to_ids(tokens)

np.char.not_equal("[PAD]", "[PAD]")

def get_mask(tokens):
  return np.char.not_equal(tokens, "[PAD]").astype(int)

get_mask(tokenizer.tokenize("My dog likes strawberries."))

def get_segments(tokens):
  seg_ids = []
  current_seg_id = 0
  for tok in tokens:
    seg_ids.append(current_seg_id)
    if tok == "[SEP]":
      current_seg_id = 1 - current_seg_id
  return seg_ids

data_with_len = [[sent, data_labels[i], len(sent)]
                 for i, sent in enumerate(data_inputs)]
random.shuffle(data_with_len)
data_with_len.sort(key = lambda x: x[2])
sorted_all = [([get_ids(sent_lab[0]),
               get_mask(sent_lab[0]),
               get_segments(sent_lab[0])],
              sent_lab[1])
              for sent_lab in data_with_len if sent_lab[2] > 7]

sorted_all[0]

all_dataset = tf.data.Dataset.from_generator(lambda: sorted_all,
                                             output_types=(tf.int32, tf.int32))

BATCH_SIZE = 32
all_batched = all_dataset.padded_batch(BATCH_SIZE,
                                       padded_shapes=((3, None), ()),
                                       padding_values=(0, 0))

NB_BATCHES = len(sorted_all) // BATCH_SIZE
NB_BATCHES_TEST = NB_BATCHES // 6
all_batched.shuffle(NB_BATCHES)
test_dataset = all_batched.take(NB_BATCHES_TEST)
train_dataset = all_batched.skip(NB_BATCHES_TEST)

len(sorted_all)

NB_BATCHES_TEST

"""# **Part 5 - Construção do Modelo**

"""

class DCNNBERTEmbedding(tf.keras.Model):

    def __init__(self,
                 nb_filters=50,
                 FFN_units=512,
                 nb_classes=2,
                 dropout_rate=0.1,
                 name="dcnn"):
        super(DCNNBERTEmbedding, self).__init__(name=name)

        self.bert_layer = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/1",
                                         trainable = False)

        self.bigram = layers.Conv1D(filters=nb_filters,
                                    kernel_size=2,
                                    padding="valid",
                                    activation="relu")
        self.trigram = layers.Conv1D(filters=nb_filters,
                                     kernel_size=3,
                                     padding="valid",
                                     activation="relu")
        self.fourgram = layers.Conv1D(filters=nb_filters,
                                      kernel_size=4,
                                      padding="valid",
                                      activation="relu")
        self.pool = layers.GlobalMaxPool1D()
        self.dense_1 = layers.Dense(units=FFN_units, activation="relu")
        self.dropout = layers.Dropout(rate=dropout_rate)
        if nb_classes == 2:
            self.last_dense = layers.Dense(units=1,
                                           activation="sigmoid")
        else:
            self.last_dense = layers.Dense(units=nb_classes,
                                           activation="softmax")

    def embed_with_bert(self, all_tokens):
      _, embs = self.bert_layer([all_tokens[:, 0, :],
                                 all_tokens[:, 1, :],
                                 all_tokens[:, 2, :]])
      return embs

    def call(self, inputs, training):
        x = self.embed_with_bert(inputs)

        x_1 = self.bigram(x)
        x_1 = self.pool(x_1)
        x_2 = self.trigram(x)
        x_2 = self.pool(x_2)
        x_3 = self.fourgram(x)
        x_3 = self.pool(x_3)

        merged = tf.concat([x_1, x_2, x_3], axis=-1) # (batch_size, 3 * nb_filters)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output

"""# **Part 6 - Treinamento do Modelo**

"""

NB_FILTERS = 100
FFN_UNITS = 256
NB_CLASSES = 2
DROPOUT_RATE = 0.5
BATCH_SIZE = 32
NB_EPOCHS = 2

Dcnn = DCNNBERTEmbedding(nb_filters=NB_FILTERS,
                         FFN_units=FFN_UNITS,
                         nb_classes=NB_CLASSES,
                         dropout_rate=DROPOUT_RATE)

if NB_CLASSES == 2:
    Dcnn.compile(loss="binary_crossentropy",
                 optimizer="adam",
                 metrics=["accuracy"])
else:
    Dcnn.compile(loss="sparse_categorical_crossentropy",
                 optimizer="adam",
                 metrics=["sparse_categorical_accuracy"])

checkpoint_path = "/content/drive/MyDrive/opengpttext-clean"

ckpt = tf.train.Checkpoint(Dcnn=Dcnn)

ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=1)

if ckpt_manager.latest_checkpoint:
    ckpt.restore(ckpt_manager.latest_checkpoint)
    print("Latest checkpoint restored!!")

class MyCustomCallBack(tf.keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs=None):
        ckpt_manager.save()
        print("Checkpoint saved at {}.".format(checkpoint_path))

history = Dcnn.fit(train_dataset,
                   epochs=NB_EPOCHS,
                   steps_per_epoch = 50,
                   callbacks=[MyCustomCallBack()])

"""# Part 7 - Avaliação do Modelo"""

def get_prediction(sentence):
  tokens = encode_sentence(sentence)

  input_ids = get_ids(tokens)
  input_mask = get_mask(tokens)
  segment_ids = get_segments(tokens)

  inputs = tf.stack(
      [
       tf.cast(input_ids, dtype=tf.int32),
       tf.cast(input_mask, dtype=tf.int32),
       tf.cast(segment_ids, dtype=tf.int32),
      ], axis = 0)
  inputs = tf.expand_dims(inputs, 0)

  output = Dcnn(inputs, training=False)

  sentiment = math.floor(output*2)

  if sentiment == 0:
    print("Output of the model: {}\nPredicted text GPT: negative".format(output))
  elif sentiment == 1:
    print("Output of the model: {}\nPredicted text GPT: positive".format(output))

get_prediction("A Sturdy Woman. As a month slips away With no one bothering to inquire about her deeds Fulfilling what he left undone With emotions in scarce supply Calling out for heavenly assistance To avoid going insane and becoming a defendant Mapping out plans on a sheet of paper Constructing yet another tower of Babel in the process I won't deceive And certainly won't omit That she genuinely contemplates giving up So why persist with obligations? Numerous faces look alike With fragile egos Their spirits departed And paths diverged Bearing the weight of the world on her shoulders I'd wager a million on her behalf For her battle, no arguments can Claim credit for being our inspiration Due to her age Vanity is no longer as pronounced Acting authentically And captivating a few thousand")

get_prediction("A big woman. So a month goes by With no one wanting to know what she did Completing what he didn't remake With your feelings in short supply Crying out for help from heaven So as not to go crazy and become a defendant Put your plans on a sheet of paper Thus building yet another tower of Babel I must not lie And much less omit That she really wants to give up So why insist on obligations? So many similar faces With your glass egos Having your spirit gone And their divided paths Carrying a world on your back For her I would make a million bets For her fight, there are no arguments that can Take the credit for being our inspiration Due to his age There is no longer so much vanity Acting naturally And enchanting a few thousand")