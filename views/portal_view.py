from models.permit import CitizenPermit
from services.permit_service import GovernmentPermitUtility

class PortalView:
    def __init__(self):
        self.portal = GovernmentPermitUtility()
        p1 = CitizenPermit("SLP-2026-01", "Fatu Kamara", "NID-987654", "Business Operating License")
        p2 = CitizenPermit("SLP-2026-02", "Ibrahim Bangura", "NID-123456", "Building Construction Permit")
        
        self.portal.add_permit(p1)
        self.portal.add_permit(p2)
        
        p1.record_clearance("ENV01", "Environmental Impact Assessment", "APPROVED")
        p1.record_clearance("TAX02", "National Revenue Authority (NRA) Tax Clearance", "APPROVED")
        
        p2.record_clearance("MCD01", "Municipal City Council Zoning Review", "PENDING")

    def run(self):
        while True:
            print("\n=============================================")
            print("DIGITAL PERMIT & LICENSE MANAGEMENT PORTAL")
            print("=============================================")
            print("1. View all Registered Permits")
            print("2. Issue a New Permit Application")
            print("3. Record Regulatory Clearance Stage")
            print("4. View Individual Permit Status & Profile")
            print("5. View System Statistics (Class Method)")
            print("6. Exit Portal")
            
            choice = input("\nEnter Your Choice(1-6): ").strip()
            
            if choice == "1":
                self.portal.display_all_permits()
                
            elif choice == "2":
                print("\n----- ISSUE NEW PERMIT APPLICATION -------")
                p_no = input("Enter Permit Number (e.g., SLP-2026-03): ").strip()
                name = input("Enter Citizen Full Name: ").strip()
                nid = input("Enter National ID Number: ").strip()
                p_type = input("Enter Permit / License Type: ").strip()
                
                new_permit = CitizenPermit(p_no, name, nid, p_type)
                self.portal.add_permit(new_permit)
                
            elif choice == "3":
                print("\n----- Record Regulatory Clearance Stage -----")
                p_no = input("Enter Permit Number: ").strip()
                permit = self.portal.find_permit(p_no)
                
                if permit:
                    code = input("Enter Stage Code (e.g., FIRE01): ").strip().upper()
                    stage_name = input("Enter Stage Description: ").strip()
                    status = input("Enter Status (APPROVED / PENDING / REJECTED): ").strip().upper()
                    permit.record_clearance(code, stage_name, status)
                else:
                    print(f"-> Error: Permit Number '{p_no}' not found.")
                    
            elif choice == "4":
                print("\n----- View Permit Profile & Clearance -----")
                p_no = input("Enter Permit Number: ").strip()
                permit = self.portal.find_permit(p_no)
                if permit:
                    permit.display_info()
                else:
                    print(f"-> Error: Permit Number '{p_no}' not found.")    
                    
            elif choice == "5":
                print("\n" + CitizenPermit.get_total_system_permits())

            elif choice == "6":
                print("\nExiting Government Permit Portal. Goodbye!")
                break
            else:
                print("-> Invalid choice! Please select an option between 1 and 6.")