from demoqa_tests.model.pages.registration_form import *
from demoqa_tests.utils.app import registration_form, register_new_user
from demoqa_tests.utils.convert import convert


def test_stepobject():
    register_new_user.fill_and_submit()


def test_submit_user_details():

    registration_form.open_browser_and_remove_ads()

    registration_form.set_first_name(kemal.first_name)
    registration_form.set_last_name(kemal.last_name)
    registration_form.set_email(kemal.email)
    registration_form.select_gender(kemal.gender.value)
    registration_form.set_mobile(kemal.mobile)
    registration_form.select_date_of_birth(kemal.birth_year, kemal.birth_month, kemal.birth_day)
    registration_form.click_subjects(kemal.subjects)
    registration_form.select_hobbies(kemal.hobbies)
    registration_form.upload_picture(kemal.picture_file)
    registration_form.set_address(kemal.current_address)
    registration_form.set_state(kemal.state)
    registration_form.set_city(kemal.city)
    registration_form.submit_form()

    registration_form.check_submitted_form(
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
        ]
    )
