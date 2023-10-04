from django.test import TestCase

from catstagram.cats.forms import CatDeleteForm


class DeleteCatFormTests(TestCase):

    def test_cat_delete_form_disabled_fields__expect_all_to_be_disabled(self):
        form = CatDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[CatDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            CatDeleteForm.disabled_attr_name, disabled_fields['name']
        )
