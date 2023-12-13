import GetSense
import getDistractor
import GenerateQuestion
import getNounandAdj
def getMCQs(sent):
  sentence_for_bert = sent.replace("**"," [TGT] ")
  sentence_for_bert = " ".join(sentence_for_bert.split())
  try:
      sense,meaning,answer = GetSense.get_sense(sentence_for_bert)
      print(sense)
      print(meaning)
      print(answer)
      if sense is not None:
        distractors = getDistractor.get_distractors_wordnet(sense,answer)
      else: 
        distractors = ["Word not found in Wordnet. So unable to extract distractors."]
      sentence_for_T5 = sent.replace("**"," ")
      sentence_for_T5 = " ".join(sentence_for_T5.split()) 
      ques = GenerateQuestion.get_question(sentence_for_T5,answer)
      return [ques,answer,distractors,meaning]
  except:
      return None
    
  



def GetQuestionList(paragraph):
    Questions=[]
    sentances=getNounandAdj.preProcess(paragraph)
    print(sentances)
    for sentance in sentances:
        if(len(Questions)>=10):
           return Questions
        result=getMCQs(sentance)
        if result is not None:

            # Question=result[0]
            # answer=result[1]
            options=result[2]
            if(len(options)>=3):
               Questions.append(result)
               print('**************************************************************')
            # meaning=result[3]
            # print("Question: ",Question)
            # print("Answer: ",answer)
            # print("options: ",options)
            # print("Meainng: ",meaning)
            
    return Questions

            