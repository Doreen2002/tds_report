// Copyright (c) 2024, raindrop and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TDS Raindrop Localization"] = {
	"filters": [
		{
            fieldname: 'account_head',
            label: __('TDS Category'),
            fieldtype: 'Link',
            options: 'TDS Category',
        
        },
	{
            fieldname: 'from_date',
            label: __('From Date'),
            fieldtype: 'Date',
           
        
        },
	{
            fieldname: 'to_date',
            label: __('To Date'),
            fieldtype: 'Date',
           
        
        },
	{
            fieldname: 'supplier',
            label: __('Supplier'),
            fieldtype: 'Link',
	    options: 'Supplier'
           
        
        },
	]
};
