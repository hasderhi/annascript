from parser import parse_text
from renderer import render
import argparse
import time
import sys

def run_file(input_path: str, output_path: str):
    start_time = time.time()

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    ast = parse_text(text)
    html_out = render(ast)
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(html_out)

    end_time = time.time()
    elapsed_time_ms = round((end_time - start_time) * 1000, 2)

    print(f"Wrote {output_path} in {elapsed_time_ms}ms")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Process annaScript files and output HTML.")
    p.add_argument("input", nargs="?", help="Path to the input file (annaScript).")
    p.add_argument("output", nargs="?", help="Path to the output file (HTML).")
    
    if len(sys.argv) == 1:
        print("Error: No arguments provided.")
        p.print_help()
        sys.exit(1)

    args = p.parse_args()
    
    if args.input is None or args.output is None:
        print("Error: Both input and output paths are required.")
        p.print_help()
        sys.exit(1)

    run_file(args.input, args.output)
