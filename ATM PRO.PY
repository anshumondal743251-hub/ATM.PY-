import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random


# =========================================================
# ACCOUNT CLASS
# =========================================================

class Account:

    def __init__(self, account_no, mobile, balance):
        self.account_no = account_no
        self.mobile = mobile
        self.balance = balance
        self.transactions = []

    # ---------------- CREDIT ----------------

    def credit(self, amount):

        if amount <= 0:
            return False, "Enter a valid amount."

        self.balance += amount

        self.transactions.append({
            "type": "CREDIT",
            "amount": amount,
            "balance": self.balance,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        return True, f"₹{amount:,.2f} credited successfully."

    # ---------------- DEBIT ----------------

    def debit(self, amount):

        if amount <= 0:
            return False, "Enter a valid amount."

        if amount > self.balance:
            return False, "Insufficient balance."

        self.balance -= amount

        self.transactions.append({
            "type": "DEBIT",
            "amount": amount,
            "balance": self.balance,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        return True, f"₹{amount:,.2f} debited successfully."


# =========================================================
# GLOBAL VARIABLES
# =========================================================

account = None
generated_otp = None


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("MyBank - Secure Banking")
root.geometry("500x600")
root.configure(bg="#eef2ff")
root.resizable(False, False)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg="#172554",
    height=130
)

header.pack(fill="x")

tk.Label(
    header,
    text="MYBANK",
    font=("Arial", 30, "bold"),
    bg="#172554",
    fg="white"
).pack(pady=(25, 5))

tk.Label(
    header,
    text="Secure Digital Banking",
    font=("Arial", 11),
    bg="#172554",
    fg="#cbd5e1"
).pack()


# =========================================================
# LOGIN CARD
# =========================================================

login_card = tk.Frame(
    root,
    bg="white",
    padx=35,
    pady=30
)

login_card.pack(
    padx=40,
    pady=35,
    fill="both"
)

tk.Label(
    login_card,
    text="Secure Login",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#172554"
).pack()

tk.Label(
    login_card,
    text="Enter your account details",
    font=("Arial", 10),
    bg="white",
    fg="#64748b"
).pack(pady=(5, 25))


# =========================================================
# ACCOUNT NUMBER
# =========================================================

tk.Label(
    login_card,
    text="Account Number",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

account_entry = tk.Entry(
    login_card,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)

account_entry.pack(
    fill="x",
    pady=(5, 15),
    ipady=7
)


# =========================================================
# MOBILE NUMBER
# =========================================================

tk.Label(
    login_card,
    text="Mobile Number",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

mobile_entry = tk.Entry(
    login_card,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)

mobile_entry.pack(
    fill="x",
    pady=(5, 15),
    ipady=7
)


# =========================================================
# OPENING BALANCE
# =========================================================

tk.Label(
    login_card,
    text="Opening Balance",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

balance_entry = tk.Entry(
    login_card,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)

balance_entry.pack(
    fill="x",
    pady=(5, 20),
    ipady=7
)


# =========================================================
# OTP WINDOW
# =========================================================

def otp_window():

    global generated_otp

    # Generate 6 digit OTP
    generated_otp = str(
        random.randint(100000, 999999)
    )

    print("DEMO OTP:", generated_otp)

    otp = tk.Toplevel(root)

    otp.title("MyBank - OTP Verification")
    otp.geometry("500x500")
    otp.configure(bg="#eef2ff")
    otp.resizable(False, False)

    # ---------------- HEADER ----------------

    otp_header = tk.Frame(
        otp,
        bg="#172554",
        height=110
    )

    otp_header.pack(fill="x")

    tk.Label(
        otp_header,
        text="OTP VERIFICATION",
        font=("Arial", 23, "bold"),
        bg="#172554",
        fg="white"
    ).pack(pady=30)

    # ---------------- CARD ----------------

    card = tk.Frame(
        otp,
        bg="white",
        padx=35,
        pady=30
    )

    card.pack(
        padx=40,
        pady=35,
        fill="both"
    )

    tk.Label(
        card,
        text="Verify your mobile",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#172554"
    ).pack()

    # Mask mobile number

    mobile = mobile_entry.get()

    if len(mobile) >= 4:
        masked_mobile = "******" + mobile[-4:]
    else:
        masked_mobile = mobile

    tk.Label(
        card,
        text=f"OTP sent to {masked_mobile}",
        font=("Arial", 10),
        bg="white",
        fg="#64748b"
    ).pack(pady=8)

    # ---------------- DEMO OTP ----------------

    otp_display = tk.Label(
        card,
        text=f"DEMO OTP: {generated_otp}",
        font=("Arial", 13, "bold"),
        bg="#fef3c7",
        fg="#92400e",
        padx=10,
        pady=10
    )

    otp_display.pack(
        pady=15
    )

    # ---------------- OTP ENTRY ----------------

    otp_entry = tk.Entry(
        card,
        font=("Arial", 18),
        justify="center",
        bd=1,
        relief="solid"
    )

    otp_entry.pack(
        fill="x",
        ipady=8,
        pady=10
    )

    # ---------------- VERIFY ----------------

    def verify_otp():

        entered_otp = otp_entry.get()

        if entered_otp == generated_otp:

            messagebox.showinfo(
                "Success",
                "OTP verified successfully!"
            )

            otp.destroy()
            root.withdraw()

            banking_dashboard()

        else:

            messagebox.showerror(
                "Invalid OTP",
                "The OTP you entered is incorrect."
            )

    tk.Button(
        card,
        text="VERIFY OTP",
        command=verify_otp,
        bg="#2563eb",
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        fill="x",
        ipady=10,
        pady=10
    )


# =========================================================
# SEND OTP
# =========================================================

def send_otp():

    global account

    account_no = account_entry.get()
    mobile = mobile_entry.get()
    balance = balance_entry.get()

    # Validation

    if not account_no:
        messagebox.showerror(
            "Error",
            "Enter account number."
        )
        return

    if not mobile.isdigit() or len(mobile) != 10:

        messagebox.showerror(
            "Error",
            "Enter a valid 10-digit mobile number."
        )

        return

    try:

        opening_balance = float(balance)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter a valid opening balance."
        )

        return

    if opening_balance < 0:

        messagebox.showerror(
            "Error",
            "Balance cannot be negative."
        )

        return

    # Create account

    account = Account(
        account_no,
        mobile,
        opening_balance
    )

    # Open OTP screen

    otp_window()


# =========================================================
# SEND OTP BUTTON
# =========================================================

tk.Button(
    login_card,
    text="SEND OTP",
    command=send_otp,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
).pack(
    fill="x",
    ipady=10
)


# =========================================================
# BANKING DASHBOARD
# =========================================================

def banking_dashboard():

    bank = tk.Toplevel(root)

    bank.title("MyBank - Dashboard")
    bank.geometry("1000x750")
    bank.configure(bg="#f1f5f9")
    bank.resizable(False, False)

    # =====================================================
    # HEADER
    # =====================================================

    header = tk.Frame(
        bank,
        bg="#172554",
        height=80
    )

    header.pack(fill="x")

    tk.Label(
        header,
        text="MYBANK",
        font=("Arial", 25, "bold"),
        bg="#172554",
        fg="white"
    ).pack(
        side="left",
        padx=30,
        pady=20
    )

    tk.Label(
        header,
        text=f"Account: {account.account_no}",
        font=("Arial", 11),
        bg="#172554",
        fg="#cbd5e1"
    ).pack(
        side="right",
        padx=30
    )


    # =====================================================
    # BALANCE
    # =====================================================

    balance_card = tk.Frame(
        bank,
        bg="#2563eb",
        height=150
    )

    balance_card.pack(
        padx=35,
        pady=25,
        fill="x"
    )

    tk.Label(
        balance_card,
        text="TOTAL BALANCE",
        font=("Arial", 12, "bold"),
        bg="#2563eb",
        fg="#dbeafe"
    ).pack(pady=(25, 5))

    balance_label = tk.Label(
        balance_card,
        text=f"₹ {account.balance:,.2f}",
        font=("Arial", 32, "bold"),
        bg="#2563eb",
        fg="white"
    )

    balance_label.pack()


    # =====================================================
    # TRANSACTION SECTION
    # =====================================================

    transaction = tk.Frame(
        bank,
        bg="white",
        padx=25,
        pady=20
    )

    transaction.pack(
        padx=35,
        fill="x"
    )

    tk.Label(
        transaction,
        text="Make a Transaction",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#172554"
    ).pack(
        anchor="w",
        pady=(0, 15)
    )

    amount_entry = tk.Entry(
        transaction,
        font=("Arial", 13),
        bd=1,
        relief="solid"
    )

    amount_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=8
    )


    # =====================================================
    # NOTIFICATION FUNCTION
    # =====================================================

    def show_notification(transaction_type, amount):

        if transaction_type == "CREDIT":

            message = (
                f"₹{amount:,.2f} has been credited "
                f"to your account.\n\n"
                f"Available Balance: "
                f"₹{account.balance:,.2f}"
            )

        else:

            message = (
                f"₹{amount:,.2f} has been debited "
                f"from your account.\n\n"
                f"Available Balance: "
                f"₹{account.balance:,.2f}"
            )

        messagebox.showinfo(
            f"{transaction_type} Notification",
            message
        )


    # =====================================================
    # UPDATE BALANCE
    # =====================================================

    def update_balance():

        balance_label.config(
            text=f"₹ {account.balance:,.2f}"
        )


    # =====================================================
    # ADD HISTORY
    # =====================================================

    def add_history(transaction_type, amount):

        now = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        if transaction_type == "CREDIT":

            text = (
                f"🟢 CREDIT    "
                f"+ ₹{amount:,.2f}    "
                f"Balance: ₹{account.balance:,.2f}    "
                f"{now}"
            )

        else:

            text = (
                f"🔴 DEBIT     "
                f"- ₹{amount:,.2f}    "
                f"Balance: ₹{account.balance:,.2f}    "
                f"{now}"
            )

        history_list.insert(
            tk.END,
            text
        )


    # =====================================================
    # CREDIT
    # =====================================================

    def credit_money():

        try:

            amount = float(
                amount_entry.get()
            )

            success, result = account.credit(
                amount
            )

            if success:

                update_balance()

                add_history(
                    "CREDIT",
                    amount
                )

                amount_entry.delete(
                    0,
                    tk.END
                )

                show_notification(
                    "CREDIT",
                    amount
                )

            else:

                messagebox.showerror(
                    "Credit Failed",
                    result
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )


    # =====================================================
    # DEBIT
    # =====================================================

    def debit_money():

        try:

            amount = float(
                amount_entry.get()
            )

            success, result = account.debit(
                amount
            )

            if success:

                update_balance()

                add_history(
                    "DEBIT",
                    amount
                )

                amount_entry.delete(
                    0,
                    tk.END
                )

                show_notification(
                    "DEBIT",
                    amount
                )

            else:

                messagebox.showerror(
                    "Debit Failed",
                    result
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )


    # =====================================================
    # CREDIT BUTTON
    # =====================================================

    tk.Button(
        transaction,
        text="CREDIT",
        command=credit_money,
        bg="#16a34a",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        side="left",
        padx=10,
        ipadx=20,
        ipady=8
    )


    # =====================================================
    # DEBIT BUTTON
    # =====================================================

    tk.Button(
        transaction,
        text="DEBIT",
        command=debit_money,
        bg="#dc2626",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        side="left",
        ipadx=20,
        ipady=8
    )


    # =====================================================
    # HISTORY
    # =====================================================

    history_frame = tk.Frame(
        bank,
        bg="white"
    )

    history_frame.pack(
        padx=35,
        pady=25,
        fill="both",
        expand=True
    )

    tk.Label(
        history_frame,
        text="Transaction History",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#172554"
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )

    history_list = tk.Listbox(
        history_frame,
        font=("Arial", 11),
        bd=0,
        bg="#f8fafc"
    )

    history_list.pack(
        padx=20,
        pady=(0, 20),
        fill="both",
        expand=True
    )


    # =====================================================
    # LOGOUT
    # =====================================================

    def logout():

        bank.destroy()
        root.deiconify()

    tk.Button(
        bank,
        text="LOGOUT",
        command=logout,
        bg="#475569",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat"
    ).pack(
        pady=(0, 15),
        ipadx=30,
        ipady=6
    )


# =========================================================
# START
# =========================================================

root.mainloop()