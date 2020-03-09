
#import docutils.core
#    docutils.core.publish_file(source_path="introduction.rst", destination_path="introduction.html", writer_name="html")

import docutils.core
import os
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".rst"):
             file = (os.path.join(root, file))
             destination = file[0:-3] + "html"
             docutils.core.publish_file(source_path=file, destination_path=destination, writer_name="html")









