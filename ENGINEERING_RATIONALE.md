# Engineering Rationale

**Feras Elghandour**

## Objective

Integrate ring-count prediction, subgroup-focused generative augmentation, and inspectable decision rules in one experimental pipeline. This is an analysis prototype, not a validated conservation policy.

## Evidence and trade-offs

After fitting preprocessing and the augmentation model only on training data, baseline overall MAE is 1.5615 rings versus 1.5726 after augmentation. The older subgroup changes from 5.1377 to 4.9848 MAE. The subgroup benefit is modest and comes with a small overall regression; there is no basis to claim that augmentation improves every outcome.

## Design choices

- A random forest provides an interpretable tabular baseline and exposes tree-level variation.
- A VAE explores targeted feature generation for the smaller older-specimen group. Its heuristic synthetic labels are a limitation, not ground truth.
- Explicit decision rules and event traces make each illustrated decision inspectable. The disagreement score is uncalibrated, and the event list is in memory.

## Next validation

Repeat the study across independent splits and seeds, compare simpler resampling baselines, assess joint feature/label consistency, calibrate uncertainty, and define domain-reviewed decision costs before any operational use. The existing test partition should not become a repeated tuning target.
