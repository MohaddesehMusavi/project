import math


select = input("what do you want to do? \n  1)simple calculator \n  2)advanced calculator  \nselect :")
if select == "1" :
  number = input("choice the one operator : \n 1) + \n 2) - \n 3) * \n 4) / \n 5) ** \n 6) // \n 7) % \n 8) log2 \n 9) log10 \n 10)radical  \nselect :")
  if number == '1' :
       num1 =float(input("Enter number 1 :"))
       num2 =float(input("Enter number 2 :"))
       result = num1 + num2
       print("result = ",result)

  elif number == '2' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        result = num1 - num2
        print("result = ",result)

  elif number == '3' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        result = num1 * num2
        print("result = ",result)
  
  elif number == '4' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        
        if num2 == 0 :
            print("error!!")
        else :
            result = num1 / num2
            print("result = ",result)

  elif number == '5' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        result = num1 ** num2
        print("result = ",result)

  elif number == '6' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        if num2 == 0 :
            print("error!!")
        else :
            result = num1 //  num2
            print("result = ",result)
    
  elif number == '7' :
        num1 =float(input("Enter number 1 :"))
        num2 =float(input("Enter number 2 :"))
        result = num1 % num2
        print("result = ",result)

  elif number == '8' :
        num1 =float(input("Enter a number  :"))
        result = math.log2(num1)
        print("result = ",result)

  elif number == '9' :
        num1 =float(input("Enter a number  :"))
        result = math.log10(num1)
        print("result = ",result)
    
  elif number == '10' :
        num1 =float(input("Enter a number  :"))
        result = math.sqrt(num1)
        print("result = ",result)
  else :
        print("Please try again!!")


    
elif select == "2" :
    number = input("choice the one operator : \n 1)  sin \n 2)  cos \n 3)  ton \n 4)  kmm \n 5)  bmm \n 6)  fact \n 7)  max \n 8)  min \n 9)  radian \n 10) degree \n 11) e \n 12) pi \nselect:")
    if number == '1' :
       num1 =float(input("Enter angle :"))
       result = math.sin(num1)
       print("result = ",result)

    elif number == '2' :
       num1 =float(input("Enter angle :"))
       result = math.cos(num1)
       print("result = ",result)

    elif number == '3' :
       num1 =float(input("Enter angle :"))
       result = math.tan(num1)
       print("result = ",result)

    elif number == '4' :
       num1 =int(input("Enter number 1 :"))
       num2 =int(input("Enter number 2 :"))
       result = math.lcm(num1,num2)
       print("result = ",result)

    elif number == '5' :
       num1 =int(input("Enter number 1 :"))
       num2 =int(input("Enter number 2 :"))
       result = math.gcd(num1,num2)
       print("result = ",result)

    elif number == '6' :
       num1 =int(input("Enter a  number  :"))
       result = math.factorial(num1)
       print("result = ",result)

    elif number == '7' :
       num1 =int(input("Enter number 1 :"))
       num2 =int(input("Enter number 2 :"))
       result = max(num1,num2)
       print("result = ",result)

    elif number == '8' :
       num1 =int(input("Enter number 1 :"))
       num2 =int(input("Enter number 2 :"))
       result = min(num1,num2)
       print("result = ",result)

    elif number == '9' :
       num1 =float(input("Enter number 1 :"))
       result = math.radians(num1)
       print("result = ",result)
    
    elif number == '10' :
       num1 =float(input("Enter number 1 :"))
       result = math.degrees(num1)
       print("result = ",result)

    elif number == '11' :
       result = math.e
       print("result = ",result)

    elif number == '12' :
       result = math.pi
       print("result = ",result)

else : 
    print("Please try again :")
