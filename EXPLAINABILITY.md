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

This repository implements the worker as a declarative OpenGAP package. `agent.yaml` specifies maintenance-report inputs and a review-oriented triage output, `SOUL.md` defines emergency and human-approval constraints, and this file documents the evidence and uncertainty model; `README.md` supplies usage context.

There is no sensor feed, contractor dispatch, or repair-authorization integration in the repository. A compatible host must expose uncertainty and possible hazards, direct emergencies to local procedures, and leave diagnosis and dispatch to qualified humans.
