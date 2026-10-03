print("currency converter")
print("1. SGD to USD")
print("2. SGD to MYR")
print("3. SGD to IDR")
print("4. SGD to BND")
print("5. Quit")

choice = input("pick a number (1/2/3/4/5):")
amount_sgd = float(input("How much in SGD? "))
rate_usd = 0.74
rate_myr = 3.15
rate_idr = 10500
rate_bnd = 1.00

if choice == "1":
    total = amount_sgd * rate_usd
    print(f"{amount_sgd} SGD is {total} USD")
elif choice == "2":
    total = amount_sgd * rate_myr
    print(f"{amount_sgd} SGD is {total} MYR")
elif choice == "3":
    total = amount_sgd * rate_idr
    print(f"{amount_sgd} SGD is {total} IDR")
elif choice == "4":
    total = amount_sgd * rate_bnd
    print(f"{amount_sgd} SGD is {total} BND")
else:
    print("Quit. THank you!")