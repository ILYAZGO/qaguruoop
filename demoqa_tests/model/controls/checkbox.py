from selene import have


class Checkbox:
    def select_checkbox(self, elements, *options: str):
        for option in options:
            elements.by(have.exact_text(option)).first.element('..').click()
        return self