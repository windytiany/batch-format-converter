import os
import subprocess
import argparse
from pathlib import Path


if __name__ == '__main__':        
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", nargs="?", default=".", 
                        help="the path for files to be converted, default to current directory.")
    parser.add_argument("--out-dir", nargs="?", 
                        help="the save path for converted files, default to original directory.")
    parser.add_argument("--ffmpeg-path", nargs="?", default="ffmpeg",
                        help="the path for ffmpeg executable, default to globally installed ffmpeg.")
    parser.add_argument("--overwrite", "-w", action="store_true", default=False,
                        help="whether to delete original files, default to false.")
    parser.add_argument("--recursive", "-r", action="store_true", default=False,
                        help="whether to iterate files recursively, default to false.")
    parser.add_argument("--input-format", "-i", required=True, nargs="*",
                        help="the formats to be converted. example: .png .mp3 .mkv")
    parser.add_argument("--output-format", "-o", required=True,
                        help="the target format to convert. example: .png .mp3 .mkv")
    parser.add_argument("--extra", default="", type=str,
                        help="extra arguments passed to ffmpeg.")

    args = parser.parse_args()
    file_dir = Path(args.dir)
    if args.out_dir:
        out_dir = Path(args.out_dir)
    else:
        out_dir = None
    ffmpeg_path = args.ffmpeg_path
    is_overwrite = args.overwrite
    is_recursive = args.recursive
    input_format = args.input_format
    output_format = args.output_format
    extra_args = args.extra

    file_iter = file_dir.rglob("*") if is_recursive else file_dir.iterdir()
    for file in file_iter:
        if file.suffix not in input_format:
            continue
        
        if out_dir:
            out_filename = file.with_suffix(output_format).name
            out_path = out_dir.joinpath(out_filename)
        else:
            out_path = file.with_suffix(output_format)
            
        subprocess.run(f"{ffmpeg_path} -i {file} {extra_args} {out_path}", shell=True)
        
        if is_overwrite:
            os.remove(file)
