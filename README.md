## CocoaZip
Simple zip archiver with or without password

## Dependency
- Python 3.4 or later
- pyminizip
  - depends on zlib

## CommandLine Options
|option|param|desc|
|---|---|---|
|-d, --folder|folder [folder folder....]|Add Folder to Archive. Folder structure is kept|
|-f, --file|file [file file....]|Add File to Archive. Put on root in archive|
|-g, --gen_password|None|Generate password(length = 12)|
|-o, --output|path|Archive name. if default, Archive.zip is generated on current folder|
|-p, --password|password|Encrypt archive using specified password if you need. if use --gen_password, this option is override|


## Use
### case : zipping SINGLE file
```
$ python main.py -- file nyan.txt --output nyan.zip


Output:
  nyan.zip/
    └ nyan.txt
```

### case : zipping MULTIPLE files
```
$ python main.py --file nyan.txt myon.txt --output nyan.zip

Output:
  nyan.zip/
    ┝ nyan.txt
    └ myon.txt
```

### case : zipping SINGLE folder
```
$ python main.py --folder nyan --output nyan.zip

Input:
  nyan/
    ┝ nyan.txt
    └ myon.txt

Output:
  nyan.zip/
    └ nyan/
        ┝ nyan.txt
        └ myon.txt
```

### case : zipping MULTIPLE folder
```
$ python main.py --folder nyan myon --output nyan.zip

Input:
  nyan/
    └ nyan.txt
  myon/
    └ myon.txt

Output:
  nyan.zip/
    ┝ nyan/
    |   └ nyan.txt
    └ myon/
        └ myon.txt
```

### case : zipping file and folder
```
$ python main.py --file nyan.txt --folder myon --output nyan.zip

Input:
  nyan.txt
  myon/
    └ myon.txt

Output:
  nyan.zip/
    ┝ nyan.txt
    └ myon/
        └ myon.txt

```