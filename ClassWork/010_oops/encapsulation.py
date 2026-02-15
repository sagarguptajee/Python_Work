class Sample:
    __a = 10

    def set(self,a):
        self.__a = a
    def get(self):
        print(self.__a)

    def __display(self):
        print("display calling")

s = Sample()
# s.set(50)
s.get()