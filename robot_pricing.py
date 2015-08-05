#This is a test of Python with robot pricing
robot = {
	"price":900,
	"count":2,
	"vat":1.25
}
book={
	"price":100,
	"count":1,
	"vat":1.06
}
print robot["price"]*robot["count"]*robot["vat"]+book["price"]*book["count"]*book["vat"]