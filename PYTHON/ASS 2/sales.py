sales_data = [
    {"product_name": "Silver Ring", "category": "Jewellery", "units_sold": 150, "unit_price": 200.0},
    {"product_name": "iphone", "category": "Mobile", "units_sold": 120, "unit_price": 150000.0},
    {"product_name": "Jacket", "category": "Clothes", "units_sold": 200, "unit_price": 3000.0},
    {"product_name": "Oneplus", "category": "Mobile", "units_sold": 100, "unit_price": 20000.0},
    # Add more product data as needed
]
def total_sales(data):
    return sum(item['units_sold'] * item['unit_price'] for item in data)

def average_sales(data):
    return total_sales(data) / len(data)

def top_selling_product(data):
    return max(data, key=lambda x: x['units_sold'])

def sales_by_category(data):
    category_sales = {}
    for item in data:
        if item['category'] not in category_sales:
            category_sales[item['category']] = 0
        category_sales[item['category']] += item['units_sold'] * item['unit_price']
    return category_sales
def main():
    print("Total Sales: $", total_sales(sales_data))
    print("Average Sales: $", average_sales(sales_data))
    
    top_product = top_selling_product(sales_data)
    print(f"Top-Selling Product: {top_product['product_name']} with {top_product['units_sold']} units sold.")
    
    category_sales = sales_by_category(sales_data)
    print("Sales by Category:")
    for category, sales in category_sales.items():
        print(f"{category}: ${sales}")

if __name__ == "__main__":
    main()

