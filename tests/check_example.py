import unittest

from examples.simple.blog import app as simple_app


class TestApp(object):
    maxDiff = None

    def setUp(self):
        self.client = self.app.test_client()

    def test_output(self):
        r = self.client.get("/doc")
        self.assertEqual(r.status_code, 200)
        data = r.data.decode('utf-8')
        with open(self.filename) as f:
            expected = f.read()

        self.assertEqual(data, expected)


class TestSimpleApp(TestApp, unittest.TestCase):
    app = simple_app
    filename = "tests/files/simple.html"


if __name__ == "__main__":
    unittest.main()
