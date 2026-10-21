class CitizenPermit:
    total_permits_issued = 0
    
    def __init__(self, permit_number, citizen_name, national_id, permit_type):
        self.permit_number = permit_number
        self.citizen_name = citizen_name
        self.national_id = national_id
        self.permit_type = permit_type
        
        self.clearance_stages = {}
        
        CitizenPermit.total_permits_issued += 1
    
    def record_clearance(self, stage_code, stage_name, status):
        if CitizenPermit.validate_status(status):
            self.clearance_stages[stage_code] = (stage_name, status)
            print(f"-> Success: Clearance recorded for {self.citizen_name} at stage [{stage_code}] {stage_name}")
        else:
            print("-> ERROR: INVALID STATUS. STATUS MUST BE 'APPROVED', 'PENDING', OR 'REJECTED'")
            
    def calculate_overall_status(self):
        if not self.clearance_stages:
            return "No clearance stages logged yet"
    
        statuses = [status for _, status in self.clearance_stages.values()]
        
        if all(s == "APPROVED" for s in statuses):
            standing = "Fully Approved / Active Permit"
        elif any(s == "REJECTED" for s in statuses):
            standing = "Rejected / Action Required"
        else:
            standing = "Under Review / Pending"
        
        return f"Total Stages: {len(statuses)} | Status: {standing}"
    
    def display_info(self):
        print("-" * 50)
        print(f"PERMIT_RECORD: {self.permit_number}")
        print("-" * 50)
        print(f"Citizen Name : {self.citizen_name}")
        print(f"National ID  : {self.national_id}")
        print(f"Permit Type  : {self.permit_type}")
        print("\nREGULATORY CLEARANCE STAGES")

        if not self.clearance_stages:
            print("  (NO CLEARANCE STAGES LOGGED YET)")
        else:
            for code, (name, status) in self.clearance_stages.items():
                print(f"* [{code}] {name}: {status}")
                
        print(f"\nCompliance  : {self.calculate_overall_status()}")
        print("-" * 50)
    
    @classmethod
    def get_total_system_permits(cls):
        return f"[Govt Portal Stat] Total permits processed in system: {cls.total_permits_issued}"
    
    @staticmethod 
    def validate_status(status):
        valid_statuses = ["APPROVED", "PENDING", "REJECTED"]
        return isinstance(status, str) and status.upper() in valid_statuses