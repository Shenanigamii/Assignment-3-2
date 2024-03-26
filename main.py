#input from user:
testScoreString = input("Enter the students test score: ")
classRankString = input("Enter the students rank in the class: ")
#converting the strings into an integer
testScore = int(testScoreString)
classRank = int(classRankString)

#decision structure
#if testScore >= 90 then ("then" is not used in python, keeps asking for ":"")
if testScore >= 90:
  if classRank >= 25:
     #output "Accept" ("output" is not used in python, and instead uses "print")
      print("Accept")
  #endif (not used in python, because it uses "elif" and "else")
  else:
      print("Reject")
elif testScore >= 80:
  if classRank >= 50:
      print("Accept")
  else:
      print("Reject")
elif testScore >= 70:
  if classRank >= 75:
      print("Accept")
  else:
      print("Reject")
else:
  print("Reject")
  #I seriously hope thats not a legitimate accept or reject formula...because even if I am number 1 in the class, and I score an 99, I am still rejected.


#original code and its problems in python
#start (not needed, so removed)
   #input testScore, classRank
   #if testScore >= 90 then ("then" is not used in python, keeps asking for ":"")
      #if classRank >= 25 then ("then" is not used in python, keeps asking for ":"")
         #output "Accept" ("output" is not used in python, and instead uses "print")
      #else
         #output "Reject" ("output" is not used in python, and instead uses "print")
      #endif (not used in python, because it uses "elif" and "else")
   #else
      #if testScore >= 80 then ("then is not used in python, keeps asking for ":"")
         #if classRank >= 50 then ("then is not used in python, keeps asking for ":"")
            #output "Accept" ("output is not used in python, and instead uses "print")
        #else
            #output "Reject" ("output is not used in python, and instead uses "print")
         #endif (not used in python, because it uses "elif" and "else")
      #else
         #if testScore >= 70 then ("then is not used in python, keeps asking for ":"")
            #if classRank >= 75 then ("then is not used in python, keeps asking for ":"")
               #output "Accept" ("output is not used in python, and instead uses "print")
            #else
               #output "Reject" ("output is not used in python, and instead uses "print")
            #endif (not used in python, because it uses "elif" and "else")
         #else
            #output "Reject" ("output is not used in python, and instead uses "print")
         #endif (not needed, so removed)
      #endif (not needed, so removed)
   #endif (not needed, so removed)
#stop (not needed, so removed)