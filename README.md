# Reduced-Order-Wake-Modelling-tool

## Overview

This repository contains the reduced-order wake modelling workflow developed as part of an Advanced Research Project investigating wake-resolved fatigue loading predictions for large offshore wind turbines.

The workflow combines engineering wake models, stochastic turbulence generation and aeroelastic load analysis to evaluate the conservatism of the IEC 61400-1 effective turbulence intensity approach when compared with wake-resolved inflow representations.

The methodology integrates:

* PyWake engineering wake models
* TurbSim stochastic inflow generation
* OpenFAST aeroelastic simulations
* Post-processing routines for fatigue and Damage Equivalent Load (DEL) assessment

The work was developed using the IEA 15 MW Monopole reference turbine and validated against reference LES datasets.

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
* Farm array configuration
* Representative TurbSim input file
* Representative OpenFAST input files

These datasets correspond directly to the cases presented within the report.

---

## Wake Resolving Modelling Tool

A generalised version of the wake-resolving modelling tool developed during this project is provided. The workflow combines PyWake, TurbSim and OpenFAST to generate wake-resolved inflow fields and evaluate the resulting turbine loads and fatigue behaviour.

Users may adapt the framework to alternative turbines, wind farm layouts, wake models and operating conditions. To ensure compatibility, any new inputs should follow the same directory structure and file conventions used throughout the provided examples.

---

## Simulation Inputs

The simulations use the same inflow definitions, turbine configuration and modelling assumptions described in the accompanying paper.

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

Wake deficit modelling is based on implementations available through the PyWake framework:

https://gitlab.windenergy.dtu.dk/TOPFARM/PyWake/-/blob/40424ed292d8678d3c6eaeca7bc59cf73ddb8965/docs/notebooks/WakeDeficitModels.ipynb

Models considered include:

* Bastankhah–Porté-Agel Gaussian Wake Model
* Niayifar–Porté-Agel Wake Model 
* TurbOPark Wake Model

---

## Turbulence Models

Wake-added turbulence representations are based on implementations available through the PyWake framework:

https://gitlab.windenergy.dtu.dk/TOPFARM/PyWake/-/blob/40424ed292d8678d3c6eaeca7bc59cf73ddb8965/docs/notebooks/TurbulenceModels.ipynb

Models considered include:

* Crespo–Hernández Wake Added Turbulence Model

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
https://github.com/IEAWindSystems/IEA-15-240-RWT.git

Representative files are provided to present the inputs used for the main OpenFAST simulations. This specifically includes the Elastodyn, InflowWind and main fst file. The other OpenFAST modules are kept as default from the original IEA-15 Monopole reference turbine definiton. 

### TurbSim

TurbSim is used for stochastic turbulent inflow generation.

Documentation:

https://openfast.readthedocs.io

A Representative file is provided to present the inputs used for each TurbSim simulation.
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
