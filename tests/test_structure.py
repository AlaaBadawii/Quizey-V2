import importlib.util
import unittest


@unittest.skipUnless(
    importlib.util.find_spec("flask") and importlib.util.find_spec("flask_sqlalchemy"),
    "Flask dependencies are not installed in this environment.",
)
class AppFactoryTests(unittest.TestCase):
    def test_app_factory_registers_expected_blueprints(self):
        from app import create_app

        app = create_app("testing")
        prefixes = {rule.rule for rule in app.url_map.iter_rules()}

        self.assertIn("/health", prefixes)
        self.assertIn("/api/v1/auth/login", prefixes)
        self.assertIn("/api/v1/exams/", prefixes)
        self.assertIn("/api/v1/attempts/", prefixes)
        self.assertIn("/api/v1/grading/", prefixes)


if __name__ == "__main__":
    unittest.main()
