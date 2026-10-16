
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd  # type: ignore[reportMissingModuleSource]

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    """,
    conn
)


# STEP 3
# Select last name first, followed by employee number
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    """,
    conn
)


# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    """,
    conn
)


# STEP 5
# Classify employees as Executive or Not Executive
df_executive = pd.read_sql(
    """
    SELECT
        *,
        CASE
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing')
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
    """,
    conn
)


# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees
    """,
    conn
)


# STEP 7
# Return the first two letters of each job title
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    """,
    conn
)


# STEP 8
# Calculate each order total, round it, and sum the results
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
    """,
    conn
).sum()


# STEP 9
# Return order date, day, month, and year
df_day_month_year = pd.read_sql(
    """
    SELECT
        orders.orderDate,
        STRFTIME('%d', orders.orderDate) AS day,
        STRFTIME('%m', orders.orderDate) AS month,
        STRFTIME('%Y', orders.orderDate) AS year
    FROM orderDetails
    JOIN orders ON orderDetails.orderNumber = orders.orderNumber
    """,
    conn
)


# Close the database connection
conn.close()
