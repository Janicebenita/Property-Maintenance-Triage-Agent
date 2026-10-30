"""Triage supplied maintenance reports with explicit safety escalation."""
from __future__ import annotations

EMERGENCY_TERMS = {"fire", "gas leak", "sparking", "collapse", "flooding", "no breathing"}
URGENT_TERMS = {"leak", "electrical", "mold", "sewage", "no heat", "broken lock"}


def triage_request(request: dict) -> dict:
    text = f"{request.get('category', '')} {request.get('description', '')}".lower()
    emergency = sorted(term for term in EMERGENCY_TERMS if term in text)
    urgent = sorted(term for term in URGENT_TERMS if term in text)
    priority = "emergency" if emergency else "urgent" if urgent else "routine"
    route = "local-emergency-procedure" if emergency else "qualified-maintenance-review"
    return {"request_id": request.get("id"), "priority": priority, "route": route, "matched_terms": emergency or urgent, "evidence": {"category": request.get("category"), "description": request.get("description")}, "diagnosis": None, "repair_authorized": False, "human_assessment_required": True}
