from unittest import skip
from .base import FunctionalTest
    
class ItemValidataionTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edit goes to the home page and accidendtally tries to submit
        # an empty list item, She hits Enter on the empty input box
        
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second balnk list item
        
        # She receives a similar warning on the list page

        # And she can correct it by fillign some text in
        self.fail('write me!')
        

