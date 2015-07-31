#! /usr/bin/env python
# coding: utf-8

import unittest

import fuzzyclock

class FuzzyClockTests(unittest.TestCase):

    def test_hours(self):
        self.assertEqual(fuzzyclock.parse_time(00, 00), "meia noite")
        self.assertEqual(fuzzyclock.parse_time(24, 00), "meia noite")

        self.assertEqual(fuzzyclock.parse_time(1, 00), "uma")
        self.assertEqual(fuzzyclock.parse_time(13, 00), "uma")

        self.assertEqual(fuzzyclock.parse_time(2, 00), "duas")
        self.assertEqual(fuzzyclock.parse_time(14, 00), "duas")

        self.assertEqual(fuzzyclock.parse_time(3, 00), "tres")
        self.assertEqual(fuzzyclock.parse_time(15, 00), "tres")

        self.assertEqual(fuzzyclock.parse_time(4, 00), "quatro")
        self.assertEqual(fuzzyclock.parse_time(16, 00), "quatro")

        self.assertEqual(fuzzyclock.parse_time(5, 00), "cinco")
        self.assertEqual(fuzzyclock.parse_time(17, 00), "cinco")

        self.assertEqual(fuzzyclock.parse_time(6, 00), "seis")
        self.assertEqual(fuzzyclock.parse_time(18, 00), "seis")

        self.assertEqual(fuzzyclock.parse_time(7, 00), "sete")
        self.assertEqual(fuzzyclock.parse_time(19, 00), "sete")

        self.assertEqual(fuzzyclock.parse_time(8, 00), "oito")
        self.assertEqual(fuzzyclock.parse_time(20, 00), "oito")

        self.assertEqual(fuzzyclock.parse_time(9, 00), "nove")
        self.assertEqual(fuzzyclock.parse_time(21, 00), "nove")

        self.assertEqual(fuzzyclock.parse_time(10, 00), "dez")
        self.assertEqual(fuzzyclock.parse_time(22, 00), "dez")

        self.assertEqual(fuzzyclock.parse_time(11, 00), "onze")
        self.assertEqual(fuzzyclock.parse_time(23, 00), "onze")

        self.assertEqual(fuzzyclock.parse_time(12, 00), "meio dia")

    def test_minutes(self):
        for minute in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
            if minute == 0:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith(""))
            elif minute == 5:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e cinco"))
            elif minute == 10:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e dez"))
            elif minute == 15:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e quinze"))
            elif minute == 20:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e vinte"))
            elif minute == 25:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e vinte e cinco"))
            elif minute == 30:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e meia"))
            elif minute == 35:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith("e trinta e cinco"))
            elif minute == 40:
                self.assertTrue("vinte para a" in fuzzyclock.parse_time(12, minute))
            elif minute == 45:
                self.assertTrue("quinze para a" in fuzzyclock.parse_time(12, minute))
            elif minute == 50:
                self.assertTrue("dez para a" in fuzzyclock.parse_time(12, minute))
            elif minute == 55:
                self.assertTrue("cinco para a" in fuzzyclock.parse_time(12, minute))
            elif minute == 60:
                self.assertTrue(fuzzyclock.parse_time(12, minute).endswith(""))

    def test_junction(self):
        for hour in [0, 1, 13, 24, 25]:
            self.assertEqual(fuzzyclock.junction(hour).strip(), "a")
        for hour in [12]:
            self.assertEqual(fuzzyclock.junction(hour).strip(), "o")
        for hour in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
            self.assertEqual(fuzzyclock.junction(hour).strip(), "as")

    def test_switch(self):
        self.assertEqual(fuzzyclock.switch(1, [([1], lambda: 1)], 0), 1)
        self.assertNotEqual(fuzzyclock.switch(2, [([1], lambda: 1)], 0), 1)
        self.assertEqual(fuzzyclock.switch(2, [([1], lambda: 1)], 0), 0)


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(FuzzyClockTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
