import csv

def read_csv_data(csv_files: list):
    all_data = []  # List to hold all data rows with column names

    for csv_file in csv_files:
        csv_text = csv_file.read().decode("utf-8")
        csv_reader = csv.reader(csv_text.splitlines())
        
        headers = next(csv_reader)  # Extracting the header row
        for row in csv_reader:
            if row:  # Ensuring the row is not empty
                row_data = {headers[i]: row[i] for i in range(len(row))}  # Create a dict with column names
                all_data.append(row_data)

    return all_data  # Return the list of dictionaries


if __name__ == "__main__":
    with open("benefit_labor.csv", "rb") as csv_file:
        raw_text = read_csv_data([csv_file])
        # print(data)

        from text_chunks import get_text_chunks
        chunks = get_text_chunks(raw_text)
        # print(chunks)

        from vector_store import get_vector_store
        vector_store = get_vector_store(chunks, "laborBenefit_index")