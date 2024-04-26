import unittest
from unittest import TestCase
from rock_band import Musician, MusicBand, RestrictedMixin, UkrainianMusicBand


class TestMusician(TestCase):
    """TestMusician"""
    def setUp(self):
        self.musician1 = Musician("Ruslana", "Ukraine", ["vocal", "drum", "guitare"])
        self.musician2 = Musician("Kobzon", "Russia", ["vocal", "drum", "guitare"])
        self.musician3 = Musician("Joe Newman", "England", ["vocal"])
        self.musician4 = Musician("Thom Sonny Green", "England", ["vocal", "guitare"])
        self.musician5 = Musician("Gus Unger-Hamilton", "England", ["vocal", "drum"])

    def test_invalid_musican_initializing(self):
        with self.assertRaises(ValueError) as assert_error:
            Musician("A", "B", [])
        self.assertEqual(
            assert_error.exception.args[0], "The musician must have at least one musical instrument")

    def test_musican_initializing(self):

        self.assertEqual(
            (self.musician1.name), "Ruslana", "Неправильнt імя музичного гурту!")
        self.assertEqual(
            (self.musician2.residency), "Russia", "Неправильна крвїна музиканта!")
        self.assertEqual(
            (self.musician3.music_instrument), ["vocal"], "Неправильна кількість пелюсток!")

    def test_musican_str(self):

        self.assertEqual(
            (str(self.musician3)
             ), "Joe Newman plays only one musical instrument. This instrument is vocal.", "Хибний метод str")
        self.assertEqual(
            (str(self.musician5)
             ), "Gus Unger-Hamilton plays following musical instruments: vocal, drum.", "Хибний метод str")

    def test_musican_repr(self):
        # Joe Newman
        self.assertEqual(
            (str([self.musician3, self.musician5])
             ), "[Joe Newman (England), Gus Unger-Hamilton (England)]", "Хибний метод repr")

    def test_add_special_method(self):
        self.assertEqual(
            (self.musician1 + self.musician2
             ), "Collaboration with Russians is unavailable", "Хибний метод add")
        self.assertEqual(
            (self.musician1 + self.musician3).name, "RuslanaNewman", "Хибний метод add")
        self.assertIsInstance(
            self.musician1 + self.musician5, MusicBand, "Не створюється гурт з двох музикантів!")


class TestMusicBand(TestCase):
    """ TestMusicBand"""
    def setUp(self):
        self.musician1 = Musician("Ruslana", "Ukraine", ["vocal", "drum", "guitare"])
        self.musician2 = Musician("Kobzon", "Russia", ["vocal", "drum", "guitare"])
        self.musician3 = Musician("Joe Newman", "England", ["vocal"])
        self.musician4 = Musician("Thom Sonny Green", "England", ["vocal", "guitare"])
        self.musician5 = Musician("Gus Unger-Hamilton", "England", ["vocal", "drum"])
        self.musician6 = Musician("Yurii Kaplan", "Ukraine", ["vocal", "guitare"])
        self.musician7 = Musician("Stanislav Murashko", "Ukraine", ["guitare"])
        self.musician8 = Musician("Konstantin Pyzhov", "Ukraine", ["piano", "guitare"])

        self.band1 = MusicBand(
            "Alt-j", [self.musician4, self.musician3, self.musician5], 2017, ["First Album", "Second Album"])
        self.band2 = MusicBand(
            "Alt-jCopy", [self.musician1, self.musician4, self.musician3, self.musician5], 2024, ["First Album", "Second Album"])
        self.band3 = MusicBand(
            "UnknownMachine", [self.musician3, self.musician2], 2020, ["First Album", "Second Album"])
        self.ukr_band1 = UkrainianMusicBand(
            "Valentin Strykalo", [self.musician6, self.musician7, self.musician8], 2010, ["First Album", "Second Album"])
        self.restricted_countries = ["Russia"]
        self.restricted_atrists = ["Grigory Leps", "Irina Dubtsova", "Mikhail Boyarskiy"]

    def test_invalid_music_band_initializing(self):
        with self.assertRaises(ValueError) as assert_error:
            MusicBand("A", ["Bob"], 2024, ["Bob", "ImBob"])
        self.assertEqual(
            assert_error.exception.args[0], "Band should consist of more than 1 member!")

    def test_music_band_initializing(self):
        self.assertEqual(
            (self.band1.name), "Alt-j", "Неправильнt імя музичного гурту!")
        self.assertEqual(
            (len(self.band1.members)), 3, "Неправильна кількість музикантів!")
        self.assertEqual(
            (self.band1.foundation_year), 2017, "Неправильний рік заснування!")

    def test_music_band_member_property(self):
        self.band2.members = self.musician7
        self.assertEqual(
            (len(self.band2.members)), 5, "Хибно працює members property!")
        self.band2.members = self.musician1
        self.assertEqual(
            (len(self.band2.members)), 5, "Хибно працює members property!")
        del self.band2.members
        self.assertEqual(
            (len(self.band2.members)), 0, "Хибно працює members deleter!")

    def test_music_band_hash_method(self):
        set_1 = set()
        self.assertTrue(self.band1 not in set_1)
        set_1.add(self.band1)
        self.assertTrue(self.band1 in set_1)

    def test_music_band_str(self):
        self.assertEqual(
            (str(self.band1)
             ), "The musical band 'Alt-j' was founded in 2017 and has 3 members.", "Хибний метод str")
        self.assertEqual(
            (str(self.band2)
             ), "The musical band 'Alt-jCopy' was founded in 2024 and has 4 members.", "Хибний метод str")

    def test_music_band_repr(self):
        self.assertEqual((str([self.band1, self.band2])), "[Alt-j, Alt-jCopy]", "Хибний метод repr")

    def test_music_band_le(self):
        self.assertEqual((self.band2 <= self.band1), True, "Хибне порівняння віку")
        self.assertFalse(self.band1 <= self.band2)

    def test_music_band_touring(self):
        touring_dates = {'Warsaw': '15.03.2024', 'London': '12.04.2024'}
        self.assertEqual((self.band2.touiring(touring_dates)), "We will make a tour to: Warsaw(15.03.2024), London(12.04.2024)", "Хибний static method")

    def test_music_band_collaboration(self):
        touring_dates = {'Warsaw': '15.03.2024', 'London': '12.04.2024'}
        self.assertEqual(
            (self.band1.collaboration(self.band2, touring_dates)), "We 'Alt-j' and 'Alt-jCopy' announce a joint tour!\n\
We will make a tour to: Warsaw(15.03.2024), London(12.04.2024)", "Хибно утворена колаборація")


class TestUkrainianMusicBand(TestCase):
    """TestUkrainianMusicBand"""
    def setUp(self):
        self.musician1 = Musician("Ruslana", "Ukraine", ["vocal", "drum", "guitare"])
        self.musician2 = Musician("Kobzon", "Russia", ["vocal", "drum", "guitare"])
        self.musician3 = Musician("Joe Newman", "England", ["vocal"])
        self.musician4 = Musician("Thom Sonny Green", "England", ["vocal", "guitare"])
        self.musician5 = Musician("Gus Unger-Hamilton", "England", ["vocal", "drum"])
        self.musician6 = Musician("Yurii Kaplan", "Ukraine", ["vocal", "guitare"])
        self.musician7 = Musician("Stanislav Murashko", "Ukraine", ["guitare"])
        self.musician8 = Musician("Konstantin Pyzhov", "Ukraine", ["piano", "guitare"])

        self.band1 = MusicBand(
            "Alt-j", [self.musician4, self.musician3, self.musician5
                      ], 2017, ["First Album", "Second Album"])
        self.band2 = MusicBand(
            "Alt-jCopy", [self.musician1, self.musician4, self.musician3, self.musician5
                          ], 2024, ["First Album", "Second Album"])
        self.band3 = MusicBand(
            "UnknownMachine", [self.musician3, self.musician2
                               ], 2020, ["First Album", "Second Album"])
        self.ukr_band1 = UkrainianMusicBand(
            "Valentin Strykalo", [self.musician6, self.musician7, self.musician8
                                  ], 2010, ["First Album", "Second Album"])
        self.restricted_countries = ["Russia"]
        self.restricted_atrists = ["Grigory Leps", "Irina Dubtsova", "Mikhail Boyarskiy"]

    def test_ukr_music_band_initializing(self):

        self.assertEqual(
            (self.ukr_band1.name), "Valentin Strykalo", "Неправильнt імя музичного гурту!")
        self.assertEqual(
            (len(self.ukr_band1.members)), 3, "Неправильна кількість музикантів!")
        self.assertEqual(
            (self.ukr_band1.foundation_year), 2010, "Неправильний рік заснування!")
        self.assertEqual(
            (len(self.ukr_band1.albums)), 2, "Неправильна кількість пісень в альбомі!")

    def test_restricted_countries(self):
        UkrainianMusicBand.set_restricted_countries(self.restricted_countries)
        self.assertEqual(
            (UkrainianMusicBand.restricted_countries), ["Russia"], "Неправильний список \
заборонених країн!")
        UkrainianMusicBand.add_restricted_country("Belarus")
        self.assertEqual(
            (UkrainianMusicBand.restricted_countries), ["Russia", "Belarus"], "Неправильний \
список заборонених країн!")

    def test_restricted_artist(self):
        UkrainianMusicBand.set_restricted_artists(self.restricted_atrists)
        self.assertEqual(
            (UkrainianMusicBand.restricted_artists
             ), ["Grigory Leps", "Irina Dubtsova", "Mikhail Boyarskiy"], "Неправильний \
список заборонених країн!")
        UkrainianMusicBand.add_restricted_artist("Basta")
        self.assertEqual(
            (len(UkrainianMusicBand.restricted_artists)), 4, "Неправильний \
список заборонених країн!")

    def test_ukr_music_band_member_property(self):
        self.ukr_band1.members = self.musician1
        self.assertEqual(
            (len(self.band2.members)), 4, "Хибно працює members property!")
        self.ukr_band1.members = self.musician1
        self.assertEqual(
            (len(self.band2.members)), 4, "Хибно працює members property!")

    def test_ukr_music_band_collaboration(self):
        UkrainianMusicBand.set_restricted_countries(self.restricted_countries)
        self.assertEqual(
            (UkrainianMusicBand.restricted_countries), ["Russia"], "Неправильний \
список заборонених країн!")
        touring_dates = {'Warsaw': '15.03.2024', 'London': '12.04.2024'}
        self.assertEqual(
            (self.ukr_band1.collaboration(self.band3, touring_dates)
             ), "We cannot cooperate because of ties with Russia", "Хибно сформована колаборація")
        self.assertEqual(
            (self.ukr_band1.collaboration(self.band1, touring_dates)), "We \
'Valentin Strykalo' and 'Alt-j' announce a joint tour!\nWe will make a \
tour to: Warsaw(15.03.2024), London(12.04.2024)", "Хибно сформована колаборація")

    def test_urk_band_isinstance(self):
        self.assertIsInstance(self.ukr_band1, UkrainianMusicBand)
        self.assertIsInstance(self.ukr_band1, MusicBand)
        self.assertIsInstance(self.ukr_band1, RestrictedMixin)


if __name__ == '__main__':
    unittest.main(verbosity=2)
