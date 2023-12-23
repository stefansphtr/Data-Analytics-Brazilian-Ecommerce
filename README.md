# 📊 Project Data Analytics: Brazilian E-Commerce Public Dataset by Olist

## 📚 Table of Contents

- [📊 Project Data Analytics: Brazilian E-Commerce Public Dataset by Olist](#-project-data-analytics-brazilian-e-commerce-public-dataset-by-olist)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [💻 Installation](#-installation)
  - [🔄 Project Workflow](#-project-workflow)
  - [🗂️ Entity Relationship Diagram](#️-entity-relationship-diagram)
  - [📈 Dashboard Explanation](#-dashboard-explanation)


## 🎯 Introduction

This project focuses on the analysis of a public dataset provided by Olist, a Brazilian e-commerce company. The dataset includes information about customer orders, products, payments, reviews, and more. The goal of this project is to extract meaningful insights from the data that can help improve business strategies and customer experience.

## 💻 Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**

   Clone the repository using git:

   ```bash
   git clone https://github.com/stefansphtr/Data-Analytics-Brazilian-Ecommerce/tree/data-visualization.git
   ```

2. **Set up a virtual environment** (Optional)

   It's recommended to create a virtual environment to keep the dependencies required by this project separate from your system's Python environment. Here's how you can create a virtual environment:

   ```bash
   python3 -m venv env
   ```

   Activate the virtual environment:

   On Windows:

   ```bash
   .\env\Scripts\activate
   ```

   On Unix or MacOS:

   ```ls
   source env/bin/activate
   ```

3. **Install the dependencies**

   Navigate to the project directory and install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**

   Now you can run the project easily by click on the run all button in the jupyter notebook

## 🔄 Project Workflow

1. **Data Wrangling**
    
   The first step of the project is to clean and prepare the data for analysis. The data wrangling process includes:

   - Handling missing values
   - Handling duplicate values
   - Handling incorrect data types
   - Handling outliers
   - Handling inconsistent data
   - Handling data redundancy
   - Handling data normalization

2. **Exploratory Data Anlaysis**

    The second step of the project is to explore the data and extract meaningful insights. The exploratory data analysis process includes:
    
    - Order Analysis
    - Product Analysis
    - Payment Analysis
    - Customer Analysis
    - Reviews Analysis
    - Sellers Analysis

3. **Data Visualization**
   
    The third step of the project is to visualize the data and extract meaningful insights. The data visualization process includes:
    
    - Product Category with most outstanding reviews given by customers
    - Visualize OTD(On Time Delivery) rate of orders
    - Visualize the demographics of customers
    - Visualize the frequency of purchases made by customers
    - Visualize the monetary value of purchases made by customers
    - Visualize the recent purchases made by customers
    - Visualize the customers segmentation based on RFM analysis
  
4. **Dashboard**

    The last step of the project is to create a dashboard that can be used to visualize the data and extract meaningful insights. The dashboard includes:
    
    - Product Category sales performance
    - Daily sales performance

## 🗂️ Entity Relationship Diagram

![ERD](https://i.imgur.com/HRhd2Y0.png)

The Entity Relationship Diagram (ERD) provides a comprehensive graphical view of the logical structure of our database. It helps to understand how different tables are related to each other in the database.

The ERD for this project is defined in the [db_schema.vuerd.json](ERD/db_schema.vuerd.json) file and can be viewed using tools that support the Vuerd format.

The diagram includes the following tables:

- `customers_dataset`: This dataset has information about the customer and its location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.
  
- `geolocation_dataset`: This dataset has information Brazilian zip codes and its lat/lng coordinates.
  
- `orders_dataset`: This is the core dataset of the project.
  
- `order_items_dataset`: This dataset includes data about the items purchased within each order.
  
- `order_payments_dataset`: This dataset includes data about the orders payment options.
  
- `order_reviews_dataset`: This dataset includes data about the reviews made by the customers.
  
- `products_dataset`: This dataset includes data about the products sold by Olist.
  
- `product_category_name_translation`: This dataset translates the product_category_name to english.
  
- `sellers_dataset`: This dataset includes data about the sellers that fulfilled orders made at Olist.

Each table is linked to one or more other tables through foreign keys, representing the relationships between different entities in the e-commerce business model.

## 📈 Dashboard Explanation

Follow these steps to run the dashboard on your local machine:

1. **Run the Streamlit app**

   Navigate to the project directory and run the Streamlit app using the following command:

   ```sh
   streamlit run dashboard/dashboard.py
   ```

   This will start the Streamlit server and open a new page in your default web browser with the URL of the Streamlit app.

2. **Use the dashboard**

The dashboard provides a visual representation of sales performance data. Here's how to use it:

- **Filter the data**

   Use the filters in the sidebar to select the city, customer segmentation, and date range you're interested in. The dashboard will update automatically to reflect your selections.

- **View key performance indicators**

   At the top of the dashboard, you'll see key performance indicators (KPIs) such as total sales, average rating, and average sales per order.

- **Explore the charts**

   The dashboard includes two charts: Sales by Product Line and Sales by Day. These charts provide a visual representation of the sales data based on your filter selections.
