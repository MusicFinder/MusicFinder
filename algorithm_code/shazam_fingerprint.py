# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from dejavu import Dejavu
config = {
    "database": {
        "host": "127.0.0.1", #"192.168.1.171",
        "user": "root",
        "passwd": "1234567", 
        "db": "ir_data",
    }
}
djv = Dejavu(config)
djv.fingerprint_directory("MusicTrain", [".wav"], 4)
print (djv.db.get_num_fingerprints())