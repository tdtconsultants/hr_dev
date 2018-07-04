from odoo import models, fields, api


class MrpEcoChecklistTemplate(models.Model):
    _name = 'mrp.eco.interpod_checklist.template'

    name = fields.Char('Name', required=True)
    help = fields.Char('Help')
    is_mandatory = fields.Boolean('Mandatory', required=True)

class MrpEcoChecklist(models.Model):
    _name = 'mrp.eco.interpod_checklist'

    eco_id = fields.Many2one(
        'mrp.eco',
        string='ECO',
        ondelete='cascade',
    )
    name = fields.Char('Name', required=True)
    help = fields.Char('Help')
    is_mandatory = fields.Boolean('Mandatory', required=True)
    is_approved = fields.Boolean(compute='_compute_is_approved')
    status = fields.Boolean('Status', required=True)

    @api.one
    @api.depends('status', 'is_mandatory')
    def _compute_is_approved(self):
        return not self.is_mandatory or self.status

class MrpEco(models.Model):
    _inherit = "mrp.eco"

    def _fill_checklist(self):
        return [(0, None, {
            'name': t.name,
            'is_mandatory': t.is_mandatory,
            'help': t.help,
        }) for t in self.env['mrp.eco.interpod_checklist.template'].search([])]

    interpod_checklist_ids = fields.One2many(
        'mrp.eco.interpod_checklist',
        'eco_id',
        string="Checklist",
        default=_fill_checklist,
    )
    interpod_project = fields.Many2one(
        'project.project',
        string="Project",
    )

    is_product_all = fields.Boolean(
        'Applies to All Pod Types',
        compute='_is_product_all',
        inverse='_set_product',
    )
    interpod_linked_documents = fields.Char(
        'Linked Documents')
    interpod_stage_id_tracking = fields.Many2one(
        'mrp.eco.stage', string="Stage")

    # XXX Following fields are legacy and will soon be removed
    interpod_upload_redline_markup = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string='Upload Redline Mark-Up',
    )
    interpod_update_routing = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Routing",
    )
    interpod_update_qc_docs = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update QC Docs",
        help="Update QC documentation, including QC inspections,"
        " QC Checkpoints, and ITP's")
    interpod_update_model = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Drawings / Model",
    )
    interpod_update_machine_files = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Machine Files",
        help="Update Machine Files",
    )
    interpod_update_bom = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ], string="Update BoM")
    interpod_testing_and_validation = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Testing and Validation",
    )
    interpod_supplier_update = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Supplier Update")
    interpod_quarantine_parts = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Quarantine Parts",
        )
    interpod_project_manager_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Project Manager Approval",
    )
    interpod_production_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Production Approval",
    )
    interpod_customer_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Customer Approval",
    )

    @api.depends('product_tmpl_id')
    @api.onchange('product_tmpl_id')
    def _is_product_all(self):
        """Set is_product_all from product_tmpl_id"""
        product_all_id = self.env.ref('interpod_eco_attributes.product_all_pods').id
        self.is_product_all = self.product_tmpl_id.id == product_all_id

    @api.onchange('is_product_all')
    def _set_product(self):
        """Set product_tmpl_id from is_product_all"""
        product_all_id = self.env.ref('interpod_eco_attributes.product_all_pods').id
        if self.is_product_all:
            self.product_tmpl_id = product_all_id
        elif self.product_tmpl_id.id == product_all_id:
            self.product_tmpl_id = None

class MrpEcoApproval(models.Model):
    _inherit = "mrp.eco.approval"

    approval_template_id = fields.Many2one(
        'mrp.eco.approval.template', 'Template',
        ondelete='cascade')
