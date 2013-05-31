Omni Translator
================

Translate one word to all languages supported by the Google Translate API.

**Usage**

`python translate.py <source_language> <word>`

Expect the app to run for 5-60 seconds depending on your internet speed and Google's servers. It will make ~50 json requests.

**Example Usage**

Output to the console:  
`python translate.py en moped`

Or output to a file:  
`python translate.py en moped > moped_or_whatever_name.txt`

**Requirements**

A Google Translate API key is required. 

To obtain one, 

1. Go to: https://code.google.com/apis/console/
2. Enable Translate API, if not already enabled.
3. Add your billing info, if not already added.
4. Create (or re-use an existing) server key. 

Note:

While Google technically does not have a free quota for the Translate API, the cost of running this app is negligible. The motivation for this app is to translate one word into all the ~50 supported languages. So, for example, if your word is five characters long, that's only 250 characters translated. They charge on the order of $20 per million characters processed. That equates to $0.005 (a half cent) in our example.

**License**

You may modify this file as desired, except keep my credit. Thanks.

**Author**

Bill Paetzke
