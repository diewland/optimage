import json
from pprint import pprint as pp
 
NAME    = "OptiMage"
DESC    = "Draw prizes every 13th of every month, worth 13$, 48 times, numbers from the website. https://cryptofees.info/ decimal number ETH 1Dayfees"
IMG     = "https://diewland.github.io/optimage/assets/cover.png"
ENGINE  = "Jigsaw Engine"

OUTPUT_DIR  = "./json"
FROM_ID     = 1
TO_ID       = 100

if __name__ == "__main__":

    # craft metadata
    metadata = {
      "name": "***",
      "description": DESC,
      "image": IMG,
      "compiler": ENGINE,
    }

    # build json + write to file
    for id in range(FROM_ID, TO_ID+1):

        # update data
        metadata["name"] = "{} #{}".format(NAME, id)

        # debug
        #print(metadata)

        # write file
        with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
            json.dump(metadata, f, ensure_ascii=False)
