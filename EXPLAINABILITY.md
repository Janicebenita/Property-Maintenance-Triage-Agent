# Property Maintenance Triage Agent Explainability

## Decision and Reasoning Process

The agent's decision process classifies the reported issue and applies approved safety and service-priority rules. Its reasoning identifies trigger words, observed symptoms, affected areas, and the basis for routing or escalation.

## Inputs and Data Sources Used

Input data includes occupant reports, authorized property records, photos, sensor readings, and the maintenance priority matrix. Only relevant and authorized data sources are used for triage.

## Outputs and Supporting Evidence

The output contains issue category, suggested priority, safety guidance, routing recommendation, and missing questions. Supporting evidence is tied to the submitted report and applicable priority rule.

## Limits, Constraints, and Known Issues

A key limitation is that remote descriptions and images may omit dangerous conditions. The agent is constrained from diagnosing technical failures, confirming safety, or authorizing repairs without qualified review.

## Uncertainty and Human Review

Uncertainty is emphasized whenever evidence is incomplete or a hazard is possible. Human assessment is required, and emergencies must follow local emergency procedures.

## Implementation in This Repository

`agent.py` implements `triage_request(request)`. It matches the supplied category and description against explicit emergency and urgent term sets, selects emergency/urgent/routine priority, routes emergencies to local emergency procedures, retains the matched terms and original text as evidence, returns no diagnosis, never authorizes repair, and requires human assessment. `test_agent.py` verifies the gas-leak emergency route and repair guardrail.

There is no sensor feed, contractor dispatch, or repair-authorization integration. Diagnosis and dispatch remain with qualified humans.
