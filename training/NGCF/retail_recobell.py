import csv
import re

import progressbar
from collections import defaultdict

data = defaultdict(list)

# with open("../Data/recobell/_train.rating", "r") as f:
#     csv_reader = csv.reader(f, delimiter='|', quotechar='', quoting=csv.QUOTE_NONE)
#     for line in progressbar.ProgressBar()(csv_reader):
#         uid, itemid = int(line[0]), int(line[1])
#         data[uid].append(itemid)
#
# with open("../Data/recobell/train.txt", "w") as f:
#     for u, i in data.items():
#         line = [u]
#         line.extend(i)
#         line = list(map(str, line))
#         f.write(' '.join(line)+"\n")

with open("../Data/recobell/test_negative.txt", "w") as f1:
    with open("../Data/recobell/_test.negative", "r") as f:
        csv_reader = csv.reader(f, delimiter='|', quotechar='', quoting=csv.QUOTE_NONE)
        for line in progressbar.ProgressBar()(csv_reader):
            uiid, neg_itemid = line[0], line[2:]
            # uid = int(re.search(r'\d+', uiid).group())
            # pos_itemid = int(re.search(r'\d+', uiid.split(',')[-1]).group())
            pos_itemid = line[1]
            line = [uiid, pos_itemid]
            line.extend(neg_itemid)
            line = list(map(str, line))
            f1.write(' '.join(line)+"\n")
