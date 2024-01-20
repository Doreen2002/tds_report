# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt

import frappe
from frappe import _

 

def execute(filters=None):
	columns, data = [], []
	columns =[
	{
            'fieldname': 'Supplier',
            'label': _('Supplier'),
            'fieldtype': 'Link',
	    'options': 'Supplier',
           
        },
	{
            'fieldname': 'account_head',
            'label': _('Account Head'),
            'fieldtype': 'Link',
	    'options': 'Account Head'
           
        },
	{
            'fieldname': 'tds_amount',
            'label': _('TDs Amount'),
            'fieldtype': 'Currency',
           
        },
	{
            'fieldname': 'paid_amount',
            'label': _('Paid Amount'),
            'fieldtype': 'Currency',
        },
	{
            'fieldname': 'tds_balance',
            'label': _('Paid Amount'),
            'fieldtype': 'Currency',
		
	   
           
        }
	]
	if not filters.account_head:
		frappe.throw("Please Select Account Head to View Report")
	supplier = frappe.db.get_list("Supplier", fields=['*'])
	for sup in supplier:
		total_tds_amount = 0
		total_tds_paid_amount = 0
		total_tds_balance_amount = 0
		purchase_invoice = frappe.db.get_list("Purchase Invoice", filters={"supplier":sup.name}, fields=['*'])
		for pur in purchase_invoice:
			if filters.account_head:
				tds = frappe.db.get_all("Purchase Taxes and Charges Template", filters={"custom_when_to_use":filters.account_head}, fields=['*'])
				for t in tds:
					if t.add_deduct_tax == "Deduct" and "TDS" in t.account_head:
						total_tds_amount += t.tax_amount
		data.append([sup.name, filters.account_head, total_tds_amount, total_tds_paid_amount, total_tds_balance_amount])
	return columns, data
