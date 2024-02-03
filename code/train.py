#Dados de treinamento

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
