from database.mock_db import MockDatabase

class GovernmentPermitUtility:
    def __init__(self):
        self.db = MockDatabase()
        self.permit_database = self.db.permit_database
        
    def add_permit(self, permit_obj):
        if permit_obj.permit_number in self.permit_database:
            print(f"-> ERROR: Permit Number {permit_obj.permit_number} already exists")
        else:
             self.permit_database[permit_obj.permit_number] = permit_obj
             print(f"-> SUCCESS: Permit for {permit_obj.citizen_name} added to the government registry directly")
             
    def find_permit(self, permit_number):
        return self.permit_database.get(permit_number, None)
    
    def display_all_permits(self):
        if not self.permit_database:
            print("\n -> The government permit database is currently empty.")
            return

        print("\n" + "=" * 80)
        print(f"{'DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM - ALL RECORDS':^80}")
        print("=" * 80)
        print(f"{'Permit No':<12} | {'Citizen Name':<22} | {'Permit Type':<28} | {'Stages':<8}")
        print("-" * 80)
        
        for p_no, permit in self.permit_database.items():
            print(f"{permit.permit_number:<12} | {permit.citizen_name:<22} | {permit.permit_type:<28} | {len(permit.clearance_stages):<8}")
            
        print("=" * 80)