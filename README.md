# Digital Permit & License Management System
**Module:** Object-Oriented Programming 1 (PROG211)  
---

## 1. Executive Summary
The **Digital Permit & License Management System** is a command-line application engineered to streamline, digitize, and automate government regulatory workflows, such as business operating licenses and building construction permits. Developed as an individual practical assessment for PROG211, this project applies core Object-Oriented Programming (OOP) principles to address a real-world public sector challenge while strictly adhering to **Digital Public Goods (DPG)** standards and global Sustainable Development Goals (SDGs).

---

## 2. System Architecture & Modular Design
To reflect professional software engineering standards, the system has been decomposed from a monolithic script into a clean, multi-tier modular architecture. This separation of concerns ensures high maintainability, reusability, and scalability:

- **`models/` (Entity Layer):** 
  - Host the core **`CitizenPermit`** class, managing data attributes (`permit_number`, `citizen_name`, `national_id`, `permit_type`, and `clearance_stages`).
  - Implements instance methods (`record_clearance`, `calculate_overall_status`, `display_info`), class methods (`@classmethod` for system-wide tracking via `get_total_system_permits()`), and static validation methods (`@staticmethod` for status vetting).

- **`database/` (Data Persistence Layer):**
  - Houses the **`MockDatabase`** class, providing an optimized in-memory dictionary repository (`self.permit_database`) using unique Permit Numbers as keys for instant $O(1)$ lookups.

- **`services/` (Business Logic Layer):**
  - Contains the **`GovernmentPermitUtility`** class, coordinating registry operations such as adding permits, searching records, and rendering formatted tabular overviews of government filings.

- **`views/` (Presentation Layer):**
  - Implements the **`PortalView`** class, managing user input prompts, interactive CLI menu loops, and formatted terminal outputs.

- **Root Entry Point (`index.py`):**
  - Serves as the parent bootstrap file that instantiates the portal view and launches the application execution loop.

---

## 3. Alignment with Digital Public Goods (DPG) Standards
This project satisfies all core criteria required for Digital Public Goods recognition:
1. **Open-Source Transparency:** Hosted with clear documentation, making the source code freely inspectable, forkable, and improvable by public institutions.
2. **Inclusive and Accessible Design:** Built as a lightweight command-line interface (CLI) with clean text formatting, requiring minimal system resources and no proprietary software dependencies.
3. **Privacy-Respecting:** Designed with data minimization principles—storing only necessary administrative metadata while avoiding the exposure of hyper-sensitive citizen documents.
4. **Modular & Reusable:** Clean separation of concerns between models, services, and views allows public agencies to easily scale or adapt the code for other municipal applications.

---

## 4. Alignment with Sustainable Development Goals (SDGs)
By digitizing bureaucratic processes, this system directly supports global development targets:
- **SDG 16 (Peace, Justice, and Strong Institutions):** Promotes transparent, accountable, and corruption-free public governance by tracking institutional permit clearances digitally.
- **SDG 8 (Decent Work and Economic Growth):** Simplifies and accelerates business operating license approvals, lowering administrative barriers for entrepreneurs and boosting local commerce.
- **SDG 11 (Sustainable Cities and Communities):** Streamlines municipal zoning reviews and building construction permits to ensure safe, well-regulated urban development.

---

## 5. Project Directory Structure
```text
SOFT_ENG_PROJECT/
├── README.md                 
├── index.py                   
├── models/
│   └── permit.py              
├── database/
│   └── mock_db.py             
├── services/
│   └── permit_service.py      
└── views/
    └── portal_view.py         