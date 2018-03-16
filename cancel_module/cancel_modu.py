from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def cancel_all_links_sales(doc,method):
	dokumen_patokan = doc.name

	# payment Entry
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabPayment Entry Reference`
	WHERE docstatus = 1 AND reference_name = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Payment Entry", row[0])
		doc_pe.cancel()

	# Journal Entry
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabJournal Entry Account`
	WHERE docstatus = 1 AND reference_name = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Journal Entry", row[0])
		doc_pe.cancel()

	# Sales Invoice
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabSales Invoice Item`
	WHERE docstatus = 1 AND sales_order = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Sales Invoice", row[0])
		doc_pe.cancel()

	# Delivery Note
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabDelivery Note Item`
	WHERE docstatus = 1 AND against_sales_order = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Delivery Note", row[0])

        # packing list
        # list_pl = frappe.db.sql(""" SELECT name
    	# FROM `tabPacking Slip`
    	# WHERE docstatus = 1 AND delivery_note = "{}" GROUP BY name """.format(row[0]))
        # for row2 in list_pl :
        #     doc_pe2 = frappe.get_doc("Packing Slip", row[0])
        #     doc_pe2.cancel()

		doc_pe.cancel()

@frappe.whitelist()
def cancel_all_links_purchase(doc,method):
	dokumen_patokan = doc.name

	# payment Entry
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabPayment Entry Reference`
	WHERE docstatus = 1 AND reference_name = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Payment Entry", row[0])
		doc_pe.cancel()

	# Journal Entry
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabJournal Entry Account`
	WHERE docstatus = 1 AND reference_name = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Journal Entry", row[0])
		doc_pe.cancel()

	# Purchase Invoice
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabPurchase Invoice Item`
	WHERE docstatus = 1 AND purchase_order = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Purchase Invoice", row[0])
		doc_pe.cancel()

	# Purchase Receipt
	list_pe = frappe.db.sql(""" SELECT parent
	FROM `tabPurchase Receipt Item`
	WHERE docstatus = 1 AND  purchase_order = "{}" GROUP BY parent """.format(dokumen_patokan))

	for row in list_pe:
		doc_pe = frappe.get_doc("Purchase Receipt", row[0])

        # # Landed Cost Voucher
        # list_pl = frappe.db.sql(""" SELECT parent
    	# FROM `tabLanded Cost Voucher Item`
    	# WHERE docstatus = 1 AND receipt_document = "{}" GROUP BY parent """.format(row[0]))
        # for row2 in list_pl :
        #     doc_pe2 = frappe.get_doc("Landed Cost Voucher", row[0])
        #     doc_pe2.cancel()

		doc_pe.cancel()
