import pygsheets

def main():
    try:
        # Authenticate and open the spreadsheet
        client = pygsheets.authorize(service_account_file="tutor-attendance-sheet-42ac4078dc25.json")
        spreadsheet = client.open("Tutor Attendance")
        wks = spreadsheet.worksheet("title", "Tutor Attendance")

        # Define the list of student IDs
        bottom30 = []

        # Get student IDs from user input
        student_id = input("Enter Student ID (Type \"End\" to end process): ")
        while student_id != "End":
            if len(student_id) == 3:
                bottom30.append("67070" + student_id)
            else:
                bottom30.append(student_id)
            student_id = input("Enter Student ID (Type \"End\" to end process): ")

        bottom30.sort()

        # Define the range of cells to update
        cell_range = 'B4:B212'
        cells = wks.range(cell_range)

        # Define the highlight color (normalized to [0, 1])
        highlight_color = (221/255, 126/255, 107/255)  # Light orange color

        # Prepare cells to be updated
        cells_to_update = []
        for cell in cells:
            cell_obj = cell[0]  # Use the cell object directly

            # Check if cell value is None or empty
            cell_value = cell_obj.value
            if cell_value is not None and cell_value in bottom30:
                # Modify the color only
                cell_obj.color = highlight_color
                cells_to_update.append(cell_obj)
            else:
                # Optionally reset color if needed
                cell_obj.color = None

        # Function to update cells in batches
        def update_cells_in_batches(worksheet, cells, batch_size=100):
            for i in range(0, len(cells), batch_size):
                batch = cells[i:i + batch_size]
                try:
                    worksheet.update_cells(batch)
                except Exception as e:
                    print(f"An error occurred during batch update: {e}")

        # Update the cells
        if cells_to_update:
            update_cells_in_batches(wks, cells_to_update)

        print("Cells updated successfully.")

    except pygsheets.PyGsheetsException as pe:
        print(f"Pygsheets error: {pe}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
