# Reduced-Order-Wake-Modelling-tool

# Reduced-Order Wake Modelling Tool

## Overview

This repository contains the reduced-order wake modelling workflow developed as part of an Advanced Research Project investigating wake-resolved fatigue loading predictions for large offshore wind turbines.

The workflow combines engineering wake models, stochastic turbulence generation and aeroelastic load analysis to evaluate the conservatism of the IEC 61400-1 effective turbulence intensity approach when compared with wake-resolved inflow representations.

The methodology integrates:

* PyWake engineering wake models
* TurbSim stochastic inflow generation
* OpenFAST aeroelastic simulations
* Post-processing routines for fatigue and Damage Equivalent Load (DEL) assessment

The work was developed using the IEA 15 MW reference turbine and validated against reference LES datasets.

---

## Repository Structure

```text
├── WakeDeficitModels.ipynb
├── TurbulenceModels.ipynb
├── wake_field_generation/
├── post_processing/
├── figures/
├── report_data/
├── examples/
└── README.md
```

---

## Included Data

The repository contains the processed datasets used to generate the figures and fatigue comparisons presented within the final report.

Included files contain:

* Rotor-averaged velocity data
* Rotor-averaged turbulence intensity data
* Wake model comparison datasets
* Damage Equivalent Load (DEL) results
* Figure generation scripts
* Representative flowfield outputs used for visualisation

These datasets correspond directly to the cases presented within the report.

---

## Simulation Inputs

The simulations use the same inflow definitions, turbine configuration and modelling assumptions described in the accompanying report.

These include:

* IEA 15 MW Reference Wind Turbine
* IEC Normal Turbulence Model (NTM)
* IEC Effective Turbulence Intensity (Ieff)
* Wake-resolved inflows generated using engineering wake models
* TurbSim-generated turbulent velocity fields
* OpenFAST aeroelastic response calculations

For complete modelling assumptions and parameter values, refer to the project report.

---

## Engineering Wake Models

Wake deficit modelling is based on implementations available through the PyWake framework.

Models considered include:

* Bastankhah–Porté-Agel Gaussian Wake Model (BPA)
* Niayifar–Porté-Agel Wake Model (NPA)
* TurbOPark Wake Model

---

## Turbulence Models

Wake-added turbulence representations are based on implementations available through the PyWake framework.

Models considered include:

* Crespo–Hernández Wake Added Turbulence Model
* IEC Effective Turbulence Intensity (Ieff)
* Additional turbulence formulations available through PyWake

---

## External Dependencies

This work makes use of several established open-source research tools:

### PyWake

PyWake provides the engineering wake and turbulence model implementations used throughout this work.

Repository:

https://github.com/DTUWindEnergy/PyWake

### OpenFAST

NREL OpenFAST is used for aeroelastic load prediction.

Repository:

https://github.com/OpenFAST/openfast

### TurbSim

TurbSim is used for stochastic turbulent inflow generation.

Documentation:

https://openfast.readthedocs.io

---

## Attribution

The wake deficit and wake-added turbulence model implementations contained within the referenced notebooks originate from the PyWake project and remain the intellectual property of their respective authors and contributors.

This repository primarily documents the workflow developed to:

1. Construct wake-resolved inflow fields.
2. Superimpose wake deficits onto turbulent velocity fields.
3. Generate OpenFAST-compatible inflow conditions.
4. Evaluate fatigue loading and DEL predictions.
5. Compare engineering wake models against LES-informed reference cases.

---

## Citation

If using this repository, please cite:

Ahmed Noor Danayal,
"Assessment of Wake-Resolved Inflow Modelling for Fatigue Prediction in Large Offshore Wind Turbines",
University of Manchester, Advanced Research Project, 2026.
