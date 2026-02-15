class Demo:
    def test(self):
        print("Demo class test calling")

class Sample(Demo):
    def test(self):
        print("sample class test calling")
        super().test()

s  =Sample()
s.test()