import tkinter as tk

# ========== منطق اصلی (همون کد ترمینالی تو) ==========
# Main logic (the same terminal code you wrote)

tarikhche = []  # history list / لیست تاریخچه
a = None        # first number / عدد اول
amalgar = None  # operator / عملگر
b = None        # second number / عدد دوم

def button_click(text):
    global a, amalgar, b
    
    # Clear / پاک کردن
    if text == 'C':
        display.delete(0, tk.END)
        a = None
        amalgar = None
        b = None
        return
    
    # Equal / مساوی - محاسبه کن
    if text == '=':
        if a is not None and amalgar is not None:
            b = float(display.get())
            
            # همون if/elif های خودت
            # The same if/elif you wrote
            if amalgar == '+':
                natije = a + b
            elif amalgar == '-':
                natije = a - b
            elif amalgar == '*':
                natije = a * b
            elif amalgar == '/':
                if b == 0:
                    display.delete(0, tk.END)
                    display.insert(0, "تقسیم بر صفر اخه؟")
                    a = None
                    amalgar = None
                    return
                else:
                    natije = a / b
            
            # نمایش نتیجه / show result
            display.delete(0, tk.END)
            display.insert(0, str(natije))
            
            # ذخیره در تاریخچه / save to history
            tarikhche.append(f'{a} {amalgar} {b} = {natije}')
            
            # نتیجه میشه عدد اول بعدی / result becomes next first number
            a = natije
            amalgar = None
            
            return
    
    # History / تاریخچه
    if text == 'H':
        history_window = tk.Toplevel(root)
        history_window.title("تاریخچه")
        history_text = tk.Text(history_window, font=("Arial", 14))
        history_text.pack()
        for item in tarikhche:
            history_text.insert(tk.END, item + '\n')
        return
    
    # Operators / عملگرها
    if text in ['+', '-', '*', '/']:
        if a is None:
            # اولین عدد هنوز وارد نشده / first number not entered yet
            a = float(display.get())
        amalgar = text
        display.delete(0, tk.END)
        return
    
    # Numbers / اعداد
    display.insert(tk.END, text)


# ========== ظاهر گرافیکی ==========
# Graphical interface

root = tk.Tk()
root.title("ماشین حساب")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'H'
]

row = 1
col = 0
for button in buttons:
    tk.Button(
        root,
        text=button,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda b=button: button_click(b)
    ).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
