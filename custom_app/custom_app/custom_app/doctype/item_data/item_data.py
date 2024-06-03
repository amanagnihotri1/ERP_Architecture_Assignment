# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.password import encrypt
@frappe.whitelist(allow_guest=1)
    def give_fullName(self, first_name, last_name): #this is a whitelisted method getting called using postman
        try:
            full_name = f"these are the arguments passed to the function call {first_name}, {last_name}"
            return full_name
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), str(e))
            frappe.throw(frappe._("An error occurred: {0}").format(e))
class Item_data(Document):
    def before_save(self):
        if self.aadhar_num and not self.is_encrypted(self.aadhar_num):
                self.aadhar_num = encrypt(self.aadhar_num)
        try:
            data = frappe.db.sql("""SELECT * FROM `tabItem_data` WHERE item_qty>2""", as_dict=1)
            if len(data)<5:
                frappe.log_error(frappe.get_traceback(),"Data is empty")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), str(e))
    def is_encrypted(self, text):
        """ Encrypted field value starts with "gAAAAAB" """
        return text.startswith("gAAAAAB")
   