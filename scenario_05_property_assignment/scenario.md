# Scenario 5: Direct Property Assignment

Consider a sports tournament management system. When a match concludes, a coordinator script is responsible for recording the final outcome.

Instead of telling the Match to finalize itself, the script reaches in and manually constructs the internal state of the Match.

```python
# match_coordinator.py
def finalize_tournament_match(match, winner_id, scores):
    # High coupling: The coordinator must know exactly how to 
    # instantiate a 'MatchResult' object and what fields it requires.
    match.outcome = MatchResult(
        winner_id=winner_id,
        home_score=scores['home'],
        away_score=scores['away'],
        overtime=False
    )
    print(f"Match {match.id} finalized.")
```
Because the coordinator is "micromanaging" the assignment, it becomes dependent on the internal structure of the MatchResult class.

**Question:** Does this create high coupling?
