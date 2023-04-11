import unittest
import main_tests


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(main_tests.TestLoginRegister))
    suite.addTests(loader.loadTestsFromTestCase(main_tests.TestFindGifts))
    suite.addTests(loader.loadTestsFromTestCase(main_tests.TestGen))

    unittest.TextTestRunner().run(suite)
