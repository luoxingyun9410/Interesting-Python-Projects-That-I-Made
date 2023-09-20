customer_spending = {
	"White": 2000,
    "Black": 3000,
    "Yellow": 12000,
    "Green": 15000,
    "Grey": 8000
}

for i in customer_spending:
    if customer_spending[i] > 10000:
        customer_spending[i] = "vip"
    else:
        customer_spending[i] = "normal customer"

print(customer_spending)
