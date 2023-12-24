import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Set up the page
st.set_page_config(page_title="Sales Performance Dashboard", page_icon=":bar_chart:", layout="wide")

# Load the dataset
all_df = pd.read_csv('data/all_data.csv')
all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])

# Fill missing values
all_df["customer_segment"].fillna("Mid Value Customers", inplace=True)

# Get min and max date
min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

# Create constants to be used in the app
LOGO_URL = "https://i.pinimg.com/originals/65/dd/2f/65dd2f283db26ce78dd6ab61a489b90e.jpg"
BAR_COLOR = "#E36414"

def filter_data(all_df):
    with st.sidebar:
        # Add company's logo
        st.image(LOGO_URL, width=250)
        st.header("Filter here:")

        city = st.sidebar.multiselect(
            "Select the City:",
            options=all_df["customer_city"].unique(),
            default=["sao paulo"],
            placeholder="Select a city",
        )

        customer_type = st.sidebar.multiselect(
            "Select the Customer Segmentation:",
            options=all_df["customer_segment"].unique(),
            default=["Mid Value Customers"],
            placeholder="Select a customer segment",
        )

        date_range = st.sidebar.date_input(
            "Select the Date Range:",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date,
        )

    df_selection = all_df.query(
        "customer_city == @city & customer_segment == @customer_type & order_purchase_timestamp >= @date_range[0] & order_purchase_timestamp <= @date_range[1]"
    )
    
    if df_selection is not None and "order_purchase_timestamp" in df_selection:
        df_selection["order_purchase_day"] = df_selection["order_purchase_timestamp"].dt.day
    else:
        df_selection = pd.DataFrame({"order_purchase_timestamp": pd.date_range(start='1/1/2017', periods=31)})
        df_selection["order_purchase_day"] = df_selection["order_purchase_timestamp"].dt.day

    return df_selection

def display_kpis(all_df):
    # TOP KPI's
    if all_df is not None:
        total_sales = int(all_df["total_price"].sum()) if "total_price" in all_df else 0
        average_rating = round(all_df["review_score"].mean(), 1) if "review_score" in all_df else 0
        star_rating = ":star:" * int(round(average_rating, 0)) if not np.isnan(average_rating) else ":star:" * 0
        average_sales_per_order = round(all_df["total_price"].mean(), 2) if "total_price" in all_df else 0
    else:
        total_sales = 0
        average_rating = 0
        star_rating = ":star:" * 0
        average_sales_per_order = 0

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

def plot_charts(df):
    # Sales by Product Line (Bar Chart)
    if df is not None:
        sales_by_product_line = df.groupby(by=["product_category_name_english"])[["total_price"]].sum().sort_values(by="total_price")
    else:
        sales_by_product_line = None

    if sales_by_product_line is not None:
        fig_product_sales = px.bar(
            sales_by_product_line,
            x="total_price",
            y=sales_by_product_line.index,
            orientation="h",
            title="<b>Sales by Product Line</b>",
            color_discrete_sequence=[BAR_COLOR] * len(sales_by_product_line),
            template="plotly_white",
        )
    else:
        fig_product_sales = go.Figure()


    # Daily Sales [bar chart]
    if df is not None and "order_purchase_timestamp" in df:
        df["order_purchase_day"] = df["order_purchase_timestamp"].dt.day
    else:
        df = pd.DataFrame({"order_purchase_timestamp": pd.date_range(start='1/1/2017', periods=31)})
        df["order_purchase_day"] = df["order_purchase_timestamp"].dt.day
    sales_by_day = df.groupby(by=["order_purchase_day"])[["total_price"]].sum().reset_index()

    color_discrete_sequence = [BAR_COLOR] * len(sales_by_day) if len(sales_by_day) > 0 else [BAR_COLOR]

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

    # Sales by Day and Product Line Tab
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_daily_sales, use_container_width=True)
    right_column.plotly_chart(fig_product_sales, use_container_width=True)

def main():
    # Main Panel
    st.title("Sales Performance Dashboard")
    st.markdown("##")

    df_selection = filter_data(all_df)
    display_kpis(df_selection)
    plot_charts(df_selection)

    # Hide Streamlit Style
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """

    st.markdown(hide_st_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()