#This is a test of Python with robot pricing
class Item(object):
	price=0
	count=0
	vat=0

	def __init__(self,price,count,vat):
		self.price=price
		self.count=count
		self.vat=vat

	def total_price(self):
		full_price= self.price*self.count*self.vat
		if self.price > 500:
			return 0.9*full_price
		else:
			return full_price
		
items=[Item(900,2,1.25), Item(100,1,1.06)]
total=0

for item in items:
	total+=item.total_price()


# total=items[0].total_price()+items[1].total_price()
print "Your total with discount is", total, "SEK"
#robot = Item(900,2,1.25)
# robot.price=900
# robot.count=2
# robot.vat=1.25

#book = Item(100,1,1.06)
# book.price=100
# book.count=1
# book.vat=1.06

#print robot.total_price()+book.total_price()

#print robot.price*robot.count*robot.vat+book.price*book.count*book.vat