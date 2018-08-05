engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
employees = engineers | programmers
employees
type(employees)
engineers.add('Marvin')
employees
employees.update(engineers)
employees
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
engineering_management = engineers & managers
engineering_management
for group in [engineers, programmers, managers, employees]: 
    group.discard('Susan')  
    print(group)
for group in [engineers, programmers, managers, employees]: 
    print(type(group))
    group.discard('Susan')  
    print(group)
