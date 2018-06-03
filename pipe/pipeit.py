import shutil
import os
import errno



##super simple move files
##version .01
#adding class
class pipeit():
    def __init__(self, parent=None):
        super(pipeApp, self).__init__(parent)


    def ultraShout (shout):
        shout = shout
        print(shout)

    def ultraMove(source,destination):
        source = "C:\\sandbox\\source"
        destination = "C:\\sandbox\\target"


        #files = os.listdir(source)
        #
        #for f in files:
        shutil.move(source, destination)

    #ultraCopy v.01
    #used tocopy or publish from one directory to the next and do other fancy stuff.
    def ultraCopy(source,destination,ignored):
        source = "C:\\sandbox\\source"
        destination = "C:\\sandbox\\target"
        ignored = ""

        if os.path.isdir(source):
            if not os.path.isdir(destination):
                os.makedirs(destination)
            files = os.listdir(source)
            if ignore is not None:
                ignored = ignore(source, files)
            else:
                ignored = set()
            for f in files:
                if f not in ignored:
                    recursive_overwrite(os.path.join(source, f),
                                        os.path.join(destination, f),
                                        ignore)
        else:
            shutil.copyfile(source, destination)

    def ultraCopyTree(src, dst, symlinks=False, ignore=None):
        names = os.listdir(src)
        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()

        os.makedirs(dst)
        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    copytree(srcname, dstname, symlinks, ignore)
                else:
                    copy2(srcname, dstname)
                # XXX What about devices, sockets etc.?
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Error as err:
                errors.extend(err.args[0])
        try:
            copystat(src, dst)
        except WindowsError:
            # can't copy file access times on Windows
            pass
        except OSError as why:
            errors.extend((src, dst, str(why)))
        if errors:
            raise Error(errors)
