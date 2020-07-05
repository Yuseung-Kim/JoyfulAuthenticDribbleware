#animal package
# dog, cat modules
# dog, cat modules can say "hi"
from animal import dog
# animal 패키지에서 dog이라는 모듈을 갖고와줘

from animal import cat

from animal import *
# animal 패키지가 갖고있는 모듈 다 불러와

d = Dog()
d.hi()

c = Cat()
c.hi()
