print ("Monthly Loan Interest Calculator")

loanamount = float(input("Loan Amount?"))

apr = float(input("APR?"))

aprpercentagefinal = apr/100

year = 12

monthlyint = aprpercentagefinal*loanamount/year


print (f"Your interest payment per month is ${monthlyint}")
