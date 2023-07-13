from faker import Faker



class GeneratedData:

    def generate_first_name():
        fake = Faker('ru_RU')
        first_name = fake.first_name()
        return first_name

    def generate_last_name():
        fake = Faker('ru_RU')
        last_name = fake.last_name()
        return last_name

    def generate_delivery_address():
        fake = Faker('ru_RU')
        delivery_address = f"{fake.street_name()} {str(fake.random_int(111, 999))}"
        return delivery_address

    def generate_phone_number():
        fake = Faker()
        phone_number = f"+7{str(fake.random_int(900, 999))}{str(fake.random_int(1111111, 9999999))}"
        return phone_number