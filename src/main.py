from CocoaZip.ZipUtility import ZipUtility
from CocoaZip.CocoaZipBoard import CocoaZipBoard

import sys

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
            prog='CocoaZip', 
            usage='Zip Archiver', 
            description='description', 
            epilog='end')

    parser.add_argument('-f', '--file', nargs='*', help = 'Add File to Archive(can specify like a list)')
    parser.add_argument('-d', '--folder', nargs='*', help = 'Add Folder to Archive(can specify like a list)')
    parser.add_argument('-o', '--output', default = 'Archive.zip', help = 'Archive name. Default is "Archive.zip"')
    parser.add_argument('-p', '--password', help = "Encrypt archive using password if you need")
    parser.add_argument('-g', '--gen_password', action = 'store_true', help = 'Generate password(length = 12)')
    parser.add_argument('--override', action = 'store_true', help = "Allow override if exists archive, otherwise raise error")
    parser.add_argument('--gui', type = bool, help = 'Display GUI')

    args = parser.parse_args()

    if (len(sys.argv) == 1) or (args.gui and len(sys.argv == 2)):
        window = CocoaZipBoard(False)
        window.MainLoop()
        sys.exit()

    zipUtil = ZipUtility()
    password = None
    if args.gen_password:
        password = zipUtil.PasswordGeneration()
    elif args.password is not None:
        password = args.password
    print(password)
    if args.folder is not None:
        for d in args.folder:
            zipUtil.AddFolder(d)
            
    if args.file is not None:
        for f in args.file:
            zipUtil.AddFile(f)

    zipUtil.Compress(archive = args.output, password = password, override = args.override)

