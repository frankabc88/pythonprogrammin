devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]

salario=0
actual_dev={}

for dev in devs:
    if dev['salario']>salario:
        salario=dev['salario']
        actual_dev=dev
        
print(actual_dev['cc'],actual_dev['nombre']) 


i= 0
while i <len(devs): #para insertar un valor inicial 
    if i == 0:
        dev_temp = devs[0]
        
    if dev_temp['years']<devs[i]['years']:
        dev_temp =devs[i]
    i+=1    
    