import json, urllib, sys
import settings

def get_languages_json():
    '''Get languages supported by Google Translate in a json payload'''

    url = 'https://www.googleapis.com/language/translate/v2/languages?key={0}'
    response = urllib.urlopen(url.format(settings.GOOGLE_TRANSLATE_API_KEY))
    langs_json = json.load(response)

    return langs_json

def get_languages():
    '''Get a list of languages supported by Google Translate'''
    
    langs_json = get_languages_json()
    langs = []
    for lang_node in langs_json['data']['languages']:
        langs.append(lang_node['language'])

    return langs

def get_translation(source, target, query):
    '''Translate a query (word/phrase/sentence) from source language to target language using the Google Translate API'''

    url = 'https://www.googleapis.com/language/translate/v2?key={0}&source={1}&target={2}&q={3}'
    response = urllib.urlopen(url.format(settings.GOOGLE_TRANSLATE_API_KEY,
                                        source,
                                        target,
                                        query))
    translation_json = json.load(response)

    return "{0}\t{1}".format(target, 
                            translation_json['data']['translations'][0]['translatedText'].encode('utf-8'))

def main():
    '''Prints out the given query in all languages supported by the Google Translate API'''

    source_lang = sys.argv[1]
    query = sys.argv[2]

    target_langs = get_languages()
    target_langs.remove(source_lang) # don't want to translate from source to source

    for target_lang in target_langs:
        print get_translation(source_lang, target_lang, query)

if __name__ == '__main__':
    main()
