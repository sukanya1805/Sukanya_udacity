import csv

def city_input():
   """This function first introduces to explore US bike share data
      and ask's for the city to be entered """
   
print("Hii all! I'm Sukanya ,Lets explore US BikeShare Data!")
strcity=input("Would you like to see data for Chicago, New York or Washington?\n")

strcity=strcity.capitalize()

if strcity == 'Chicago':
   print("Oh it's " +strcity+" Let's go further")
   with open('chicago.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

    csvFile.close()
    
elif strcity =='Washington':
     print("Oh it's " +strcity+" Let's go further")
     with open('chicago.csv', 'r') as csvFile:
      reader = csv.reader(csvFile)
      for row in reader:
         print(row)
         
      csvFile.close()

elif strcity == 'New York':
     print("Oh it's " +strcity+" Let's go further")
     with open('chicago.csv', 'r') as csvFile:
      reader = csv.reader(csvFile)
      for row in reader:
         print(row)
         
      csvFile.close()

       
else:
    print("Inavlid City")
