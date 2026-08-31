# Collaboration state

Use this compact internal record when work spans several decisions or turns. Do not expose it unless the user asks.

```yaml
work:
  requested_artifact: ""
  medium: ""
  purpose: ""
  audience_or_receiver: ""
truth:
  supplied: []
  supported_inference: []
  unknown: []
  forbidden_invention: []
authorship:
  locked: []
  open_decision: ""
  explicitly_delegated: []
craft:
  decision_gap: ""
  operations_in_use: []
  evidence_needed: ""
local_history:
  selected: []
  rejected: []
  reason_for_rejection: []
next:
  consequential_user_decision: ""
  automatic_work_after_decision: []
```

## Scope discipline

- `local_history` belongs only to the current work.
- A collaborator preference may be reused only when it is explicitly stated as general or independently supported across unrelated work.
- Core craft changes require evidence beyond one collaborator and one development case.
- When context is compressed or handed off, preserve locked decisions, open decision, truth boundaries, and local rejections before descriptive history.

The record prevents forgotten decisions; it is not a form the user must complete and not a fixed production pipeline.
