# space-id
Invisible Watermarks with Space Characters in ASCII Files

## Usage

    usage: spaceid.py [-h] [-f path] [-i path] [-p path] [--remove] [--debug]

    Online Hash Checker

    optional arguments:
      -h, --help  show this help message and exit
      -f path     File to ID (if used with -i it writes the ID to the file)
      -i path     ID (writes ID to file)
      -p path     Preamble to start the space ID with
      --remove    Remove space ID
      --debug     Debug output

## Screenshots

![Space ID Screenshot](https://github.com/Neo23x0/space-id/blob/master/screenshots/screen1.png "Space ID in action")
![Space ID Screenshot](https://github.com/Neo23x0/space-id/blob/master/screenshots/screen2.png "Space ID modified file")

## Examples

Add a space ID to an ASCII file with debug output
```
python3 spaceid.py -i client01 -f ./test/test.txt --debug
```

Read a space ID from a file
```
python3 spaceid.py -f ./test/test.txt
```

Remove a space ID from a file
```
python3 spaceid.py -f ./test/test.txt --remove
```