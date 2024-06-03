import frappe
import json

@frappe.whitelist(allow_guest=True)
def get_item_details(item_code): #This function Implements caching api present in frappe
    cache_key = f'item_details_{item_code}'
    item_details = frappe.cache().get_value(cache_key)
    if item_details:
        return json.loads(item_details)  # Convert JSON string back to Python object

    item_details = frappe.db.get_value('Item', item_code, ['item_name', 'description', 'stock_uom'], as_dict=True)
    if item_details:
        frappe.cache().set_value(cache_key, json.dumps(item_details), expires_in_sec=3600)  # Cache for 1 hour
    return item_details
