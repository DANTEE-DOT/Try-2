import streamlit as st
from savings_account import SavingsAccount

st.title("💰 Savings Account")

if "savings" not in st.session_state:
    st.session_state.savings = SavingsAccount()

action = st.selectbox("Choose action", ["Deposit", "Withdraw", "Apply Interest", "View Balance"])

amount = st.number_input("Amount", min_value=0.0, step=10.0)

if st.button("Submit"):
    acc = st.session_state.savings
    if action == "Deposit":
        if acc.deposit(amount):
            st.success("Deposit successful")
        else:
            st.error("Deposit failed")
    elif action == "Withdraw":
        if acc.withdraw(amount):
            st.success("Withdrawal successful")
        else:
            st.error("Insufficient funds")
    elif action == "Apply Interest":
        interest = acc.apply_interest()
        st.success(f"Interest of {interest:.2f} applied!")

st.info(f"Current Balance: ₦{st.session_state.savings.get_balance():.2f}")