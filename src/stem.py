import sys
from pathlib import Path
from stem_engine import StemEngine

def main():
    if len(sys.argv) < 2:
            print("Usage: python src/stem.py <audio_file>")
                    sys.exit(1)

                        input_file = sys.argv[1]
                            if not Path(input_file).is_file():
                                    print(f"File not found: {input_file}")
                                            sys.exit(1)

                                                engine = StemEngine(engine="spleeter")
                                                    out_dir = engine.stem(input_file)
                                                        print(f"Stems written to: {out_dir}")

                                                        if __name__ == "__main__":
                                                            main()