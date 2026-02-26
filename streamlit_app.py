import streamlit as st
import pandas as pd

st.title("📊 Simple vs Compound Interest Calculator")
st.markdown("Learn how interest grows!")

# Choice selector
interest_type = st.radio(
    "Choose interest type:",
    ["Simple Interest", "Compound Interest"]
)

# Common inputs
P = st.number_input("Principal amount ($)", min_value=0.0, value=1000.0)
r = st.number_input("Annual interest rate (%)", min_value=0.0, value=5.0) / 100
years = st.number_input("Number of years", min_value=1, max_value=30, value=5)

if interest_type == "Simple Interest":
    # Simple interest calculation
    data = []
    for year in range(1, years + 1):
        interest = P * r * year
        total = P + interest
        data.append({"Year": year, "Interest": f"${interest:.2f}", "Total": f"${total:.2f}"})
    
    st.subheader("Year-by-Year Breakdown")
    st.table(pd.DataFrame(data))
    st.success(f"Final amount: ${P + (P * r * years):,.2f}")

else:  # Compound Interest
    # Compounding frequency selector
    freq = st.selectbox(
        "Compounding frequency:",
        ["Annually", "Semi-annually", "Quarterly", "Monthly"]
    )
    
    freq_map = {"Annually": 1, "Semi-annually": 2, "Quarterly": 4, "Monthly": 12}
    m = freq_map[freq]
    
    # Compound calculation
    data = []
    amount = P
    for year in range(1, years + 1):
        for _ in range(m):
            amount = amount * (1 + (r / m))
        data.append({"Year": year, "Total": f"${amount:,.2f}"})
    
    st.subheader("Year-by-Year Growth")
    st.table(pd.DataFrame(data))
    st.success(f"Final amount: ${amount:,.2f}")
