# CCC 2011 S2 - Multiple choice 

N_lines = int(input())
answers = []

for i in range (2*N_lines):
  char = input()
  answers.append(char)

def final_mark(answers):
  corr_ans = 0
  for i in range(N_lines):
    if answers[i] == answers[i + N_lines]:
      corr_ans = corr_ans + 1

  return corr_ans 

print("The number of questions answered correctly: ")
print(final_mark(answers))