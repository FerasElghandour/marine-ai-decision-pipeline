# Release validation

Source syntax and notebook code cells are checked on Python 3.11 and 3.12 by the included workflow. These source checks do not run training, databases, paid model providers, or external simulations. Additional runtime checks are recorded below when executed.

Full historical experiment reproduction is separate from source validation. No new benchmark result is inferred from syntax checks.

## Complete notebook execution

After removing train/test leakage, the baseline overall MAE is 1.5615 rings and augmented MAE is 1.5726. Old-class MAE changes from 5.1377 to 4.9848. Augmentation improves the older subgroup by about 3.0% while slightly worsening overall MAE; the result is a trade-off rather than an overall win.

All 10 code cells executed successfully in an isolated CPU process. No model-provider calls were made. Source/input hashes and dependency versions are recorded in `results/reproduction.json`. The raw inputs and raw execution logs are not distributed.
