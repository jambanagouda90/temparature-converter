import io
import unittest
from unittest.mock import patch

# Import functions from your script (replace 'converter' with your filename)
from converter import (
    celsius_to_fahrenheit,
    convert,
    fahrenheit_to_celsius,
    validate_celsius,
)


class TestTemperatureConverter(unittest.TestCase):

    def test_validate_celsius_valid(self):
        self.assertEqual(validate_celsius(0), 0)
        self.assertEqual(validate_celsius(-273.15), -273.15)
        self.assertEqual(validate_celsius(100), 100)

    def test_validate_celsius_below_absolute_zero(self):
        with self.assertRaises(ValueError) as ctx:
            validate_celsius(-273.16)
        self.assertEqual(str(ctx.exception), "Temperature cannot be below absolute zero")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
        self.assertEqual(celsius_to_fahrenheit(-273.15), -459.67)

    def test_celsius_to_fahrenheit_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(-300)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertEqual(fahrenheit_to_celsius(-40), -40.0)
        self.assertEqual(fahrenheit_to_celsius(98.6), 37.0)
        self.assertEqual(fahrenheit_to_celsius(-459.67), -273.15)

    def test_fahrenheit_to_celsius_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(-500)

    def test_convert_choice_1(self):
        self.assertEqual(convert(25, 1), (77.0, "°F"))

    def test_convert_choice_2(self):
        self.assertEqual(convert(77, 2), (25.0, "°C"))

    def test_convert_invalid_choice(self):
        with self.assertRaises(ValueError) as ctx:
            convert(10, 3)
        self.assertEqual(str(ctx.exception), "Invalid choice")

    @patch("builtins.input", side_effect=["1", "25"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_main_flow(self, mock_stdout, mock_input):
        import runpy
        runpy.run_module("converter", run_name="__main__")
        output = mock_stdout.getvalue()
        self.assertIn("Converted Temperature: 77.0 °F", output)


if __name__ == "__main__":
    unittest.main()
