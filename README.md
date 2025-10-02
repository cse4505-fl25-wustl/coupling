# High Coupling Scenarios

This repository contains scenarios for understanding what is high coupling between software modules. For each scenario, determine whether it's high coupling or not. If the coupling is high, consider how the modules can be decoupled.

## Scenario Overview

- [Scenario 1: Config](./scenario_01_config/scenario.md)
- [Scenario 2: Database Access](./scenario_02_database_access/scenario.md)

## Key Questions to Consider

1. Can one module's actions unexpectedly affect another module?
1. Can I test this module in isolation?
1. If I need to switch to a different 3rd party library, will this impact my business logic? 
