import odoo
import odoo.tests


@odoo.tests.common.tagged('post_install', '-at_install')
class TestSnippets(odoo.tests.HttpCase):

    def test_01_donation(self):
        self.start_tour("/?enable_editor=1", "donation_snippet_edition", login='admin')
