#data /valu stor kore rakha jay
customer={
    'name':'shahinur',
    'age':24,
    'phone':"+88011902.."
}

print("update")
print(customer["phone"])
customer['name']="ahmed"
print(customer['name'])

print("add")
print(customer.get('height','height:170 cm'))
print(customer.get('salary',190000))
