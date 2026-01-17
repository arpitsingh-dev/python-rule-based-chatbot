# MINI CHATBOT
import datetime
import time

name=input("enter your name")
presenthour=datetime.datetime.now().hour
if 5<=presenthour <=11:
   print("good morning,",name)
elif 12<= presenthour <17: 
   print("good afternoon",name)
elif 17<= presenthour <20:
   print("good evening",name)
else :
   print("good night",name)      
print("NAMASTE! WELCOME TO YOUR CHATBOT")
print("you can ask me basic question,type 'bye' toexit from the bot")

#chatbot memory creation(using dictionary)
responses={
    "hello":"Hi,welocome. how can i help you",
    "how are you":"i am fine.Thank you",
    "who are you":"i am smart ai chatbot",
    "motivate me": "Keep going until you achieve your goal 💪"
}
#function to get response of chatbot
def get_bot_response(user_question):
   userquestion=user_question.lower().strip()
   for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
   return "i am not able tell that yet .i will learn it soon"    


#TAKE USER INPUT
while True:
   userInput=input("please ask your question")
   reply=get_bot_response(userInput)
   print("bot response:",reply)

   if "bye" in userInput.lower():
      print("See you again 😊")
      break
