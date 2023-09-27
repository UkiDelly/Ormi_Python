class Person:
    def __init__(self) -> None:
        pass


l = [Person(), Person(), Person()]
newl = l.copy()
print(id(l), id(newl))


print(id(l[0]), id(newl[0]))
