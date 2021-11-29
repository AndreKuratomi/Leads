from flask import Blueprint
from app.controllers.app_controllers import create_lead, get_leads, update_lead, delete_lead

bp_lead = Blueprint("leads", __name__, url_prefix="/leads")

bp_lead.post("")(create_lead)
bp_lead.get("")(get_leads)
bp_lead.patch("")(update_lead)
bp_lead.delete("")(delete_lead)
