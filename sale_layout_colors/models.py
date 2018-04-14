# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2016-2016 BADEP. All Rights Reserved.
#    Author: Khalid HAZAM <k.hazam@badep.ma>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields as oldfields, osv
from openerp import tools
from openerp import fields, models, api
from dateutil.relativedelta import relativedelta
import openerp.addons.decimal_precision as dp
from openerp.tools.float_utils import float_round

class SaleLayoutCategory(models.Model):
    _inherit = 'sale_layout.category'
    color_code = fields.Char(string='Hex Code', required=True, size=7, default='#aaaaaa')
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: