"""
Copy Braintrust dataset from one account to another
"""

import base64
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import braintrust
from src.openrouter_classifier import VALID_CLASSES

# Source account (read-only)
SOURCE_API_KEY = "SOURCE API"
SOURCE_PROJECT = "DSHB_amfam_capstone_2026"
SOURCE_DATASET = "fixed_size_sampled"

# Destination account (write)
DEST_API_KEY = "DESTINATION API"
DEST_PROJECT = "AMFAM v2"
DEST_DATASET = "fixed_size_sampled"

def copy_dataset():
    """Copy dataset from source to destination"""
    
    # Login to source account
    print(f"Connecting to source account...")
    braintrust.login(api_key=SOURCE_API_KEY)
    source_dataset = braintrust.init_dataset(project=SOURCE_PROJECT, name=SOURCE_DATASET)
    
    # Load all records from source
    print(f"Loading records from {SOURCE_PROJECT}/{SOURCE_DATASET}...")
    records = []
    for i, row in enumerate(source_dataset):
        expected = row.get("expected")
        input_data = row.get("input") or {}
        attachment = input_data.get("image")
        metadata = input_data.get("metadata", {})
        
        # Skip placeholder rows
        if metadata.get("placeholder", False):
            continue
            
        if expected not in VALID_CLASSES or not attachment:
            continue
        
        # Try to get filename from reference
        filename = None
        try:
            reference = getattr(attachment, "reference", None) or {}
            filename = reference.get("filename")
        except (KeyError, AttributeError):
            pass
        
        # If no filename, use document_id or fallback
        if not filename:
            doc_id = input_data.get("document_id")
            if doc_id and doc_id != "generated":
                filename = f"{doc_id}.png"
            else:
                filename = f"document_{i+1}.png"
        
        records.append({
            "image_b64": base64.b64encode(attachment.data).decode("utf-8"),
            "filename": filename,
            "expected": expected,
            "metadata": metadata
        })
        
        if (i + 1) % 10 == 0:
            print(f"  Loaded {i+1} records...")
    
    print(f"Total records loaded: {len(records)}")
    
    # Login to destination account
    print(f"\nConnecting to destination account...")
    braintrust.login(api_key=DEST_API_KEY, force_login=True)
    
    # Create destination dataset
    print(f"Creating dataset {DEST_PROJECT}/{DEST_DATASET}...")
    dest_dataset = braintrust.init_dataset(project=DEST_PROJECT, name=DEST_DATASET)
    
    # Copy records to destination
    print(f"Copying {len(records)} records to destination...")
    for i, record in enumerate(records):
        # Create input with image attachment
        input_data = {
            "image": braintrust.Attachment(
                data=base64.b64decode(record["image_b64"]),
                filename=record["filename"],
                content_type="image/png"
            ),
            "metadata": record.get("metadata", {})
        }
        
        # Insert row
        dest_dataset.insert(
            input=input_data,
            expected=record["expected"],
            metadata={"source": "copied_from_dshb_account"}
        )
        
        if (i + 1) % 10 == 0:
            print(f"  Copied {i+1}/{len(records)} records...")
    
    print(f"\nDataset copy complete! {len(records)} records copied to {DEST_PROJECT}/{DEST_DATASET}")

if __name__ == "__main__":
    copy_dataset()