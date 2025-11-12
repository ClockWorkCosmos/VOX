# -----------------------------------------------------------------
#    import re;
#
#
 #   class filter:
  #      def __init__(self,filter_profanity,filter_special_chars):
   #         self.filter_profanity=filter_profanity;
    #        self.filter_special_chars=filter_special_chars;
#
 #       def apply(self,unfiltered_query):
  #          unfiltered_query=unfiltered_query.lower();
   #         unfiltered_query=re.sub(' +', ' ', unfiltered_query);
    #        special_characters=["!","?","'",",","<",">",".",";"];
     #       profanity_words=["shit","fuck","fuckface",
      #                       "fucker","motherfucker","bitch",
       #                      "asshole","cunt","faggot",
        #                     "dickweed","chink","shit",
         #                    "gook","jap","kraut","nigga","nigger",
          #                   "pussy","cocksucker","shit-eater","dick",
           #                  "titties","cum guzzler","spick"];
            #                 
            #if (self.filter_special_chars):
            #    unfiltered_query=[char for char in unfiltered_query if char not in special_characters];
             #   unfiltered_query =''.join(unfiltered_query);
                
            #if (self.filter_profanity):
             #   unfiltered_query=unfiltered_query.split();
              #  unfiltered_query=[word for word in unfiltered_query if word not in profanity_words];
               # unfiltered_query=' '.join(unfiltered_query);

            #filtered_query=unfiltered_query; return filtered_query;
# -------------------------------------------------------------------

import re;


class filter:
    def __init__(self,filter_profanity,filter_special_chars):
        self.filter_profanity=filter_profanity;
        self.filter_special_chars=filter_special_chars;

    def apply(self,unfiltered_query):
        unfiltered_query=unfiltered_query.lower();
        unfiltered_query=re.sub(' +', ' ', unfiltered_query);
        special_characters=["!","?","'",",","<",">",".",";"];
        profanity_words=["shit","fuck","fuckface",
                         "fucker","motherfucker","bitch",
                         "asshole","cunt","faggot",
                         "dickweed","chink","shit",
                         "gook","jap","kraut","nigga","nigger",
                         "pussy","cocksucker","shit-eater","dick",
                         "titties","cum guzzler","spick"];
                         
        if (self.filter_special_chars):
            unfiltered_query=[char for char in unfiltered_query if char not in special_characters];
            unfiltered_query =''.join(unfiltered_query);
            
        if (self.filter_profanity):
            unfiltered_query=unfiltered_query.split();
            unfiltered_query=[word for word in unfiltered_query if word not in profanity_words];
            unfiltered_query=' '.join(unfiltered_query);

        filtered_query=unfiltered_query; return filtered_query;
