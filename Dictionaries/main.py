customer={
    "name":"Rounak Roy",
    "age":14,
    "budget":140,
    "is_verified":True
}
customer["birth"]=2122011
customer["name"]="Sounak Roy"

print(customer["name"])
print(customer["age"])
print(customer["budget"])
print(customer["is_verified"])

print(customer.get("name"))
print(customer["birth"])