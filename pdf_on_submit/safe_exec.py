# Copyright (c) 2021, Raffael Meyer and contributors
# For license information, please see license.txt
import frappe
from frappe.utils.safe_exec import VALID_UTILS
from frappe import _dict


def get_data_utils():
	return _dict({
		key: obj
		for key, obj in frappe.utils.data.__dict__.items()
		if key in VALID_UTILS
	})


def get_context(doc):
	frappe = _dict()
	frappe.utils = get_data_utils()
	return {
		"doc": doc,
		"frappe": frappe,
	}
