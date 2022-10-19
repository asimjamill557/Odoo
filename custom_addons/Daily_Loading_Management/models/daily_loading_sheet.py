# -*- coding: utf-8 -*-
from odoo import api, fields, models

class LoadingSheetData(models.Model):
    _name = "loading.get.data"
    _description = "Daily Loading Sheet"

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string= "Gender")