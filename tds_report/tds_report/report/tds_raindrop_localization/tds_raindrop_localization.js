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
	]
};
