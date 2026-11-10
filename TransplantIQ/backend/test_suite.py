"""
TransplantIQ Automated Test & Verification Suite
Validates clinical matching, logistics, bioethics, multi-agent orchestration,
Db2 temporal query compatibility, and FastAPI endpoints.
"""

import unittest
import os
import sys

# Ensure backend directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from db import (
    init_db, seed_data, get_stats, get_hospitals, get_hospital,
    query_donors, query_recipients, haversine_distance, query_temporal_state,
    list_requests, update_request_status, get_audit_trail
)
from agents import (
    is_blood_compatible, calculate_hla_score, evaluate_logistics,
    evaluate_bioethics, compute_full_clinical_match, run_agent_pipeline,
    ORGAN_MAX_ISCHEMIA_HOURS
)

class TestTransplantIQ(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize and seed fresh database before running tests."""
        init_db()
        seed_data()

    def test_01_db_stats_and_hospitals(self):
        """Verify database seeding, hospital GIS coordinates, and clinical counts."""
        stats = get_stats()
        self.assertEqual(stats["available_donors"], 20)
        self.assertEqual(stats["waiting_recipients"], 35)
        self.assertEqual(stats["connected_hospitals"], 8)
        self.assertGreater(stats["avg_ischemia_margin_hours"], 0)

        hospitals = get_hospitals()
        self.assertEqual(len(hospitals), 8)
        h1 = hospitals[0]
        self.assertTrue(12.0 <= h1["latitude"] <= 32.0)
        self.assertTrue(72.0 <= h1["longitude"] <= 85.0)

    def test_02_abo_blood_compatibility(self):
        """Verify ABO blood group compatibility matrix."""
        # O- is universal donor
        self.assertTrue(is_blood_compatible("O-", "O-"))
        self.assertTrue(is_blood_compatible("O-", "A+"))
        self.assertTrue(is_blood_compatible("O-", "AB+"))

        # AB+ can only donate to AB+
        self.assertTrue(is_blood_compatible("AB+", "AB+"))
        self.assertFalse(is_blood_compatible("AB+", "O-"))
        self.assertFalse(is_blood_compatible("AB+", "A+"))

        # A+ can donate to A+ and AB+
        self.assertTrue(is_blood_compatible("A+", "A+"))
        self.assertTrue(is_blood_compatible("A+", "AB+"))
        self.assertFalse(is_blood_compatible("A+", "B+"))

    def test_03_hla_matching_logic(self):
        """Verify 5-locus HLA matching and weighted loci scoring."""
        donor = {
            "hla_a": "A*02:01",
            "hla_b": "B*07:02",
            "hla_c": "C*07:02",
            "hla_dr": "DRB1*15:01",
            "hla_dq": "DQB1*06:02"
        }
        recipient_perfect = dict(donor)
        score_100, breakdown_100 = calculate_hla_score(donor, recipient_perfect)
        self.assertEqual(score_100, 100.0)

        recipient_mismatch = {
            "hla_a": "A*01:01",
            "hla_b": "B*08:01",
            "hla_c": "C*07:01",
            "hla_dr": "DRB1*03:01",
            "hla_dq": "DQB1*02:01"
        }
        score_0, _ = calculate_hla_score(donor, recipient_mismatch)
        self.assertEqual(score_0, 0.0)

    def test_04_logistics_and_cold_ischemia(self):
        """Verify geodesic distance calculation and Cold Ischemia Time evaluation."""
        # Chennai (Apollo) to Vellore (CMC): ~115 km
        dist = haversine_distance(13.0617, 80.2508, 12.9246, 79.1348)
        self.assertTrue(110.0 <= dist <= 130.0)

        # Heart: Max ischemia 5.0h
        donor_chennai = {
            "hospital_lat": 13.0617,
            "hospital_lon": 80.2508,
            "organ_type": "heart"
        }
        recip_vellore = {
            "hospital_lat": 12.9246,
            "hospital_lon": 79.1348
        }
        logi_short = evaluate_logistics(donor_chennai, recip_vellore)
        self.assertTrue(logi_short["viable"])
        self.assertIn("Air Ambulance Helicopter", logi_short["transit_mode"])
        self.assertGreater(logi_short["margin_hours"], 2.0)
        self.assertGreater(len(logi_short["waypoints"]), 0)
        self.assertIn("corridor_protocol", logi_short)

        # Long distance heart (Chennai to Chandigarh: ~2100 km)
        recip_chandigarh = {
            "hospital_lat": 30.7644,
            "hospital_lon": 76.7745
        }
        logi_long = evaluate_logistics(donor_chennai, recip_chandigarh)
        self.assertIn("Dedicated Medical Air Charter", logi_long["transit_mode"])

    def test_05_bioethics_agent(self):
        """Verify ethical parity, pediatric priority, and weight ratio check."""
        donor = {"weight_kg": 65.0}
        recip_pediatric = {"pediatric": 1, "weight_kg": 40.0, "waiting_days": 400}
        bio = evaluate_bioethics(donor, recip_pediatric, urgency_score=8)
        self.assertTrue(bio["certified"])
        self.assertGreaterEqual(bio["score"], 90.0)
        self.assertTrue(any("Pediatric" in r for r in bio["reasons"]))

    def test_06_multi_agent_pipeline_execution(self):
        """Verify end-to-end multi-agent execution pipeline."""
        res = run_agent_pipeline(query="Find potential kidney matches")
        self.assertIn("response", res)
        self.assertGreater(len(res["matches"]), 0)
        self.assertGreaterEqual(len(res["agent_steps"]), 5)

        top_match = res["matches"][0]
        self.assertGreater(top_match["score"], 45.0)
        self.assertIn("logistics", top_match)
        self.assertIn("bioethics", top_match)
        self.assertIn("hla_breakdown", top_match)
        self.assertTrue(res["needs_human_approval"])

    def test_07_db2_time_travel_reconstruction(self):
        """Verify IBM Db2 temporal table query simulation (SYSTEM_TIME AS OF)."""
        res = query_temporal_state("2026-11-10T12:00:00Z")
        self.assertIn("as_of", res)
        self.assertEqual(res["active_donors_count"], 20)
        self.assertEqual(res["waiting_recipients_count"], 35)
        self.assertIn("FOR SYSTEM_TIME AS OF", res["db2_query_syntax"])

    def test_08_human_in_the_loop_approval_flow(self):
        """Verify clinical approval updates state and leaves cryptographic audit signature."""
        requests = list_requests()
        self.assertGreater(len(requests), 0)
        req = requests[0]
        req_id = req["request_id"]

        update_request_status(
            request_id=req_id,
            status="APPROVED",
            reviewed_by="Dr. Sarah Chen, MD",
            review_notes="Emergency clinical review completed. Tissue crossmatch negative."
        )

        updated_reqs = list_requests()
        target = next((r for r in updated_reqs if r["request_id"] == req_id), None)
        self.assertIsNotNone(target)
        self.assertEqual(target["status"], "APPROVED")
        self.assertEqual(target["reviewed_by"], "Dr. Sarah Chen, MD")

        # Verify audit trail contains cryptographic log
        audit = get_audit_trail(limit=10)
        self.assertTrue(any(a["action"] == "DECISION_APPROVED" for a in audit))

    def test_09_driver_route_and_zos_audit(self):
        """Verify Driver Route navigation: Start Point (Pickup) to End Point (Dropoff) with Db2 for z/OS audit."""
        from main import api_driver_route, DriverRouteRequest
        res = api_driver_route(DriverRouteRequest(donor_hospital_id=1, recipient_hospital_id=4, organ_type="heart"))
        self.assertIn("start_point", res)
        self.assertIn("end_point", res)
        self.assertEqual(res["start_point"]["type"], "COLLECTION_POINT")
        self.assertEqual(res["end_point"]["type"], "DROPPING_POINT")
        self.assertIn("turn_by_turn", res)
        self.assertGreaterEqual(len(res["turn_by_turn"]), 5)
        self.assertEqual(res["db2_zos_audit"]["zos_subsystem"], "DB2A")
        self.assertEqual(res["db2_zos_audit"]["drda_port"], 446)

if __name__ == "__main__":
    unittest.main()

