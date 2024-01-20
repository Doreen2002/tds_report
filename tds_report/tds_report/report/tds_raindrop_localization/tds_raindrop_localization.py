# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [], []
	columns =[
	{
            'fieldname': 'Supplier',
            'label': _('Supplier'),
            'fieldtype': 'Link',
	    'option': 'Supplier',
           
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
	return columns, data
