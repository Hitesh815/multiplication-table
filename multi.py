print("welcome to math tester")
x=int(input("what number's table do you think you know very well?:"))
z=int(input("till where you want to check:"))
for i in range(1,z+1,1):
  print("what is the multiple of ",str(x),"*",str(i))
  y=int(input())
  if y==x*i:
    print("yup")
    if i==z:
      break
    else:
      print("go ahead")
  else:
    print("naah bro")
    break