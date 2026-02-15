class Demo:

    id = 10
    _name = "sagar"
    __email = "sagar@gmail.com"
    def disp(self):
        print(self.id,self._name,self.__email)

class Sample(Demo):

    def test(self):
        print(self.id,self._name,self._Demo__email)


# d = Demo()
# # print(dir(d))
# d.id = 50
# d._name = "keyu"
# d._Demo__email = "keyu@gmail.com"
# d.disp()

# s = Sample()
# s.test()