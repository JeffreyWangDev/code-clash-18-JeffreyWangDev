"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""

class Solution:    
    def ClockTalker(self, input_time):
                return "It's " +{1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 0:"twelve"}[int(input_time.split(":")[0]) if int(input_time.split(":")[0]) < 12 else int(input_time.split(":")[0]) - 12]+ " " + {1:"oh one",2:"oh two",3:"oh three",4:"oh four",5:"oh five",10:"ten",11:"eleven",13:"thirteen",14:"fourteen",19:"nineteen",20:"twenty",30:"thirty",29:"twenty nine",39:"thirty nine",49:"forty nine",59:"fifty nine"}[int(input_time.split(":")[1])] +" "+ ("am" if int(input_time.split(":")[0])>12 else "pm")
def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
