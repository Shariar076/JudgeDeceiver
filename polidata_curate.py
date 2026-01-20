import json
import pandas as pd
from tqdm import tqdm

statement_file = json.loads(open("dataset/data_for_train/basic/policomp/example.jsonl", "r").read())

data = []

for i in tqdm(range(len(statement_file))):
    statement = statement_file[i]["statement"]
    data.append(dict(
        instruction="Please respond to the following statement.\n",
        text=statement,
        target="I strongly agree because, " 
    ))


pd.DataFrame(data).to_csv("dataset/data_for_train/basic/policomp/policomp_train_1.csv", index=False)