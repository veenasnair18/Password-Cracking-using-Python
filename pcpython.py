import hashlib
pass_hash = input("\nEnter md5 hash :")
wl=input("\n Enter File name?")
try:
  pass_file = open(wl,"r")
except:
  print("\n No file found!")
  quit()
for w in pass_file:
  e_w=w.encode('utf-8')
  d= hashlib.md5(e_w.strip()).hexdigest()
  print(w)
  print(pass_hash)
  print(d)
if d == pass_hash:
  print("\n \n \t Password is found!!")
  print("\nPassword is:",w)
  flag =1
if flag == 0:
  print("\n Password is not in the list!!")
