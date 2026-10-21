# Digital Permit & License Management System
**Module:** Object-Oriented Programming 1 (PROG211)[cite: 1]  
 ---

## 1. Executive Summary
The **Digital Permit & License Management System** is a command-line application engineered to streamline, digitize, and automate government regulatory workflows, such as business operating licenses and building construction permits. Developed as an individual practical assessment for PROG211, this project applies core Object-Oriented Programming (OOP) principles to address a real-world public sector challenge while strictly adhering to **Digital Public Goods (DPG)** standards and global Sustainable Development Goals (SDGs)[cite: 1, 2].

---

## 2. System Architecture & OOP Implementation
The program is built using a modular, two-tier class architecture designed to separate entity management from core registry operations:

* **`CitizenPermit` Class (Task 1 & Task 3):**
  * **Attributes:** Manages core data fields including `permit_number`, `citizen_name`, `national_id`, `permit_type`, and a dictionary tracking clearance stages (`clearance_stages`).
  * **Instance Methods:** 
    * `record_clearance(stage_code, stage_name, status)`: Logs progressive regulatory milestones (e.g., Environmental, Tax, and Municipal checks).
    * `calculate_overall_status()`: Computes aggregate compliance standings (Fully Approved, Under Review, or Rejected).
    * `display_info()`: Outputs a clean individual profile breakdown.
  * **Class Method (`@classmethod`):** `get_total_system_permits()` tracks cumulative system-wide permit issuance across the portal lifecycle.
  * **Static Method (`@staticmethod`):** `validate_status(status)` ensures strict data integrity by vetting status inputs against permitted strings (`APPROVED`, `PENDING`, `REJECTED`).

* **`GovernmentPermitUtility` Class (Task 2):**
  * Acts as the administrative controller storing all registered permit profiles inside an optimized Python dictionary (`self.permit_database`), using unique Permit Numbers as keys for instant $O(1)$ lookups.
  * Features utility functions to add records, search by ID, and render a formatted tabular overview of the government registry.

---

## 3. Alignment with Digital Public Goods (DPG) Standards
This project satisfies all core criteria required for Digital Public Goods recognition:
1. **Open-Source Transparency:** Hosted on GitHub with clear documentation, making the source code freely inspectable, forkable, and improvable by public institutions.
2. **Inclusive and Accessible Design:** Built as a lightweight command-line interface (CLI) with clear text formatting, requiring minimal system resources and no proprietary software dependencies.
3. **Privacy-Respecting:** Designed with data minimization principles—storing only necessary administrative metadata while avoiding the exposure of hyper-sensitive citizen documents.
4. **Modular & Reusable:** Clean separation of concerns between individual permits and aggregate database utilities allows public agencies to easily scale or adapt the code for other municipal applications.

---

## 4. Alignment with Sustainable Development Goals (SDGs)
By digitizing bureaucratic processes, this system directly supports global development targets:
* **SDG 16 (Peace, Justice, and Strong Institutions):** Promotes transparent, accountable, and corruption-free public governance by tracking institutional permit clearances digitally.
* **SDG 8 (Decent Work and Economic Growth):** Simplifies and accelerates business operating license approvals, lowering administrative barriers for entrepreneurs and boosting local commerce.
* **SDG 11 (Sustainable Cities and Communities):** Streamlines municipal zoning reviews and building construction permits to ensure safe, well-regulated urban development.

---

## 5. Project Directory Structure
```text
government_permit_system/
│
├── README.md           # Comprehensive project documentation & DPG alignment report
└── src/
    └── index.py        # Main Python source code file containing classes and CLI menu loop