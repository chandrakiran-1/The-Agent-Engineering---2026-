class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(2,4))

class Maths:
     def add(self, a, b):
         return a+b
c = Maths()
result = c.add(2,4)
print(result)