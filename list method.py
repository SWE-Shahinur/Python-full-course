numbers=[1,4,2,9,8,4,29,]
numbers.append(13)
print(numbers)

numbers=[1,4,2,9,8,4,29,]
numbers.insert(0,19)
print(numbers)

numbers=[1,4,2,9,8,4,29,]
numbers.clear()
print(numbers)

numbers=[1,4,2,9,8,4,29,]
numbers.pop()
print(numbers)

#position dekhte caile
numbers=[1,4,2,9,8,4,29,]
print(numbers.index(9))

#koto bar ase dekhar jonno count
numbers=[1,4,2,9,8,4,29,4,3,]
print(numbers.count(4))

#boolean
numbers=[1,4,2,9,8,4,29,]
print(20 in numbers)

numbers=[1,4,2,9,8,4,29,]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

fruits=['apple','lichi']
flower=['roose','lily']
fruits.append(flower)
print(fruits)
