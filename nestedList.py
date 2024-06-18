#Given the names and grades for each student in a class of N students, store them in a #nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
   n = int(input())
   report = []
   for i in range(n):
       name = input()
       score = float(input())
       report.append([name,score])
   scoresList =  [score for name,score in report]
   reportToSet = sorted(set(scoresList))
   secondMin = reportToSet[1]
   
   ans =[]
   for record in report:
       if record[1] == secondMin:
           ans.append(record[0])
   ans = sorted(ans)
   for s in ans:
        print(s)
           
    
