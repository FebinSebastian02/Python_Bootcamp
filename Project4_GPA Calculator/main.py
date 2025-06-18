# This is the base version of GPA Calculator

# A dictionary is created to store Subject name, score and credits
transcript_febin = {'Vehicle Vibrations' : [1, 3], 'Drives and Gears' : [1.3, 3],
              'Manufacturing Engineering and Production in the Automotive Industry' : [1.8, 6],
              'Foundations of Software Engineering' : [2.3, 4], 'Safety and Reliability of Embedded Systems' : [3.3, 4],
              'Automotive Software and Systems Engineering' : [3.7, 4], 'CVT Programming Project' : [1, 4],
              'Principles of Electrical and Computer Engineering' : [3.7, 5],'Introduction to Autonomous Systems' : [1.7, 4],
              'Vehicle Propulsion Systems' : [2.7, 3], 'Simulation of Bus Systems' : [2, 4], 'Electric and Hybrid vehicles' : [1.7, 3], 'CAE in Control Engineering' : [2.3, 4],
              'Industrial Organisation' : [2.7, 4.5], 'Linguistics and Language Processing' : [1.7, 5]}

sumOfNumerator = 0
sumOfDenominator = 0

for item in transcript_febin:
    score = transcript_febin[item][0]
    credit = transcript_febin[item][1]

    numerator = score * credit
    sumOfNumerator += numerator
    sumOfDenominator += credit

finalGPA = sumOfNumerator/ sumOfDenominator
print()
print("Your Final GPA is: ", finalGPA)
print()
