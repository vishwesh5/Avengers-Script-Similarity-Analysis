import re
script_processed = open("script-processed.txt",'w')
with open("script-raw.txt",'r') as script_raw:
    for line in script_raw.readlines():
        x = re.sub("[\(\[].*?[\)\]]", "", line)
        x = x.strip()
        script_processed.write("{}\n".format(x))
script_processed.close()
