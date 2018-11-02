from ..field import Field, stere_performer, use_after, use_before


@stere_performer('click', consumes_arg=False)
class Button(Field):
    """Convenience Class on top of Field, it implements `click()` as its performer.
    """
    @use_after
    @use_before
    def click(self):
        """Uses Appium's click method.

        Example:

        >>> purchase = Button('id', 'buy_button')
        >>> purchase.click()

        """
        self.find().click()