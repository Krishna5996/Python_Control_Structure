favourite_subject = ["OS", "DBMS", "Algo"]
 
# making it frozenset type
f_subject = frozenset(favourite_subject)
print(f_subject)
 
# below line will generate error
 
#f_subject[1] = "Networking"
