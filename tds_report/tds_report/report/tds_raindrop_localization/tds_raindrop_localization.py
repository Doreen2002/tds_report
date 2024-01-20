# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt

import frappe
from frappe import _

 

def execute(filters=None):
	columns =[
	{
            'fieldname': 'TDs Type/ Party Name',
            'label': _('Supplier'),
            'fieldtype': 'Link',
	    'options': 'Supplier',
           
        },
	{
            'fieldname': 'account_head',
            'label': _('Account Head'),
            'fieldtype': 'Link',
	    'options': 'Account Head',
	    'default': '11131 TDS on Rent'
           
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
	if  filters.account_head == None:
		frappe.throw("Please Select Account Head to View Report")
	supplier = frappe.db.get_list("Supplier", fields=['*'])
	for sup in supplier:
		total_tds_amount = 0
		total_tds_paid_amount = 0
		total_tds_balance_amount = 0
		purchase_invoice = frappe.db.get_list("Purchase Invoice", filters={"supplier":sup.name}, fields=['*'])
		for pur in purchase_invoice:
			tds = frappe.db.get_all("Purchase Taxes and Charges", filters={"parent":pur.name, "add_deduct_tax":"Deduct" , "custom_when_to_use":filters.account_head}, fields=['*'])
			frappe.throw("{tds}")
			for t in tds:
				total_tds_amount += t.tax_amount
			journal = frappe.db.get_list("Journal Entry", fields=['*'])
			# for jour in journal:
			# 	journal_tds = frappe.db.get_all("Journal Entry Account", filters={"parent":jour.name,"custom_when_to_use":filters.account_head, "reference_type":"Purchase Invoice", "reference_name":pur.name}, fields=['*'])
			# 	for tds in journal_tds:
			# 		total_tds_paid_amount += tds.debit
		
		data.append([sup.name, filters.account_head, total_tds_amount, total_tds_paid_amount, total_tds_balance_amount])
	return columns, data
