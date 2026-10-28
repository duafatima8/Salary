class Employee:
  def __init__(self, name, salary , emploId):
    self.__name = name
    self.__salary = salary
    self.__emploId = emploId

  
  def increase_salary(self,double_per):
    if double_per > 0:
      up_salary = self.__salary *(1+ double_per/100)
      print(f"""      Your old salary : {self.__salary}
      Your updated salary : {up_salary}""")
    else:
      print("invalid value")
  
salary_info = Employee("jhope", 30000, 8941)
salary_info.increase_salary(50)  
