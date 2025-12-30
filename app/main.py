class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    people_objects = []
    for person in people:
        p = Person(person["name"], person["age"])
        if person.get("wife") is not None:
            p.wife = person["wife"]
        if person.get("husband") is not None:
            p.husband = person["husband"]

        people_objects.append(p)

    for person in people_objects:
        if "wife" in person.__dict__.keys():
            person.wife = Person.people[person.wife]
        if "husband" in person.__dict__.keys():
            person.husband = Person.people[person.husband]

    return people_objects
