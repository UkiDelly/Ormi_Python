# class Animal:
#     name: str

#     def __init__(self, name: str):
#         self.name = name

#     def say(self):
#         print("짖다")


# class Cat(Animal):
#     def __init__(self, name: str):
#         super().__init__(name)

#     def say(self):
#         print("야옹")


# cat = Cat("삐삐")

# print(issubclass(Cat, Animal))

num_list4: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_list = list(range(101))
result1 = sum(num_list[::2])
retult2 = sum(num_list[::3]) + sum(num_list[::5]) - sum(num_list[15::15])

num_list2 = list(range(1, 92))
result5 = sum(num_list2[1:92:2])

print(result1)
print(retult2)
print(result5)
