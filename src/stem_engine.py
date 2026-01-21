from pathlib import Path
from spleeter.separator import Separator

class StemEngine:
    def __init__(self, engine: str = "spleeter"):
            if engine != "spleeter":
                        raise ValueError("Only 'spleeter' is supported in this minimal setup.")
                                self.engine = engine
                                        self.separator = Separator("spleeter:2stems")

                                            def stem(self, input_file: str, output_dir: str = "stems") -> str:
                                                    output_path = Path(output_dir)
                                                            output_path.mkdir(exist_ok=True)
                                                                    self.separator.separate_to_file(input_file, str(output_path))
                                                                            return str(output_path)