# --------------------------------------------
#import chatbot;#
#
#bot=chatbot.chatbot("Adam",
 #                   False,
  #                  False,
   #                 "log.txt",
    #                "database.json");

#  user_msg=bot.listen();
  #  bot_response=bot.fetch_response(user_msg);
 #   bot.speak(bot_response,0.1);
  #  bot.append_log(user_msg,bot_response);
# ------------------------------------------

import chatbot;

bot=chatbot.chatbot("Tom",False,False,"chat_log.txt","database.json");

while True:
    user_msg=bot.listen();
    bot_response=bot.fetch_response(user_msg);
    bot.speak(bot_response,0.1);
    bot.append_log(user_msg,bot_response);