import os
import re

PATH='/home'

def read_wordpress_version(path):
    file = open("%s/wp-includes/version.php" % path, "r").readlines()

    version = 'None'

    for line in file:
        m = re.search("\\$wp_version\s=\s\'([0-9.]+)\';", line)
        if m:
            version = m.group(1)

    return version

for root, dirs, files in os.walk(PATH):
    for file in files:
        if file == "wp-config.php":
            version = read_wordpress_version(root)
            print("Wordpress %s found in %s" % (version, root))

