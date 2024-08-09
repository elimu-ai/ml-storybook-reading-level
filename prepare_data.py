import pandas as pd

# Select environment (TEST/PROD)
ENVIRONMENT = "PROD"

# Select language
# See https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
LANGUAGE = "HIN"

RAW_DATA_DIR = "./env-" + ENVIRONMENT + "/lang-" + LANGUAGE + "/data"
print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")

# Load the storybooks
storybooks_pd = pd.read_csv(RAW_DATA_DIR + "/storybooks.csv")
print(f"storybooks_pd: \n{storybooks_pd}")
