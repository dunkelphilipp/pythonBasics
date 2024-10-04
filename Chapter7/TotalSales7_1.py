def calculate():
    sales = []
    total = 0
    for i in range(7):
        daily_sale = int(input(f"Enter Sales form day {i + 1}"))
        sales.append(daily_sale)
        total += daily_sale
    print(total)

calculate()