#This is a test of Python with robot pricing
class Item(object):
	price=0
	count=0
	vat=0

robot = Item()
robot.price=900
robot.count=2
robot.vat=1.25

book = Item()
book.price=100
book.count=1
book.vat=1.06

print robot.price*robot.count*robot.vat+book.price*book.count*book.vat