# helper_functions.py

import os
import pandas as pd
import re
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers
import bert

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

    data_frames_list = []

    for file_name in os.listdir(directory):
        if file_name.endswith('.jsonl'):
            file_path = os.path.join(directory, file_name)

            temp_df = pd.read_json(file_path, lines=True, encoding='latin1')
            temp_df[new_column_name] = value

            data_frames_list.append(temp_df)

    result_df = pd.concat(data_frames_list, ignore_index=True)

    return result_df

def clean_text(text):
    """
    Clean the input text by removing mentions, URLs, and extra spaces.

    Parameters:
    - text: The input text to be cleaned.

    Returns:
    The cleaned text.
    """
    text = re.sub(r"@[A-Za-z0-9_]+", '', text)
    text = re.sub(r"https?://[A-Za-z0-9./]+", '', text)
    text = re.sub(r"[^A-Za-z.!?']", ' ', text)
    text = re.sub(r" +", ' ', text)
    return text

class DCNNBERTEmbedding(tf.keras.Model):
    def __init__(self,
                 nb_filters=50,
                 FFN_units=512,
                 nb_classes=2,
                 dropout_rate=0.1,
                 name="dcnn"):
        super(DCNNBERTEmbedding, self).__init__(name=name)

        self.bert_layer = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/1",
                                         trainable=False)

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

        merged = tf.concat([x_1, x_2, x_3], axis=-1)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output
