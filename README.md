## CocoaZip
Zip archiver with or without password

## Dependency
- Python 3.4 or later
- pyminizip
  - depends on zlib

## CommandLine Options
|option|param|desc|
|---|---|---|
|-d, --folder|[folder [folder folder....]]|Add Folder to Archive. Folder structure is kept|
|-f, --file|[file [file file....]]|Add File to Archive. Put on root in archive|
|-g, --gen_password|None|Generate password(length = 12)|
|-o, --output|path|Archive name. if default, Archive.zip is generated on current folder|
|-p, --password|password|Encrypt archive using specified password if you need. if use --gen_password, this option is override|
