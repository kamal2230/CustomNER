# -*- coding: utf-8 -*-
"""Konjac NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QRFfD60grV2dlCQBVjcU5YCeJ8BoM97Q
"""

from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm 
import spacy
from spellchecker import SpellChecker
import re

"""## Training"""

nlp = spacy.load('en_core_web_md')

s1="Have this to use along with the lemongrass gel wash.. A very good quality konjac that holds product well on the surface. It does a great job of thoroughly cleansing, also being small & soft enough to get in the crevices around the nose. Don’t be put off as though it thoroughly cleans the exfoliation is super gentle & left my skin really soft, smooth but also energised."
s1=s1.lower()

s1.find("konjac")

s2="I've never used a konjac sponge before, so I wasn’t expecting much. How wrong was I- it gently exfoliates when I use a foaming face wash with it. I don't like face scrubs as they make my face sore & so use a liquid exfoliant but as they have aha's, o can’t use them the summer so will be using this instead!! A great find that left my skin soft & radiant!!"
s2=s2.lower()
s2.find("konjac")

s3="I was really impressed with the konjac sponge. It exfoliated my skin and made it feel fresher and cleaner without feeling dry or ‘stripped’."
s3=s3.lower()
s3.find("konjac")

s4="I use my konjac sponge with my lemongrass gel wash and it makes my face feel so clean and fresh, the shape of the sponge is perfect and it has a handy little string to hang it up which I loop over my fingers when using. I can see and feel how much my skin has been detoxed after washing. The sponge make the gel wash foam up lots too."
s4=s4.lower()
s4.find("konjac")

s5="I love Konjac sponges generally and this one is no different. It helps provide my skin with gentle but effective daily exfoliation"
s5=s5.lower()
s5.find("konjac")

s6="I've used a konjac sponge in the past but it contained charcoal and I found it quite drying on my combination skin, so I was interested to see how this one worked out. I've used it without cleanser and with, to judge its effects. I find that without cleanser and just using water, the sponge still somehow manages to remove makeup like magic and produces a bubbly feeling (I'm guessing something to do with all the air in those hundreds of little holes?!). However, I also love using this with a foaming cleanser as it becomes super foamy and bubbly. I do find I then have to rinse the sponge several times and repeatedly wash my face to remove the cleanser thoroughly, but after this I feel really deeply cleansed and refreshed. The little string attached goes right through the inside of the sponge and is super helpful in hanging it up to dry between uses. I would definitely recommend this natural, bubbly little sponge!"
s6=s6.lower()
s6.find("konjac")

s7="When the Konjac Sponge arrives, it is very hard (it reminded me of a pumice stone). After soaking it for a few minutes in warm water it expands and becomes very squidgy. I have been using this with a gel cleaner which I massage onto my face using my hands and then go over it with the sponge which absorbs a lot of the product making it easier to rinse my face. I have found this to be a nice addition to my skincare routine - especially when I don't want to use a flannel - but I wouldn't consider it a must-have tool. I would also say that I didn't find it to have much of an exfoliating effect on my skin."
s7=s7.lower()
s7.find("konjac")

s8="I have never used a konjac sponge, so I can't compare it other sponges.. but I didn't find it gave much exfoliation compared to my normal routine. This is something that is going to be dependent on your preferences, I like a harsh exfoliator both manual and chemical and while this only recommends to be use a few times a week - for me it is something I would use on the in between days my other products and not instead of."
s8=s8.lower()
s8.find("konjac")

s9="I really loved and like Garnier Organic Konjac Botanical Cleansing Sponge , it make my skin felt very clean and smooth after use it, you could hand it up in the shower it is great design! Definitely recommend this product."
s9=s9.lower()
s9.find("konjac")

s10="This is a good little sponge for everyday gentle cleansing-sometimes I use it with face wash, and sometimes just with water. It does smooth out my skin more than if I hadn't used it, but I can't see a difference in this to any other Konjac sponge on the market."
s10=s10.lower()
s10.find("konjac")

s11="I use the Konjac Sponge with the Garnier Lemongrass detox gel wash and double cleanse. I normally find that my skin is very sensitive when it comes to washing my face with sponges, muslin clothes, flannels etc. I didn't experience any sensitivity or redness when washing my face with the Konjac sponge at all, which is quite the rarity. I use the sponge twice in the morning as I double cleanse and dependent on my evening regime a further two times. The sponge is very gentle on the face, just be sure to soak the sponge to soften it prior to use first. I'll definitely have to pick up another sponge once it's time to replace my current one"
s11=s11.lower()
s11.find("konjac")

s12="Not having ever heard of a konjac sponge before, I was keen to try this new product! It's absolutely fantastic! After soaking as instructed I used this on my skin and did a great job of cleaning my skin and also gently exfoliating. I will undoubtedly continue to use this product."
s12=s12.lower()
s12.find("konjac")

s13="This was my first time using a konjac sponge and omg where have I been these are amazing they left my skin so soft and faded some Mark's from spots too I'm in love and will definitely be adding this to my beauty regime"
s13=s7.lower()
s13.find("konjac")

s14="This is the first time I have used Konjac Sponge and I am impressed with the results. It is gentle and non-abrasive on your skin making it smoother and shinier. It becomes soft after soaking and is very easy to use. It deeply cleanses and exfoliates dead skin making it radiant with a healthy glow."
s14=s14.lower()
s14.find("konjac")

s15="I have been using this Konjac root cleansing sponge, initially it felt a little rough but quickly softened up leaving my skin feeling nice and smooth. "
s15=s15.lower()
s15.find("konjac")

s16="I really enjoyed using this konjac sponge. I found it to be a fun addition to my usual cleansing routine. It works excellently to gently exfoliate my skin and help prevent break outs. I would definitely recommend."
s16=s16.lower()
s16.find("konjac")

s17="This easy to use polishing konjac sponge is great. It's a great way to cleanse my skin & my skin feels soft & looks glowing after use too."
s17=s17.lower()
s17.find("konjac")

s18="These are lovely natural Garnier konjac root fiber sponge. Great new way to cleanse face and body. The sponge is wonderful very soft and suitable for all skin types, you don't need anything just add water. Konjac sponge gives a natural skincare and very gently skin exfoliating. Leaves my skin feeling soft and clean. Great for removing makeup really does what it claims. Highly recommend"
s18=s18.lower()
s18.find("konjac")

s19="I was really excited to try out this based on the reviews that konjac sponges have been getting. I Love the lemongrass face wash so thought together these products would be amazing. I have to say I don’t see any better results from using the sponge too. It has only been a few days so perhaps I am judging too soon but I wouldn’t be in a rush to buy another when this is done."
s19=s19.lower()
s19.find("konjac")

s20="The Garnier Organic Konjac Sponge is quite possibly one of the best things I have used this year. It is made from 100% natural Konjac root which is known for its natural cleansing and exfoliating properties. It is easy to use simply wet the sponge under running water until it softens, squeezing out any excess water. I use the Garnier lemongrass detox with the Konjac sponge which leaves my skin feeling cleansed and smooth to the touch. Once you’re finished leave it somewhere to dry and use as often as you like."
s20=s20.lower()
s20.find("konjac")

TRAIN_DATA = [
    (s1, {
        'entities': [(74, 80, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
     (s2, {
        'entities': [(18, 24, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s3, {
        'entities': [(32, 38, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s4, {
        'entities': [(9, 15, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s5, {
        'entities': [(7, 13, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s6, {
        'entities': [(12, 18, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s7, {
        'entities': [(9, 15, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s8, {
        'entities': [(20, 26, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s9, {
        'entities': [(40, 46, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s10, {
        'entities': [(233, 239, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s11, {
        'entities': [(10, 16, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s12, {
        'entities': [(27, 33, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s13, {
        'entities': [(9, 15, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s14, {
        'entities': [(35, 41, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s15, {
        'entities': [(23, 29, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s16, {
        'entities': [(28, 34, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s17, {
        'entities': [(27, 33, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s18, {
        'entities': [(33, 39, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s19, {
        'entities': [(63, 69, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    }),
    (s10, {
        'entities': [(20, 26, 'Garnier Organic Konjac Botanical Cleansing Sponge')]
    })
]

model = None
output_dir=Path("C:\\Konjac NER")
n_iter=100

if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe('ner')

for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            nlp.update(
                [text],  
                [annotations],  
                drop=0.5,  
                sgd=optimizer,
                losses=losses)
        print(losses)

for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])

if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)

"""## Testing"""

print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)

test1="I never heard of a Konjac sponge before. So, when it’s dry it’s really crisp and hard but once it’s wet it feels just like a sponge even though it’s a completely natural product.. I used it with the lemongrass gel wash. The sponge felt really good on my skin. My face felt soft and smooth afterwards and there is even a small hanging thread so you can hang up the sponge to dry!"
doc = nlp2(test1.lower())
test1.lower().find("konjac")

print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])

test2="This little sponge is perfect for cleansing. It feels so natural on the face and was a perfect fit to hold and get into the tricky areas like the nose and around the eyes. I also used this with the Garnier Organic Fresh Lemongrass Detox Gel Wash, and it was a perfect combination. It felt like my face was getting an even deeper clean. Perfect little sponge to use morning or night to cleanse the face."
doc=nlp2(test2.lower())
test2.lower().find("konjac")

print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])

test3="First I was surprised by this sponge. I didn’t see why but I tried. So good, it is very soft and exfoliate my skin smoothly, I use it with the toner and it’s just perfect. My son is 16 and I noticed that he uses it as well."
doc=nlp2(test3.lower())
test3.lower().find("konjac")

print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])

test4="I've never used a sponge to wash my face before..or ever written a review about a skincare product!...but this has changed everything!! I love this so much! It has quite a rubbery feel to it but leaves my skin squeaky clean! In the shower so long now just washing my face with Konjac Sponge! Also used it to take face mask off :-)"
doc=nlp2(test4.lower())
test4.lower().find("konjac")

print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])

test4="I previously gave cleansed my skin with a facecloth/hot flannel but now I’m converted to using the sponge daily. My face feels super clean after use and it’s quite soft on the skin."
doc=nlp2(test4.lower())
test4.lower().find("konjac")

print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])