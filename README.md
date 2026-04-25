# StreamMaster Cost Estimator
A Python-based Graphical User Interface (GUI) application designed to help users calculate and manage their monthly streaming service expenses based on tiers, profiles, and optional add-ons.

# Features
- Tier-Based Selection: Choose between Basic, Standard, and Premium subscription levels.
- Dynamic Calculation: Automatically calculates costs based on the number of profiles and selected services.
- Add-on Services: Support for 4K Streaming, Offline Downloads, and Extra Device Logins.
- Input Validation: Error handling for invalid profile counts or negative tax rates.
- Budget Alerts: Automated warning system if the estimated total exceeds RM500.
- Summary Reports: Generates a detailed breakdown including Base Cost, Add-on totals, and Applied Taxes.

# Logic & Formula
The application calculates the final cost using the following business logic:

    Total Cost = [(Tier Price × Profiles) + Add-ons] × (1 + Tax Rate)

# Technical Details
- Language: Python 3.x
- Library: tkinter (Standard Python GUI library)
- UI Components: - LabelFrame for organized sections.
  - Radiobutton for exclusive tier selection.
  - Checkbutton for multiple add-on selections.
  - Toplevel for generating the summary report window.
