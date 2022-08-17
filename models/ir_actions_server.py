import requests
import json

import logging
from odoo import _, api, exceptions, fields, models, modules

# Example of action python code
#
# event_api_url = "http://xxxx:8123/api/events/"
# ha_token = "yyy"
#
# if record:
#   send_ha_event(event_api_url, ha_token, record)

class IrActionsServer(models.Model):

    _inherit = "ir.actions.server"
    
    @api.model
    def _get_eval_context(self, action=None):
        eval_context = super(IrActionsServer, self)._get_eval_context(action)

        def send_ha_event(event_api_url, ha_token, sale_order):
                event_type = "website_sale"
                event_data = json.dumps({
                        "name": sale_order.name,
                        "country": sale_order.partner_id.country_id.display_name,
                        "amount_total": sale_order.amount_total,
                        })
                
                # sale_order.partner_id.country_id.display_name
                #sale_order.amount_total
                headers = {'content-type': 'application/json','Authorization': 'Bearer {}'.format(ha_token)}
                response = requests.post(event_api_url + event_type, headers=headers, data=event_data)

        eval_context["send_ha_event"] = send_ha_event
        return eval_context