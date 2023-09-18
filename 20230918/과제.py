"""
문제 1:
동물 클래스 Animal을 만들고 어주세요. Dog와 Cat 클래스를 각각 정의하십시오. 

Animal 클래스는 name 속성을 가집니다. 이 클래스는 make_sound 메서드를 갖고 있습니다.

Dog와 Cat 클래스는 Animal 클래스를 상속받는 클래스입니다.Dog 클래스의 make_sound 메서드는 "멍멍!"을,
Cat 클래스의 make_sound 메서드는 "야옹!"을 출력하도록 재정의하세요.

더 완성도 높은 클래스를 만들어보세요. 추가 속성이나 메서드 작성 가능합니다.

문제 2:
Person이라는 기본 클래스를 만들어주세요. Person 클래스는 이름과 나이라는 두 개의 속성과 소개하기라는 메서드를 가지며,
이 메서드는 "Hello World!, 제 이름은 [이름]이고 제 나이는 [나이]살 입니다."라는 메시지를 출력합니다.

Person 클래스를 상속받는 Student 클래스를 정의하십시오. Student 클래스는 추가적으로 학년 속성을 가집니다.
Student 클래스에서 소개하기 메서드를 오버라이드하여 "Hello World!, 제 이름은 [이름]이고 제 나이는 [나이]살 입니다.
그리고 저는 [학년]학년입니다. "라는 메시지를 출력하도록 만드세요.
"""


from dataclasses import dataclass


# 문제 1
@dataclass
class Animal:
    name: str
    age: int

    def make_sound(self):
        pass

    def run(self):
        print(f"{self.name}(이)가 뛰고 있습니다.")


@dataclass
class Cat(Animal):
    def make_sound(self):
        print("냐옹!")


@dataclass
class Dog(Animal):
    def make_sound(self):
        print("멍멍!")


# 문제 2번
@dataclass
class Person:
    name: str
    age: str

    def introduce(self):
        return f"Hello World!, 제 이름은 {self.name}이고 제 나이는 {self.age}살 입니다."


@dataclass
class Student(Person):
    grade: int

    def introduce(self):
        return super().introduce() + f" 그리고 저는 {self.grade}학년입니다."


# 실행
if __name__ == "__main__":
    # 문제 1

    cat = Cat("삐삐", 2)
    dog = Dog("똘이", 4)

    cat.make_sound()
    dog.make_sound()

    cat.run()
    dog.run()

    # 문제 2
    person = Person("최홍식", 30)
    student = Student("송대현", 24, 2)

    print(person.introduce())
    print(student.introduce())
