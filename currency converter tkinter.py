import tkinter as tk
def convert():
    amount_sgd = float(entry.get())
    rate_usd = 0.74
    total = amount_sgd * rate_usd
    result_label.config(text=f"{amount_sgd} SGD = {total:.2f} USD")
def convert2():
    amount_sgd = float(entry.get())
    rate_jpy = 123.41
    total = amount_sgd * rate_jpy
    result_label.config(text=f"{amount_sgd} SGD = {total:.2f} JPY")
window = tk.Tk()
window.title("Currency Converter")
window.geometry("300x200")
label = tk.Label(window, text="Amount in SGD:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="amount in USD:", command=convert)
button.pack()
button2 = tk.Button(window, text="amount in JPY:", command=convert2)
button2.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()