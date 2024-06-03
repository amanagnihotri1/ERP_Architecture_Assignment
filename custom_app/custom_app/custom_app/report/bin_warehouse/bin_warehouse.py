# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data = [], []
    
    columns = [
        {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse"},
        {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data"},
        {"label": "Bin Quantity", "fieldname": "bin_qty", "fieldtype": "Float"}
    ]
    
    data = stock_data(filters)
    
    return columns, data

@frappe.whitelist()
def stock_data(warehouse, item_code):
    # Ensure the fields are indexed
    frappe.db.sql("""
        ALTER TABLE tabBin
        ADD INDEX idx_warehouse_item_code (warehouse, item_code);
    """)
    
    # Query to retrieve stock data using indexing
    stck_data = frappe.db.get_value('Bin', {
        'warehouse': warehouse,
        'item_code': item_code
    }, ['actual_qty', 'reserved_qty', 'ordered_qty'], as_dict=True)
    
    return stck_data
