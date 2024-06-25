import pandas as pd
import os

# Read the CSV file
csv_file = r'C:\Users\qusai\OneDrive\Documents\Desktop\AI project complete\combined_data.csv'
df = pd.read_csv(csv_file)

# Create directories for spam and ham emails
spam_dir = r'C:\Users\qusai\OneDrive\Documents\Desktop\AI project complete\spam_emails'
ham_dir = r'C:\Users\qusai\OneDrive\Documents\Desktop\AI project complete\ham_emails'
os.makedirs(spam_dir, exist_ok=True)
os.makedirs(ham_dir, exist_ok=True)

# Iterate through the DataFrame
for index, row in df.iterrows():
    label = row['label']
    text = row['text']
    filename = f"email-{index}.txt"  # Using 'email-index' as filename
    
    # Determine the directory based on the label
    if label == 1:
        folder = spam_dir
    else:
        folder = ham_dir
    
    # Write the email text to a text file
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
        file.write(text)

print("Files created successfully.")
