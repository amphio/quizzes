from __future__ import print_function
import os
import sys
import time
import json
import subprocess
import sys
import time
import datetime
from collections import OrderedDict, namedtuple, Counter
from pprint import pprint
from os.path import basename

def load_libray():
	try:
		print ("\nTo get started, please enter the file path of the quiz you'd like to take (e.g. /Users/Rainbow/Documents/GitHub/quizzes)...")
		quizzes_filepath = raw_input("(filepath) > ")
		quizzes_filepath = quizzes_filepath.replace(" ", "")
		#Load file
		with open(quizzes_filepath) as quiz_file:    
			uncompleted_quizzes = json.load(quiz_file, object_pairs_hook=OrderedDict)
		return quizzes_filepath, uncompleted_quizzes
	except Exception as e:
		raise e
		print ("The file %s was not found in the current directory. \nPlease try again..." % (quizzes_filepath))
		load_libray()
	


def run_quiz(items):
	"""
	Expects a quiz dict
	Returns that quiz with answers from user
	"""
	user_responses = OrderedDict()

	total_items = 0
	for item in items:
		total_items = total_items + 1
	
	#Ask questions
	current_item_number = 1
	for item in items:
		print ("%i of %i: " % (current_item_number, total_items) + item)
		answer = raw_input("> ")
		user_responses[item] = answer
		current_item_number = current_item_number + 1
	#Todo: Plain text Antyhing elsE?
	print ("\nquiz complete.")
	return user_responses


def run_through_quizzes(uncompleted_quizzes, expected_responses = OrderedDict(), actual_responses = OrderedDict()):
	"""
	Expects a quiz list
	Returns that quiz with answers from user
	"""
	current_quiz = uncompleted_quizzes.keys()[0]
	
	if current_quiz == "Context":
		response = "y"
	else:
		print ("\nWould you like to be quizzed on " + current_quiz + "?")
		response = raw_input("(y/n) > ")

	if response == "y":
		expected_responses[current_quiz] = uncompleted_quizzes[current_quiz]
		actual_responses[current_quiz] = run_quiz(uncompleted_quizzes[current_quiz])
	else:
		pass

	#Remove this quiz
	del uncompleted_quizzes[current_quiz]

	#Check if quizzes exist
	if not uncompleted_quizzes:
		#No more quizzes found
		pass
	else:
		run_through_quizzes(uncompleted_quizzes)
	
	completed_quizzes = {"expected_responses": expected_responses, "actual_responses": actual_responses}
	return (completed_quizzes)


def check_answers(completed_quizzes):
	test = completed_quizzes["actual_responses"]
	correct_answers = completed_quizzes["expected_responses"]


	test_results = {"Test passed":True, "Unexpected_behaviours": {}}
	section_failed = True
	for section in test:
		if section != "Context":
			for question in test[section]:
				if test[section][question] == correct_answers[section][question]:
					pass
				else:
					test_failed = False
					test_results["Unexpected_behaviours"][question] = test[section][question]
					test_results["Test passed"] = False
	return test_results


def dump_to_file(final_results):
	"""
	Writes results to json
	"""
	#Add prefix result
#	if final_results["Results"]["Test passed"] == True:
#		time_now = time.time()
#		ouput_filepath = quizzes_filepath.replace("example_quiz.json", "", 1) + "results/" + datetime.datetime.fromtimestamp(time_now).strftime('%Y-%m-%d_%Hh%Mm%Ss') + "_PASSED.json"
#	else:
#		time_now = time.time()
#		ouput_filepath = quizzes_filepath.replace("example_quiz.json", "", 1) + "results/" + datetime.datetime.fromtimestamp(time_now).strftime('%Y-%m-%d_%Hh%Mm%Ss') + "_FAILED.json"

#Get current directory
	if final_results["Results"]["Test passed"] == True:
		time_now = time.time()
		filename = basename(quizzes_filepath)
		ouput_filepath = os.path.dirname(os.path.abspath(__file__)) + "/results/" + filename + datetime.datetime.fromtimestamp(time_now).strftime('%Y-%m-%d_%Hh%Mm%Ss') + "_PASSED.json"
#	else:
#		time_now = time.time()
	else:
		time_now = time.time()
		filename = basename(quizzes_filepath)
		ouput_filepath = os.path.dirname(os.path.abspath(__file__)) + "/results/" + filename + datetime.datetime.fromtimestamp(time_now).strftime('%Y-%m-%d_%Hh%Mm%Ss') + "_FAILED.json"
	with open(ouput_filepath,  'w') as fp:
		json.dump(final_results, fp)
	return ouput_filepath

#----------------------------------------------------
#PRINT ASCII ART
print ("""\n\n\n
                
                                                                 ,-=::::::-,                                              
                                                                ,:;///,   ,-:;;=                                          
                                                                      :/--=.   ,+:                                        
                                                                    .:;;:-.      :;                                       
                                                                  -/:.      .-:;;;X;=-/;::;;-                             
                                                                .+=      :;;=,.     .:;+,  -;%=                           
                                                               -+    :+$/.              ;/ ,,=:;/,                        
                                                              -/  -%+=$-                 .+=     ;;                       
                                                              % =/H= X.  -:/;/;;;;=,         =;;;;%$.                     
                                                             /:+-/= %=;+;-.       ,://:             :/-                   
                                                             H: ,+ -M/.               -+/             :/                  
                                                                $. H:                   =%   .-==-.    =;                 
                                                               ,+                        :%/;:=,-H:;;.  %.                
                                                               +,                                /-  ;; ::                
                                                               $                                 .%   ./;/                
                                                              -/                                  $     :=                
                                                              +,                                  /-                      
                                                              X                                   ;:                      
                 -/;;                                         $                                   -/                      
                :/  ;=                                       -/        .;/;;++::,                 ,/                      
               .$   =/:;;:                                   ;+=,     :/, ;;:,.,=;/,              ,/                      
               =;   ;%.  -+                                  +=-:///=+: ,%,   .    /:             ,+                      
               ;-   $,    X/:                                $      :X- $     ;=    /=             %                      
               +,  ,X:;   X =+                               X      /= -;    -.%    .X;//,,//;;+X$+$                      
              =+   --+;  ;;  $                            ,=,%      ;: -/    $ /,   .%   X/ -/;-,,=//.                    
             .%      =%-/+  :;                           +;-=+,     .$. %    =..;   /-  =/ /:        /=                   
             /-       ,:$-,/;                           +-:+/-       .+;=%,        /:   :=::     ,;   +,                  
             %,          ::;+-.                         $   -$         .=;//:-,,=//,    :=%.  :=  %   =;                  
             %,      -=      -:;;/.                     $   -               .-:=,       ::/,  -:  %   :=                  
          ,=-%,      /:          .$                     ,%:==                           =$,%      ;  ,%                   
         =H:,;;     -$          ,;;                       $-,                           .@/%H:     .:/                    
        .% =/+$    ./     =/;/;;=                        -+                              %- /+;;::;:.                     
        +,    =///=,     ;/                              $.                              .X.$                             
       ,/         ,://;//@@.                            ;:                                =@.                             
       %.                 %.                           -%                                  +-                             
      =;                 -/                           .$                                   .%                             
      %                 .%                            %.                                   .%                             
     =;                 +.                          -%%/                       +:          ;:                             
     $                 ::                          +:                           :%:      .;;                              
    :=                .%                          =;  +%##@$/,                    -///%/$/.                               
   .%                 /,                       ,;;X=  $ +#####M%:.                      ,+                                
   +,                ,+                     .;;: =X;  .;%M########$:                     %,                               
  ,+                 %.                   ,/;   ;/.+      -/X####; =@/=                  -/                               
  +.                -/                ,;+X;    =+             :$@. $: ,;;;.               $               .               
  $                 X%:;;;;;;::;;;;:%+://     -$                   ,+    .://,            X            =+;=/;--           
  %                -+X             =-,%,    :/=;/:                .;;       $:/;,         $           /::   X=-%,  -/;:   
 ./                .,$              ;/     -/    -+=           ,//;.        =/..://;-    /=          :; @   $- -/ :/  +-  
 .+                 .-             +=      %.      =+         +:             .:::;/.-;+X;,       :///H  :+=+/  :$/;   /-  
  $                              ,%.       %        =/       %,                   .;:;:         =/   ,$,  ,X  ,X     ,%   
  -+                            -+         $         X      +,                                  ,%.   .$   +/++.    ;/    
   ./;.                        :+        -+.         %/;/. /$;::::/.                             ./=   +          :+.     
     .;/;-                    ;:        :;           %  .X/-      /-                             . /:     :      :;       
         -:;;:-              +=        ,%           +,   %       ,+                           -/;X/%+     :/     X        
              -;;;:-         +,        -/         ,+-   ;-      :/                          .+:  .%%:     :;     $        
                   -:;;;%;;;::$         ++;::::;;;=;;-,/=     :/;;;-                       :/.     //    .%     ;;        
                      .+-    ,/=       =/            ,$      %,    =;/=                  -/,        .//.      ,/;         
                     ,+.       %,     .%             ,X-     $        .:;;,            .+:            ./+= .+%=           
                    -+          $,    %.        .::  %.%     $            =/;=        ;;                 -/X/:/           
                   ,+         .,:H.  =:         /=::/, /%:-:/$               ,;;;;-,=/.                     ,;X=          
                   %     .:;;;;=.    $           --.+ -/ ... X                 ,+;;X=                        -+                                      
""")

#----------------------------------------------------
#PROCESS


#Welcome and list quizzes
print ("WELCOME TO quizzes...")

#Load library
quizzes_filepath, uncompleted_quizzes = load_libray()

#Show quizzes in selected library
print ('\nThe following quizzes are available in %s: ' % quizzes_filepath)
for keys in (uncompleted_quizzes.keys()):
	print (keys)

#Ask for begin
print ("\nShall we begin?")
response = raw_input("(y/n) > ")
if response == "y":
	pass
else:
	print ("No quizzes completed")
	sys.exit()

#Run the optional quizzes
completed_quizzes = run_through_quizzes(uncompleted_quizzes)
quiz_results = check_answers(completed_quizzes)
score = Counter(quiz_results.values())

#Print test results
print(score)
print ("quiz RESULTS:")
pprint (quiz_results)

final_results = OrderedDict()
final_results["Results"] = quiz_results
final_results["actual_responses"] = completed_quizzes["actual_responses"]

#Save test results
ouput_filepath = dump_to_file(final_results)
print ("\nTest results saved to: " + ouput_filepath)
print ("Please commit these results to GitHub...")
