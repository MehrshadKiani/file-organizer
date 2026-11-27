# File Organizer

A command-line tool that sorts the files in a folder into subfolders by type (Images, Documents, Archives, Audio, Video, Other).

## What it does

- Sorts files by extension into category subfolders
- Preview mode by default: shows what would happen and changes nothing
- Never overwrites files: duplicates are renamed (`photo_1.jpg`, `photo_2.jpg`, ...)
- Categories and extensions are easy to change at the top of `organize.py`

## Requirements

- Python 3.9+
- No external libraries

## How to use

1. Preview (nothing is moved):

   ```
   python organize.py path/to/folder
   ```

2. Actually move the files:

   ```
   python organize.py path/to/folder --run
   ```

## Example

```
[preview] photo.jpg -> Images/photo.jpg
[preview] notes.txt -> Documents/notes.txt
[preview] unknown.xyz -> Other/unknown.xyz
Done: 3 file(s) would be moved.
```