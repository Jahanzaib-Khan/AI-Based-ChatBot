import nltk
import pyttsx3
import speech_recognition as sr
from nltk.stem import WordNetLemmatizer
from word2number import w2n
from num2words import num2words 


def extract(text):

    ii = ee = 0

    def token(text):
        text = text.lower()
        from nltk.tokenize import sent_tokenize, word_tokenize
        # nltk.download('punkt')
        words = word_tokenize(text)
        return (words)

    def remove_p(words):
        words = [word for word in words if word.isalnum()]
        return (words)

    def remove_uw(words):
        # nltk.download('stopwords')
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        filtered_words = []
        for i in words:
            if i not in stop_words:
                filtered_words.append(i)
        return (filtered_words)

    def stemming(words):
        ws = []
        lem=WordNetLemmatizer()
        for i in words:
            ws.append(lem.lemmatize(i,pos='v'))
        return (ws)
    
    words = token(text)
    words = remove_p(words)
    words = remove_uw(words)
    words = stemming(words)

    intents = ["order", "reserve", "menu", 'buy', "purchase", "take", 'get', 'checkout', 'cart', 'price', 'cost']
    enitities = ['pizza', 'burger', 'sandwich', 'drink', 'pepsi', '7up', 'mirinda',"messi meat burger", "creamy pizza",
    ]

    intentsInMsg = []
    entitiesInMsg = []
    quantities = []

    for w in words:
        for i in enitities:
            if w == i:
                # print("Entity: ", w)
                ee = 1
                entitiesInMsg.append(w)

    for w in words:
        for i in intents:
            if w == i:
                # print("Intent: ", w)
                ii = 1
                intentsInMsg.append(w)
    

    # def quantity_finder(entitiesInMsg):
    #     numbers=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty","hundred","thousand"]
    #     nums=""
    #     for u_entity in entitiesInMsg:
    #         for num in numbers:
    #             if num==u_entity:
    #                 nums=nums+u_entity
    #                 nums=nums+" "
    #                 print(nums)
    #                 nums= w2n.word_to_num(nums)
    #                 quantities.append(nums)


    def finder(items,u_entities):
        numbers=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty","hundred","thousand"]
        nums=""
        quantity=[]
        u_items=[]
        temp_items=[]
        quantity_elements=[]  
        for entity in u_entities:
            if entity.isnumeric()==True:
                entity=num2words(entity)

            for item in items:
                if entity==item:
                    temp_items.append(entity)
                    #print(temp_items)      
                if entity not in items and entity not in quantity_elements:
                    quantity_elements.append(entity)      
                if len(temp_items)>0:
                    a=temp_items[0]
                    #print(a)
                    u_items.append(a)
                    temp_items = []
            for u_entity in quantity_elements:
                        for num in numbers:
                            if num==u_entity:
                                nums=u_entity
                            #nums=nums+" " 
                            #print(nums)
                                if nums != "":
                                    nums=w2n.word_to_num(nums)
                                    quantity.append(nums)
                                    #print(quantity)
                                    temp_items=[]
                                nums=''
            # if len(quantity_elements) > 0:
            #     for i in quantity_elements:
            #         num = w2n.word_to_num(i)
            #         quantity.append(num)
        return(u_items,quantity)

    finalEntities,quantities = finder(enitities,words)

    # if ii == 0 and ee == 0:
    if len(finalEntities)<1 and len(quantities)< 1:
        # print("\nBot: Sorry I didn't understand your intent")
        return ("Sorry I couldnt understand you, You can try rephrasing your words ")

    else:
        return ({"intents":intentsInMsg,"entities":finalEntities, "quantities": quantities})



