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
    
    data = get_bin_stock_data(filters)
    
    return columns, data

def get_bin_stock_data():
    bin_data = frappe.db.sql("""
        SELECT
            bin.warehouse,
            bin.item_code,
            item.item_name,
            bin.actual_qty as bin_qty
        FROM
            `tabBin` bin
        JOIN
            `tabItem` item ON bin.item_code = item.name
        """, as_dict=1)
    
    return bin_data
