from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import pandas as pd

cx_bot = ChatBot(name='PyBot', 
                read_only=True,
                logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.BestMatch'])

#comments = pd.read_csv('')

small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']

my_comments = ['August is cool', 'Great customer service']

#other_comments = ['']

list_trainer = ListTrainer(cx_bot)

for item in (my_comments, small_talk):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(cx_bot)
corpus_trainer.train('chatterbot.corpus.english')

while true:
    try:
        bot_input = input("You: ")
        bot_response = cx_bot.get_response(bot input)
        print(f"{cx_bot.name}: {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break;
