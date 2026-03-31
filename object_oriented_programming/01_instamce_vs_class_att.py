class Employee :
      language = "py" # This is an class attributes 
      salary = 1000000

yash = Employee ()
yash.language   = "javascript " # This is an object / INSTANCE  attributes
print( yash.language, yash.salary )


# yash.language   = "javascript " # that because instance attributes , prefer over class attrubutes during assignment & retrieval 