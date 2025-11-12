# ------------------------------------------------------------------------------
 #   import datetime; import math; import pyttsx3;
 #   import random; import requests; import time;
 #  import speech_recognition; import response_selector;
#
#
 #         self.live=False; self.name=name; self.enable_voice=enable_voice;
  #          self.enable_mic=enable_mic; self.log_filepath=log_filepath;
   #         self.database_filepath=database_filepath;
    #        self.selector=response_selector.response_selector(0,self.database_filepath);
     #       try:log_file=open(self.log_filepath,"x"); log_file.close();
      #      except:
       #        except:print(">> ERR : A problem occurred while trying to find the log file");
       #     try:db=open(self.database_filepath,"x"); db.close();
        #    except:
       #         try:db=open(self.database_filepath,"r"); db.close();
        #        except:print(">> ERR : A problem occurred while trying to find the database");
        #
        #def wake(self):self.live=True;
        #def sleep(self):self.live=False;
        
       # def speak(self,response,buffer):
        #    if (self.enable_voice==True):
         #       voice_engine=pyttsx3.init(); voice_engine.setProperty('rate',125);
          #      voice_engine.setProperty('volume',0.35); voice_engine.say(response);
           #     voice_engine.runAndWait(); time.sleep(buffer);
          #  else:print(">> "+self.name+" : "+response); time.sleep(buffer);
            
        #def append_log(self,log_user,log_bot):
        #    log_file=open(self.log_filepath,"a"); 
        #    log_file.write("\n@"+str(datetime.datetime.now())+" { USER : "+log_user+" || BOT : "+log_bot+" }");
        #    log_file.close();
         
        #def display_log(self):
        #    log_file=open(self.log_filepath,"r"); contents=log_file.read();
        #    log_file.close(); return contents;
        
        #def listen(self):
         #   sphinx_recog=speech_recognition.Recognizer();
          #  goog_recog=speech_recognition.Recognizer();
          #  if (self.enable_mic==True):
          #      timeout=2;
          #      try:
          #          requests.head("http://www.google.com/",timeout=timeout);
          #          while(1):
          #              try:
          #                  with speech_recognition.Microphone() as source:
          #                      goog_recog.adjust_for_ambient_noise(source,duration=0.2);
          #                      audio=goog_recog.listen(source); msg=goog_recog.recognize_google(audio);
          #                      return str(msg);
           #             except speech_recognition.RequestError: msg=str("____unknown____"); return msg;
           #             except speech_recognition.UnknownValueError: msg=str("____unknown____"); return msg;
            #    except requests.ConnectionError:
            #        with speech_recognition.Microphone() as source: audio=sphinx_recog.listen(source);
             #       try:msg=str(sphinx_recog.recognize_sphinx(audio)); return msg;
             #       except speech_recognition.UnknownValueError:msg=str("____unknown____"); return msg;
              #      except speech_recognition.RequestError as e:msg=str("____unknown____"); return msg;
            #else:query=input(">> User : "); time.sleep(0.1); return query;

        #def fetch_response(self,query):
         #   response=self.selector.compute(query);
          #  return response;
# ------------------------------------------

import datetime; import math; import pyttsx3;
import random; import requests; import time;
import speech_recognition; 
import response_selector;


class chatbot():
    def __init__(self,name,enable_voice,enable_mic,log_filepath,database_filepath):
        self.live=False; self.name=name; self.enable_voice=enable_voice;
        self.enable_mic=enable_mic; self.log_filepath=log_filepath;
        self.database_filepath=database_filepath;
        self.selector=response_selector.response_selector(0,self.database_filepath);
        try:log_file=open(self.log_filepath,"x"); log_file.close();
        except:
            try:log_file=open(self.log_filepath,"r"); log_file.close();
            except:print(">> ERR : A problem occurred while trying to find the log file");
        try:db=open(self.database_filepath,"x"); db.close();
        except:
            try:db=open(self.database_filepath,"r"); db.close();
            except:print(">> ERR : A problem occurred while trying to find the database");
    
    def wake(self):self.live=True;
    def sleep(self):self.live=False;
    
    def speak(self,response,buffer):
        if (self.enable_voice==True):
            voice_engine=pyttsx3.init(); voice_engine.setProperty('rate',125);
            voice_engine.setProperty('volume',0.35); voice_engine.say(response);
            voice_engine.runAndWait(); print(">> "+self.name+" : "+response);
            time.sleep(buffer);
        else:print(">> "+self.name+" : "+response); time.sleep(buffer);
        
    def append_log(self,log_user,log_bot):
        log_file=open(self.log_filepath,"a"); 
        log_file.write("\n@"+str(datetime.datetime.now())+" { USER : "+log_user+" || BOT : "+log_bot+" }");
        log_file.close();
     
    def display_log(self):
        log_file=open(self.log_filepath,"r"); contents=log_file.read();
        log_file.close(); return contents;
    
    def listen(self):
        sphinx_recog=speech_recognition.Recognizer();
        goog_recog=speech_recognition.Recognizer();
        if (self.enable_mic==True):
            timeout=2;
            try:
                requests.head("http://www.google.com/",timeout=timeout);
                while(1):
                    try:
                        with speech_recognition.Microphone() as source:
                            goog_recog.adjust_for_ambient_noise(source,duration=0.2);
                            audio=goog_recog.listen(source); msg=goog_recog.recognize_google(audio);
                            return str(msg);
                    except speech_recognition.RequestError: msg=str("____unknown____"); return msg;
                    except speech_recognition.UnknownValueError: msg=str("____unknown____"); return msg;
            except requests.ConnectionError:
                with speech_recognition.Microphone() as source: audio=sphinx_recog.listen(source);
                try:msg=str(sphinx_recog.recognize_sphinx(audio)); return msg;
                except speech_recognition.UnknownValueError:msg=str("____unknown____"); return msg;
                except speech_recognition.RequestError as e:msg=str("____unknown____"); return msg;
        else:query=input(">> User : "); time.sleep(0.1); return query;

    def fetch_response(self,query):
        response=self.selector.compute(query);
        return response;