# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import today


def execute(filters=None):
	columns, data = [], []
	columns =[
	{
            'fieldname': 'Supplier',
            'label': _('TDs Type/ Party Name'),
            'fieldtype': 'Link',
	    'options': 'Supplier',
           
        },
	{
            'fieldname': 'account_head',
            'label': _('Account Head'),
            'fieldtype': 'Link',
	    'options': 'TDS Category',
	    'default':'11131 TDS on Rent'
           
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
            'label': _('TDs Balance'),
            'fieldtype': 'Currency',
		
	   
           
        },
	{
            'fieldname': 'pi_date',
            'label': _('Voucher Date'),
            'fieldtype': 'Date',
		
	   
           
        },
	{
            'fieldname': 'voucher_no',
            'label': _('Voucher No'),
            'fieldtype': 'Link',
	    'options': 'Purchase Invoice',
		
	   
           
        },
	{
            'fieldname': 'journal_voucher',
            'label': _('Journal Voucher'),
            'fieldtype': 'Link',
	    'options': 'Journal Entry',
		
	   
           
        },
	{
            'fieldname': 'pi_number',
            'label': _('Submission Number'),
            'fieldtype': 'Link',
	    'options': 'Purchase Invoice',
		
	   
           
        }
	]
	if filters.account_head == None:
		frappe.throw("Please Select Account Head to View Report")
	
	
	filters_list = {}
	if filters.supplier != None:
		filters_list.update({"supplier": filters.supplier})	
	if filters.from_date != None and filters.to_date != None:
		filters_list.update({'posting_date':[ 'between', [filters.from_date, filters.to_date]]})
	if filters.from_date != None and filters.to_date == None:
		filters_list.update({'posting_date':[ 'between', [filters.from_date, today()]]})
	if filters.from_date == None and filters.to_date != None:
		filters_list.update({'posting_date':[ 'between', [filters.to_date, filters.to_date]]})
	purchase_invoice = frappe.db.get_list("Purchase Invoice", filters=filters_list, fields=['*'])
	for pur in purchase_invoice:
		total_tds_amount = 0
		total_tds_paid_amount = 0
		total_tds_balance_amount = 0
		journal_voucher =" "
		submitted_number = ""
		account = filters.account_head
		tds = frappe.db.get_all("Purchase Taxes and Charges", filters={"parent":pur.name, "add_deduct_tax":"Deduct", "custom_when_to_use" : filters.account_head}, fields=['*'])
		for t in tds:
			if t.add_deduct_tax == "Deduct" and "TDS" in t.account_head:
				total_tds_amount += t.tax_amount
			journal_tds = frappe.db.get_all("Journal Entry Account", filters={"custom_tds_category":filters.account_head, "custom_submitted_number": pur.name}, fields=['*'])
			if journal_tds != []:
				for tds in journal_tds:
					total_tds_paid_amount += tds.debit
		total_tds_balance_amount =  total_tds_paid_amount -  total_tds_amount 
		if frappe.db.get_value("Journal Entry Account", {"custom_tds_category":filters.account_head, "custom_submitted_number": pur.name}, 'parent') != None:
			journal_voucher = frappe.db.get_value("Journal Entry Account", {"custom_tds_category":filters.account_head, "custom_submitted_number": pur.name}, 'parent')
		data.append([pur.supplier, filters.account_head, total_tds_amount, total_tds_paid_amount, total_tds_balance_amount , pur.posting_date, pur.name, journal_voucher, pur.name])
	return columns, data
