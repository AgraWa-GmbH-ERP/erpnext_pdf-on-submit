# Copyright (c) 2019, Raffael Meyer and contributors
# For license information, please see license.txt
from frappe.model.document import Document


class PDFonSubmitSettings(Document):
	def validate(self):
		for enabled_doctype in self.enabled_for:
			enabled_doctype.validate_condition()
