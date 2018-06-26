from odoo import models, fields, api


class MrpEco(models.Model):
    _inherit = "mrp.eco"

    interpod_project = fields.Many2one(
        'project.project',
        string="Project",
        required=False,
        translate=False,
    )

    is_product_all = fields.Boolean(
        'Applies to All Pod Types',
        compute='_is_product_all',
        inverse='_set_product',
    )
    interpod_linked_documents = fields.Char(
        'Linked Documents', required=False, translate=False)
    interpod_stage_id_tracking = fields.Many2one(
        'mrp.eco.stage', string="Stage", required=False, translate=False)

    interpod_upload_redline_markup = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string='Upload Redline Mark-Up',
        required=False,
        translate=False)
    interpod_update_routing = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Routing",
        required=False,
        translate=False)
    interpod_update_qc_docs = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update QC Docs",
        required=False,
        translate=False,
        help="Update QC documentation, including QC inspections,"
        " QC Checkpoints, and ITP's")
    interpod_update_model = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Drawings / Model",
        required=False,
        translate=False)
    interpod_update_machine_files = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Update Machine Files",
        help="Update Machine Files",
        required=False,
        translate=False)
    interpod_update_bom = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ], string="Update BoM", required=False, translate=False)
    interpod_testing_and_validation = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Testing and Validation",
        required=False,
        translate=False)
    interpod_supplier_update = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Supplier Update", required=False, translate=False)
    interpod_quarantine_parts = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Quarantine Parts",
        required=False, translate=False)
    interpod_project_manager_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Project Manager Approval",
        required=False,
        translate=False)
    interpod_production_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Production Approval",
        required=False,
        translate=False)
    interpod_customer_approval = fields.Selection(
        [
            ('required', 'Required'),
            ('not required', 'Not Required'),
            ('complete', 'Complete'),
        ],
        string="Customer Approval",
        required=False,
        translate=False)

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
        ondelete='cascade', required=False)
