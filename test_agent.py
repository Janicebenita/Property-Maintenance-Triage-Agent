import unittest
from agent import triage_request


class TriageTests(unittest.TestCase):
    def test_gas_leak_uses_emergency_route_without_authorizing_repair(self):
        result = triage_request({"description": "Possible gas leak"})
        self.assertEqual(result["priority"], "emergency")
        self.assertFalse(result["repair_authorized"])


if __name__ == "__main__":
    unittest.main()
