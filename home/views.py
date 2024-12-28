from django.shortcuts import render, HttpResponse
from googletrans import Translator

#list of all lang with lang codes
lang_list = {
            'Afrikaans' : 'af',
            'Albanian' : 'sq',
            'Amharic' : 'am',
            'Arabic' : 'ar',
            'Armenian' : 'hy',
            'Azerbaijani' : 'az',
            'Basque' : 'eu',
            'Belarusian' : 'be',
            'Bengali' : 'bn',
            'Bosnian' : 'bs',
            'Bulgarian' : 'bg',
            'Catalan' : 'ca',
            'Cebuano':'ceb',
            'Chichewa' : 'ny',
            'Chinese':'zh-CN',
            'Corsican' : 'co',
            'Croatian' : 'hr',
            'Czech' : 'cs',
            'Danish' : 'da',
            'Dutch' : 'nl',
            'English' : 'en',
            'Esperanto' : 'eo',
            'Estonian' : 'et',
            'Filipino' : 'tl',
            'Finnish' : 'fi',
            'French' : 'fr',
            'Frisian' : 'fy',
            'Galician' : 'gl',
            'Georgian' : 'ka',
            'German' : 'de',
            'Greek' : 'el',
            'Gujarati' : 'gu',
            'Haitian Creole' : 'ht',
            'Hausa' : 'ha',
            'Hawaiian ':'haw',
            'Hebrew' : 'he',
            'Hindi' : 'hi',
            'Hmong ' : 'hmn',
            'Hungarian' : 'hu',
            'Icelandic' : 'is',
            'Igbo' : 'ig',
            'Indonesian' : 'id',
            'Irish' : 'ga',
            'Italian' : 'it',
            'Japanese' : 'ja',
            'Javanese' : 'jw',
            'Kannada' : 'kn',
            'Kazakh' : 'kk',
            'Khmer' : 'km',
            'Kinyarwanda' : 'rw',
            'Korean' : 'ko',
            'Kurdish' : 'ku',
            'Kyrgyz' : 'ky',
            'Lao' : 'lo',
            'Latin' : 'la',
            'Latvian' : 'lv',
            'Lithuanian' : 'lt',
            'Luxembourgish' : 'lb',
            'Macedonian' : 'mk',
            'Malagasy' : 'mg',
            'Malay' : 'ms',
            'Malayalam' : 'ml',
            'Maltese' : 'mt',
            'Maori' : 'mi',
            'Marathi' : 'mr',
            'Mongolian' : 'mn',
            'Myanmar ' : 'my',
            'Nepali' : 'ne',
            'Norwegian' : 'no',
            'Odia' : 'or',
            'Pashto' : 'ps',
            'Persian' : 'fa',
            'Polish' : 'pl',
            'Portuguese' : 'pt',
            'Punjabi' : 'pa',
            'Romanian' : 'ro',
            'Russian' : 'ru',
            'Samoan' : 'sm',
            'Scots Gaelic' : 'gd',
            'Serbian' : 'sr',
            'Sesotho' : 'st',
            'Shona' : 'sn',
            'Sindhi' : 'sd',
            'Sinhala' : 'si',
            'Slovak' : 'sk',
            'Slovenian': 'sl',
            'Somali' : 'so',
            'Spanish': 'es',
            'Sundanese': 'su',
            'Swahili ': 'sw',
            'Swedish' : 'sv',
            'Tajik' : 'tg',
            'Tamil' : 'ta',
            'Tatar ': 'tt',
            'Telugu' : 'te',
            'Thai ': 'th',
            'Turkish ': 'tr',
            'Turkmen' : 'tk',
            'Ukrainian ': 'uk',
            'Urdu' : 'ur',
            'Uyghur' : 'ug',
            'Uzbek' : 'uz',
            'Vietnamese' : 'vi',
            'Welsh' : 'cy',
            'Xhosa' : 'xh',
            'Yiddish' : 'yi',
            'Yoruba' : 'yo',
            'Zulu' : 'zu',
            }

# Create your views here.
def translate(request, query,lang):

    # Initialize the translator
    translator = Translator()

    # Detect language
    text = query
    lang = lang_list[lang]
    detected = translator.detect(text)
    detected_language = detected.lang
    # out_lang = input("Which Language you'd like to translate: ")
    # lang = 'ar' #lang_list[out_lang.title()]
    # Translate text
    translated = translator.translate(text, dest=lang)
    return translated.text

def index(request):
    if request.method == "POST":
        try:
            text = request.POST.get('text','')
            lang = request.POST.get('language','')
            translated = translate(request,text,lang)
            translate_more = translate(request,"Translate More",lang)
            trans = translate(request,"Language Translator",lang)
            return render(request, 'translated.html',{
                'translate':translated,
                'lang_trans':trans,
                "translate_more":translate_more,
            })
        except:
            languages = list(lang_list.keys())
            return render(request,'index.html',{
            'languages':languages,
        })
    else:
        languages = list(lang_list.keys())
        return render(request,'index.html',{
            'languages':languages,
        })

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')