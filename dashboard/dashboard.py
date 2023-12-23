import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Sales Performance Dashboard",page_icon=":bar_chart:" , layout="wide")

# ! Load the dataset

all_df = pd.read_csv('data/all_data.csv')

# --Sidebar--

with st.sidebar:
    # ! Add company's logo
    st.image("https://i.pinimg.com/originals/65/dd/2f/65dd2f283db26ce78dd6ab61a489b90e.jpg", width=250)
    st.header("Filter here:")

city = st.sidebar.multiselect(
    "Select the City:",
    options=all_df["customer_city"].unique(),
    default=[],
    placeholder="Select a city",
)

all_df["customer_segment"].fillna("Mid Value Customers", inplace=True)

customer_type = st.sidebar.multiselect(
    "Select the Customer Segmentation:",
    options=all_df["customer_segment"].unique(),
    default=[],
    placeholder="Select a customer segment",
)

min_date = pd.to_datetime(all_df["order_purchase_timestamp"]).min()
max_date = pd.to_datetime(all_df["order_purchase_timestamp"]).max()

date_range = st.sidebar.date_input(
    "Select the Date Range:",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date,
)

all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])

df_selection = all_df.query(
    "customer_city == @city & customer_segment == @customer_type & order_purchase_timestamp >= @date_range[0] & order_purchase_timestamp <= @date_range[1]"
)

# ! Check if the df_selection is empty
if df_selection.empty:
    st.warning("No data available for the selected filters.")
    st.stop() # Stop the app from running further
    
# --Main Panel--

st.title("Sales Performance Dashboard")
st.markdown("##")

# ! TOP KPI's
total_sales = int(df_selection["total_price"].sum())
average_rating = round(df_selection["review_score"].mean(), 1)
if np.isnan(average_rating):
    star_rating = ":star:" * 0
else:
    star_rating = ":star:" * int(round(average_rating, 0))
average_sales_per_order = round(df_selection["total_price"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales")
    st.subheader(f"R$ {total_sales:,}")
    
with middle_column:
    st.subheader("Average Rating")
    st.subheader(f"{star_rating} {average_rating}")
with right_column:
    st.subheader("Average Sales per Order")
    st.subheader(f"R$ {average_sales_per_order:,}")

st.markdown("""---""")

# ! Sales by Product Line (Bar Chart)
sales_by_product_line = df_selection.groupby(by=["product_category_name_english"])[["total_price"]].sum().sort_values(by="total_price")
fig_product_sales = px.bar(
    sales_by_product_line,
    x="total_price",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#E36414"] * len(sales_by_product_line),
    template="plotly_white",
    )
fig_product_sales.update_layout(
    xaxis=(dict(showgrid=False)),
    xaxis_title="Total Sales",
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False, showticklabels=True),
    yaxis_title="Product Category",
)

# ! Daily Sales [bar chart]
# Extract the day from the order_purchase_timestamp column
df_selection["order_purchase_timestamp"] = pd.to_datetime(df_selection["order_purchase_timestamp"])
df_selection["order_purchase_day"] = df_selection["order_purchase_timestamp"].dt.day

sales_by_day = df_selection.groupby(by=["order_purchase_day"])[["total_price"]].sum().reset_index()

if len(sales_by_day) > 0:
    color_discrete_sequence = ["#E36414"] * len(sales_by_day)
else:
    color_discrete_sequence = ["#E36414"]

fig_daily_sales = px.bar(
    sales_by_day,
    x="order_purchase_day",
    y="total_price",
    title="<b>Sales by Day</b>",
    color_discrete_sequence=color_discrete_sequence,
    template="plotly_white",
)
fig_daily_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    xaxis_title="Day",
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    yaxis_title="Sales",
)

# ! Sales by Day and Product Line Tab
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_daily_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

# ---- Hide Streamlit Style ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
