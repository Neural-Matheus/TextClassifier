"""# - Avaliação do Modelo"""

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