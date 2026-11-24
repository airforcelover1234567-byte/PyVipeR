prv_marks={
    "maths":51,
    "biology":37,
    "physics":41,
    "sst":40,
    "chem":49,
    "mat":37
}
new_marks={
    "maths":57,
    "biology":57,
    "physics":46,
    "sst":31,
    "chem":60,
    "mat":45
}
if new_marks["biology"]>prv_marks["biology"]:
    print("You have showed improvement in biology!")
    print("Your percent of improvement is ",((new_marks["biology"]/prv_marks["biology"])*100)-100)
else:
    print("You showed no improvement")
    
if new_marks["physics"]>prv_marks["physics"]:
    print("You have showed improvement in physics!")
    print("Your percent of improvement is ",((new_marks["physics"]/prv_marks["physics"])*100)-100)
else:
    print("You showed no improvement")

if new_marks["sst"]>prv_marks["sst"]:
    print("You have showed improvement in sst!")
    print("Your percent of improvement is ",((new_marks["sst"]/prv_marks["sst"])*100)-100)
else:
    print("You showed no improvement")

if new_marks["chem"]>prv_marks["chem"]:
    print("You have showed improvement in chem!")
    print("Your percent of improvement is ",((new_marks["chem"]/prv_marks["chem"])*100)-100)
else:
    print("You showed no improvement")

if new_marks["mat"]>prv_marks["mat"]:
    print("You have showed improvement in mat!")
    print("Your percent of improvement is ",((new_marks["mat"]/prv_marks["mat"])*100)-100)
else:
    print("You showed no improvement")

