## Batch format converter

A simple batch format converter using ffmpeg and python.


## Prerequisite
You need install [ffmpeg](https://ffmpeg.org/) to use this program. You can either use globally installed ffmpeg or specify the path to ffmpeg executable.


## Installation

#### Download from Releases
Go to [Releases](https://github.com/windytiany/batch-format-converter/releases) page and download corresponding executable. 
> **Notice**
>
> Currently only windows build is available.

#### Build
1. Clone this repo.
```bash
git clone https://github.com/windytiany/batch-format-converter.git
```
2. Install pyinstaller.
```bash
pip install pyinstaller
```
3. Build using pyinstaller.
```bash
pyinstaller --onefile --name "bfot" main.py 
```


## Usage
```bash
usage: bfot [-h] [--dir [DIR]] [--out-dir [OUT_DIR]] [--ffmpeg-path [FFMPEG_PATH]] [--overwrite] [--recursive] --input-format 
            [INPUT_FORMAT ...] --output-format OUTPUT_FORMAT [--extra EXTRA]                                                            

options:
  -h, --help            show this help message and exit
  --dir [DIR]           the path for files to be converted, default to current directory.
  --out-dir [OUT_DIR]   the save path for converted files, default to original directory.
  --ffmpeg-path [FFMPEG_PATH]
                        the path for ffmpeg executable, default to globally installed ffmpeg.
  --overwrite, -w       whether to delete original files, default to false.
  --recursive, -r       whether to iterate files recursively, default to false.
  --input-format [INPUT_FORMAT ...], -i [INPUT_FORMAT ...]
                        the formats to be converted. example: .png .mp3 .mkv
  --output-format OUTPUT_FORMAT, -o OUTPUT_FORMAT
                        the target format to convert. example: .png .mp3 .mkv
  --extra EXTRA         extra arguments passed to ffmpeg.
```


## License
This program is licensed under [MIT](https://raw.githubusercontent.com/windytiany/batch-format-converter/refs/heads/main/LICENSE).
