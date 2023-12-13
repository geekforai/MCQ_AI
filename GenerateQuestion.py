from transformers import T5ForConditionalGeneration,T5Tokenizer

question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('t5-base')

def get_question(sentence,answer):
  text = "context: {} answer: {} </s>".format(sentence,answer)
  print (text)
  max_len = 512
  encoding = question_tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=True, return_tensors="pt")

  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = question_model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=5,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  max_length=200)


  dec = [question_tokenizer.decode(ids) for ids in outs]


  Question = dec[0].replace("question:","")
  Question= Question.strip()
  return Question

def extract_word_between_tags(sentence):
    start_tag = "[TGT]"
    end_tag = "[TGT]"

    start_index = sentence.find(start_tag) + len(start_tag)
    end_index = sentence.find(end_tag, start_index)

    if start_index == -1 or end_index == -1:
        return None
    
    word = sentence[start_index:end_index].strip()
    return word
# def GetQuest(sentence):
#     answer=extract_word_between_tags(sentence)
#     sentence_for_T5 = sentence.replace("[TGT]"," ")
#     sentence_for_T5 = " ".join(sentence_for_T5.split()) 
#     ques = get_question(sentence_for_T5,answer)
#     return ques


