# ParseMMI

A small Python utility to batch parse media files (videos for now) resolutions and bitrates supported by Audi's MMI Systems.

## Features

- Batch-processes all video files in a given directory
- Preserves aspect ratio 
- Supports `.mp4`, `.mov`, `.avi`, `.mkv`

## Requirements

- Python 3.6+
- `ffmpeg` installed and available in system PATH
- Python packages:
  ```
  pip install ffmpeg-python
  ```

## Usage

```
python parser.py <source_folder> <destination_folder> [width] [height]
```
Fields `width` and `height` are optional.

### Example

```
python downscale.py ./input ./output 640 480
```

## Notes

- The script prompts before overwriting existing output files
- It avoids upscaling — videos smaller than the target resolution are left unchanged