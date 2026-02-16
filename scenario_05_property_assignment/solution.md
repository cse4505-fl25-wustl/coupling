# Scenario 4: Direct Property Assignment

**Answer: High Coupling**

**Explanation:** If the requirements change—for example, the MatchResult class now requires a timestamp or a referee_id in its constructor—every single piece of code that assigns a result will break.

**Solution:** To lower the coupling, move the assignment inside the Match class.

```python
# match_coordinator.py (Refactored)
def finalize_tournament_match(match, winner_id, scores):
    # The coordinator only knows that a Match can be "recorded".
    # It doesn't care about the 'MatchResult' class at all.
    match.record_result(winner_id, scores['home'], scores['away'])
```

The record_result function of the Match class is the only place where MatchResult gets created. If requirements on MatchResult change, we'll only have one place to update.
