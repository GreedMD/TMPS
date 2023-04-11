class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Cannot create multiple instances of Singleton")
        else:
            Singleton.__instance = self
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def some_business_logic(self):

        print("Executing some business logic...")
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

if s1 is s2:
    print("Both instances are the same")
else:
    print("Different instances were created")

s1.some_business_logic()
