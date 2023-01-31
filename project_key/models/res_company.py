# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models


class Company(models.Model):

    _inherit = "res.company"

    def _create_internal_project_task(self):
        """Override to:
        - When a new company is created, a project is created for this company.
        The key sequences to create stories and tasks with keys, created with
        this project, must be linked to the new company to avoid security
        issues.
        """

        # Propagate the new company ID, using the context key, to fill the
        # sequences company.
        self = self.with_context(project_sequence_company=self.id)

        return super(Company, self)._create_internal_project_task()
