import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Customer Churn AI", page_icon="📉", layout="wide")

st.title("📉 E-Commerce Customer Churn Predictor")
st.markdown("Identify at-risk customers before they leave your platform using Machine Learning.")
st.divider()

@st.cache_resource
def load_engine():
    with open('src/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('src/encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    with open('src/columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    with open('src/cat_columns.pkl', 'rb') as f:
        cat_cols = pickle.load(f)
    return model, encoder, columns, cat_cols

model, encoder, columns, cat_cols = load_engine()

st.subheader("Enter Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    account_age = st.number_input("Account Age (Months)", min_value=1, value=12)
    avg_order = st.number_input("Avg Order Value ($)", min_value=1.0, value=50.0)
    total_orders = st.number_input("Total Orders", min_value=1, value=5)
    days_since = st.number_input("Days Since Last Purchase", min_value=0, value=10)
    loyalty = st.selectbox("Loyalty Member?", ["Yes", "No"])
    
with col2:
    discount_rate = st.slider("Discount Usage Rate", 0.0, 1.0, 0.2)
    return_rate = st.slider("Return Rate", 0.0, 1.0, 0.05)
    support_tickets = st.number_input("Support Tickets", min_value=0, value=0)
    browsing_freq = st.slider("Browsing Frequency (per week)", 0.0, 20.0, 5.0)
    
with col3:
    cart_abandon = st.slider("Cart Abandonment Rate", 0.0, 1.0, 0.3)
    review_score = st.slider("Product Review Score", 1.0, 5.0, 4.0)
    engagement = st.slider("Engagement Score", 0.0, 10.0, 7.0)
    satisfaction = st.slider("Satisfaction Score", 0.0, 10.0, 8.0)
    price_sens = st.slider("Price Sensitivity Index", 0.0, 10.0, 5.0)

st.write("")

if st.button("Predict Churn Risk", type="primary", use_container_width=True):
    input_dict = {
        'account_age_months': account_age,
        'avg_order_value': avg_order,
        'total_orders': total_orders,
        'days_since_last_purchase': days_since,
        'discount_usage_rate': discount_rate,
        'return_rate': return_rate,
        'customer_support_tickets': support_tickets,
        'loyalty_member': loyalty,
        'browsing_frequency_per_week': browsing_freq,
        'cart_abandonment_rate': cart_abandon,
        'product_review_score_avg': review_score,
        'engagement_score': engagement,
        'satisfaction_score': satisfaction,
        'price_sensitivity_index': price_sens
    }
    
    input_df = pd.DataFrame([input_dict])
    input_df[cat_cols] = encoder.transform(input_df[cat_cols])
    input_df = input_df[columns]
    
    prediction = model.predict(input_df)[0]
    
    st.divider()
    if prediction == "Yes":
        st.error("**HIGH RISK:** This customer is likely to churn. Consider sending a retention offer!")
    else:
        st.success("**LOW RISK:** This customer is likely to stay loyal.")
        st.balloons()