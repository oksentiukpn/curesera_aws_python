data = [
    {"Code": "bg", "Language": "Bulgarian"},
    {"Code": "hr", "Language": "Croatian"},
    {"Code": "cs", "Language": "Czech"},
    # {
    #   "Code": "da",
    #   "Language": "Danish"
    # },
    {"Code": "bg", "Language": "Bulgarian"},
    {"Code": "hr", "Language": "Croatian"},
    {"Code": "cs", "Language": "Czech"},
    {"Code": "da", "Language": "Danish"},
    {"Code": "nl", "Language": "Dutch"},
    {"Code": "en", "Language": "English"},
    {"Code": "et", "Language": "Estonian"},
    {"Code": "fi", "Language": "Finnish"},
    {"Code": "fr", "Language": "French"},
    {"Code": "de", "Language": "German"},
    {"Code": "el", "Language": "Greek"},
    {"Code": "hu", "Language": "Hungarian"},
    {"Code": "ga", "Language": "Irish"},
    {"Code": "it", "Language": "Italian"},
    {"Code": "lv", "Language": "Latvian"},
    {"Code": "lt", "Language": "Lithuanian"},
    {"Code": "mt", "Language": "Maltese"},
    {"Code": "pl", "Language": "Polish"},
    {"Code": "pt", "Language": "Portuguese"},
    {"Code": "ro", "Language": "Romanian"},
    {"Code": "sk", "Language": "Slovak"},
    {"Code": "sl", "Language": "Slovenian"},
    {"Code": "es", "Language": "Spanish"},
    {"Code": "sv", "Language": "Swedish"},
]

for row in data:
    put_response = dynamo.put_item(
        TableName="LanguagesTable",
        Item={"Code": {"S": row["Code"]}, "Language": {"S": row["Language"]}},
    )
