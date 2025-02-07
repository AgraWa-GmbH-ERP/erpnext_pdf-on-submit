# Copyright (c) 2021, Raffael Meyer and contributors
# For license information, please see license.txt
from frappe.model.document import Document
import frappe
from frappe import _
from pdf_on_submit.safe_exec import get_context


class EnabledDocType(Document):
	def validate_condition(self):
		if not self.condition:
			return

		temp_doc = frappe.new_doc(self.document_type)
		try:
			frappe.safe_eval(self.condition, None, get_context(temp_doc.as_dict()))
		except Exception:
			frappe.throw(_("The Condition '{0}' is invalid").format(self.condition))
