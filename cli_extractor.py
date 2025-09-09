#!/usr/bin/env python3
"""
Simple command-line interface for the text extractor.
This version can be used without Streamlit for quick testing.
"""

import sys
import os
import argparse
from text_extractor import TextExtractor
import json

def main():
    parser = argparse.ArgumentParser(description='Extract text from images and PDFs')
    parser.add_argument('input_file', help='Path to the input file (image or PDF)')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('-f', '--format', choices=['text', 'json'], default='text',
                       help='Output format: text or json (default: text)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
    
    try:
        # Initialize extractor
        print("Initializing text extractor...")
        extractor = TextExtractor()
        
        # Extract text
        print(f"Processing: {args.input_file}")
        
        if args.format == 'text':
            result = extractor.extract_text(args.input_file, output_format='text')
            output_content = result
        else:
            result = extractor.extract_text(args.input_file, output_format='detailed')
            output_content = json.dumps(result, indent=2, ensure_ascii=False)
        
        # Output results
        if args.output:
            # Save to file
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_content)
            print(f"Results saved to: {args.output}")
        else:
            # Print to console
            print("\n" + "="*50)
            print("EXTRACTED TEXT:")
            print("="*50)
            if args.format == 'text':
                print(result)
            else:
                print(json.dumps(result, indent=2, ensure_ascii=False))
        
        if args.verbose:
            print(f"\nProcessing completed successfully.")
            if args.format == 'text':
                print(f"Extracted {len(result)} characters.")
    
    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
