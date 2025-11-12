#    import random; import os; import json;
#    import sys; import math; import time;
#    import datetime; import filter;
#    from datetime import *;
#
#
#    class response_selector():
#        def __init__(self,type,database):
#            self.type=type; self.database=database;
#            self.filter=filter.filter(True,True);
#            
#            self.fallback_unknown=["I do not understand","I'm sorry, I do not understand",
#                                   "I don't understand","I'm sorry, I don't understand"
#                                   "My apologies, my knowledge and responses provided are limited purely to my domain of expertise"];
#        
#        def execution(self,opcode):
#            if (opcode!="0"):
#                if (opcode=="1"):
#                    resp=["The current time is ","The time is ","It is currently "];
#                    return str(random.choice(resp)+str(datetime.now().strftime("%I:%M %p")));
#                elif (opcode=="2"):
#                    resp=["Today is ","It is "];
#                    return str(random.choice(resp)+str(datetime.today().strftime('%A')));
#                    
#        def select_by_matchcase(self,query):
#            response=str(""); query=self.filter.apply(query);
#            fb=["",""];
#            if (response==""):
#                with open(self.database,'r') as db:
#                    content=json.load(db);
#                    for category in content['categories']:
#                        if ('patterns' in category):
#                            if (any(query.lower() in pattern.lower() for pattern in category['patterns'])):
#                                response=random.choice(category['responses']); op_code=random.choice(category['operation']);
#                                break;
#            if (response==""):
#                response=random.choice(self.fallback_unknown);
#                op_code="0";
#            fb[0]=response; fb[1]=op_code;
#            return fb;
#        
#        def select_by_tags(self,query_tags):
#            response=str(""); fb=["",""];
# ---------------------------------------------------------------------------------
#            if (response==""):
#                with open(self.database,'r') as db:
#                    content=json.load(db);
#                    for category in content['categories']:
#                        if ('tags' in category):
#                            if (query_tags==category['tags']):
#                                response=random.choice(category['responses']);
#                                op_code=category['operation']; break;
#            if (response=="" and op_code==""):
#                response=random.choice(self.fallback_unknown);
#                op_code="0";
#            fb[0]=response; fb[1]=op_code;
#            return fb;
#        
#        def select_by_tag_similarity():
#            response=str(""); fb=["",""];
#            if (response==""):
#                with open(self.database,'r') as db:
#                    content=json.load(db);
#                    for category in content['categories']:
#                        if ('tags' in category):
#                            if (set(query_tags).intersection(category['tags'])):
#                                response=random.choice(category['responses']);
#                                op_code=category['operation']; break;
#            if (response=="" and op_code==""):
#                response=random.choice(self.fallback_unknown);
#                op_code="0";
#            fb[0]=response; fb[1]=op_code;
#            return fb;
#        
#        def compute(self,user_input):
#            if (self.type==0):
#                feedback=self.select_by_matchcase(user_input);
#                if (feedback[1]!="0"): return self.execution(feedback[1]);
#                else: return feedback[0];
# ----------------------------------------------------------------------------

import random; import os; import json; import paramiko;
import sys; import math; import time;
import datetime; import filter;
from datetime import *;


class response_selector():
    def __init__(self,type,database):
        self.type=type; self.database=database;
        self.filter=filter.filter(True,True);
        
        self.fallback_unknown=["I do not understand","I'm sorry, I do not understand",
                               "I don't understand","I'm sorry, I don't understand",
                               "My apologies, I didn't quite catch that",
                               "My apologies, I didn't quite catch that last one",
                               "My sincerest apologies, do you mind repeating yourself",
                               "My apologies, my knowledge and responses provided are limited purely to my domain of expertise"];
    
    def execution(self,opcode):
        if (opcode!="0"):
            if (opcode=="1"):
                resp=["The current time is ","The time is ","It is currently "];
                return str(random.choice(resp)+str(datetime.now().strftime("%I:%M %p")));
            elif (opcode=="99"):
                exit();
            elif (opcode=="2"):
                resp=["Today is ","It is "];
                return str(random.choice(resp)+str(datetime.today().strftime('%A')));
            elif (opcode=="3"):
                resp=["Restarting the robot now","Restarting","Okay"];
                robotIP=str("10.43.168.156");
                ssh=paramiko.SSHClient(); ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
                ssh.connect(robotIP,username='kubot',password='HairouKubot_@2018!');
                ssh_stdin,ssh_stdout,ssh_stderr=ssh.exec_command('sudo /etc/kubot_application.sh restart');
                print(ssh_stdout.read().decode()); print(ssh_stderr.read().decode());
                ssh.close();
                return str(random.choice(resp)+str(datetime.today().strftime('%A')));
                
                
    def select_by_matchcase(self,query):
        response=str(""); query=self.filter.apply(query);
        fb=["",""];
        if (response==""):
            with open(self.database,'r') as db:
                content=json.load(db);
                for category in content['categories']:
                    if ('patterns' in category):
                        if (any(query.lower() in pattern.lower() for pattern in category['patterns'])):
                            response=random.choice(category['responses']); op_code=random.choice(category['operation']);
                            break;
        if (response==""):
            response=random.choice(self.fallback_unknown);
            op_code="0";
        fb[0]=response; fb[1]=op_code;
        return fb;
    
    def select_by_tags(self,query_tags):
        response=str(""); fb=["",""];
        if (response==""):
            with open(self.database,'r') as db:
                content=json.load(db);
                for category in content['categories']:
                    if ('tags' in category):
                        if (query_tags==category['tags']):
                            response=random.choice(category['responses']);
                            op_code=category['operation']; break;
        if (response=="" and op_code==""):
            response=random.choice(self.fallback_unknown);
            op_code="0";
        fb[0]=response; fb[1]=op_code;
        return fb;
    
    def select_by_tag_similarity():
        response=str(""); fb=["",""];
        if (response==""):
            with open(self.database,'r') as db:
                content=json.load(db);
                for category in content['categories']:
                    if ('tags' in category):
                        if (set(query_tags).intersection(category['tags'])):
                            response=random.choice(category['responses']);
                            op_code=category['operation']; break;
        if (response=="" and op_code==""):
            response=random.choice(self.fallback_unknown);
            op_code="0";
        fb[0]=response; fb[1]=op_code;
        return fb;
    
    def compute(self,user_input):
        if (self.type==0):
            feedback=self.select_by_matchcase(user_input);
            if (feedback[1]!="0"): return self.execution(feedback[1]);
            else: return feedback[0];