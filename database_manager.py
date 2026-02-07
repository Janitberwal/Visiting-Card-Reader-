import pandas as pd
import os

def save_to_excel(result_json , excel_path="data/extracted/business_cards.xlsx"):
    try:
        print("DEBUG: save_to_excel CALLED")
        print("DEBUG DATA RECEIVED:", result_json)

        processed_data={
            "Owner Name":result_json.get("primary_owner",""),
            "Company Name":result_json.get("primary_company",""),
            "Email":" ,".join(result_json.get("emails",[]))if isinstance(result_json.get("emails"), list) else result_json.get("emails"),
            "Phone Numbers":" ,".join(result_json.get("phone_numbers",[])) if isinstance(result_json.get("phone_numbers"), list) else result_json.get("phone_numbers"),
            "Address":result_json.get("address","")
        }

        new_row = pd.DataFrame([processed_data])

        #create directory if not exists
        os.makedirs(os.path.dirname(excel_path),exist_ok=True)

        #append to exisiting file or create new
        if(os.path.exists(excel_path)):
            existing_df = pd.read_excel(excel_path)
            updated_df = pd.concat([existing_df , new_row] , ignore_index=True)
            updated_df.to_excel(excel_path , index=False)
        else:
            new_row.to_excel(excel_path , index=False)
        
        print(f"Data saved successfully to {excel_path}")
        return True
    except Exception as e:
        print(f"Error saving data to excel: {e}")
        return False