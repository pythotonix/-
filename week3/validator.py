''' validator classes '''
import re
class Validator:
    def validate_name_surname(self, name_surname: str):
        ''' ckecking name and surname '''
        return bool(re.match(r'^[A-Z][a-z]{2,19} [A-Z][a-z]{2,19}$', name_surname))

    def validate_age(self, age: str):
        ''' 16 - 99 '''
        return bool(re.match(r'^1[6-9]|[2-9]\d$', age))
    def validate_country(self, country: str):
        ''' if country is writen correct'''
        return bool(re.match(r'^[A-Z][a-z]{1,9}$|^[A-Z]{3}$', country))
    def validate_region(self, region: str):
        ''' if region is writen correct'''
        return bool(re.match(r'^[A-Z][a-z0-9]{2,}$', region))
    def validate_living_place(self, living_place: str):
        ''' if place of living is writen correct'''
        return bool(re.match(r'^[A-Z][a-z]{2,19} (st\.|av\.|prosp\.|rd\.) \d[a-z0-9]$', living_place))
    def validate_index(self, index: str):
        ''' if index is writen correct'''
        return bool(re.match(r'^\d{5}$', index))
    def validate_phone(self, phone: str):
        ''' if phone number is writen correct'''
        return bool(re.match(r'^\+\d{9,12}$|^\+\d{2} \(\d{3}\) \d{3}-\d{2}-\d{2}$', phone))
    def validate_email(self, email: str):
        ''' if email adress is writen correct'''
        exp = r"^(?!.*\.{2,})(?!\.)[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~.-]{1,64}(?<!\.)@"
        exp += r"[a-z.]{1,255}\.(com|org|edu|gov|net|ua)$"
        return bool(re.match(exp, email))
    def validate_id(self, id_str):
        ''' if id is writen correct'''
        return bool(re.match(r'^\d{6}$', id_str) and id_str.count('0') == 1)

    def validate(self, data: str):
        ''' if all information is writen correct'''
        parts = re.split(r'[;,]', data.strip())
        return all((
            self.validate_name_surname(parts[0].strip()),
            self.validate_age(parts[1].strip()),
            self.validate_country(parts[2].strip()),
            self.validate_region(parts[3].strip()),
            self.validate_living_place(parts[4].strip()),
            self.validate_index(parts[5].strip()),
            self.validate_phone(parts[6].strip()),
            self.validate_email(parts[7].strip()),
            self.validate_id(parts[8].strip())
        ))
