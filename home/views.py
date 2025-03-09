from django.shortcuts import render
from googletrans import Translator

# Language list with codes
lang_list = {
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy',
    'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs',
    'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese': 'zh-CN',
    'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en',
    'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr',
    'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el',
    'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hebrew': 'he', 'Hindi': 'hi',
    'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga',
    'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk',
    'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv',
    'Lithuanian': 'lt', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml',
    'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my',
    'Nepali': 'ne', 'Norwegian': 'no', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl',
    'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm',
    'Serbian': 'sr', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so',
    'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tamil': 'ta',
    'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz',
    'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu',
}

# Function to handle translation
def translate(text, lang):
    translator = Translator()
    lang_code = lang_list.get(lang, 'en')  # Default to English if language is not found
    translated = translator.translate(text, dest=lang_code)
    return translated.text

# Main view
def index(request):
    if request.method == "POST":
        try:
            text = request.POST.get('text', '')
            lang = request.POST.get('language', '')
            
            translated = translate(text, lang)
            translate_more = translate("Translate More", lang)
            trans = translate("Language Translator", lang)
            
            return render(request, 'translated.html', {
                'translate': translated,
                'lang_trans': trans,
                "translate_more": translate_more,
            })
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            languages = list(lang_list.keys())
            return render(request, 'index.html', {'languages': languages})
    else:
        languages = list(lang_list.keys())
        return render(request, 'index.html', {'languages': languages})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')