from flask import Flask, render_template,request
import GetMCQ
from crossword import getCross
import random
app = Flask(__name__)
@app.route('/crossword',methods=['POST'])
def crossword():
    if request.method=='POST':
        paragraph=request.form['text']
        res=getCross(paragraph)
        print(res)
        crosswords=res
    return render_template('crossword.html',crosswords=crosswords)
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/MCQ')
def NEW():
    return render_template('MCQtemp.html')

@app.route('/getMcqQuiz',methods=['POST'])
def quiz():
    if request.method=='POST':
        paragraph=request.form['text']
        QuestionsData=GetMCQ.GetQuestionList(paragraph)
        # One Question= [ques,answer,distractors,meaning]
        Questions=[]
        answers=[]
        for i in range(len(QuestionsData)):
            ques=QuestionsData[i][0].replace("<pad>", "")
            ques=ques.replace("</s>","")
            temp=[]
            temp.append(ques)
            temp.append(QuestionsData[i][1])
            answers.append(QuestionsData[i][1])
            temp1=[]
            for op in QuestionsData[i][2]:
                if(len(temp1)<3):
                    temp1.append(op)

            temp1.append(QuestionsData[i][1])
            random.shuffle(temp1)
            temp.append(temp1)
        
            Questions.append(temp)
                
            

        
        
    return render_template('quiz.html',Questions=Questions,answers=answers)
if __name__ == '__main__':
    app.run(debug=True)

