from typing import Tuple
from selene import have, command
from selene.support import by
from selene.support.shared import browser
from tests.data import Subject, Hobby, kemal
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import DropDown
from demoqa_tests.model.controls.modal import dialog
from demoqa_tests.utils.convert import convert
from demoqa_tests.utils.path import upload


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def open_browser_and_remove_ads(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads][id*=container]')
        if ads.with_(timeout=5).wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def set_first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)
        return self

    def set_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        browser.all('[for^=gender-radio]').by(have.exact_text(gender)
        ).first.click()
        return self

    def set_mobile(self, mobile: str):
        browser.element('#userNumber').type(mobile)
        return self

    def select_date_of_birth(self, birth_year, birth_month, birth_day):
        self.birthday.select_date(birth_year, birth_month, birth_day)
        return self

    def type_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    def click_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').click().type(subject.value)
            browser.element('[id^="react-select-2"]').click()
        return self

    def select_hobbies(self, values: Tuple[Hobby]):
        for hobby in values:
            path = "//label[contains(.,'" + str(hobby.value) + "')]"
            browser.element(by.xpath(path)).click()
        return self

    def upload_picture(self, picture):
        upload(picture)
        return self

    def set_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    def set_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        DropDown.select(self, browser.element('#state'), value)
        return self

    def set_city(self, value):
        DropDown.select(self, browser.element('#city'), value)
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').press_enter()
        return self

    def check_submitted_form(self, data):
        rows = dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self


class RegisterNewUser:
    def __init__(self):
        self.registration_form = RegistrationForm()

    def fill_and_submit(self):
        (
            self.registration_form.open_browser_and_remove_ads()

            .set_first_name(kemal.first_name)
            .set_last_name(kemal.last_name)
            .set_email(kemal.email)
            .select_gender(kemal.gender.value)
            .set_mobile(kemal.mobile)
            .select_date_of_birth(kemal.birth_year, kemal.birth_month, kemal.birth_day)
            .type_subjects(kemal.subjects)
            .select_hobbies(kemal.hobbies)
            .upload_picture(kemal.picture_file)
            .set_address(kemal.current_address)
            .set_state(kemal.state)
            .set_city(kemal.city)
            .submit_form()

            .check_submitted_form(
                [
                    ('Student Name', f'{kemal.first_name} {kemal.last_name}'),
                    ('Student Email', kemal.email),
                    ('Gender', kemal.gender.value),
                    ('Mobile', kemal.mobile),
                    ('Date of Birth', f'{kemal.birth_day} {kemal.birth_month},{kemal.birth_year}'),
                    ('Subjects', convert(kemal.subjects)),
                    ('Hobbies', convert(kemal.hobbies)),
                    ('Picture', kemal.picture_file),
                    ('Address', kemal.current_address),
                    ('State and City', f'{kemal.state} {kemal.city}')
                ],
            )
        )