# -*- coding: utf-8 -*-
"""bb cream NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qV4dspx3FhJe_osVuGbdfOS6bLRuKrEB

### Load the package
"""

!pip install spellchecker

from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm 
import spacy
from spellchecker import SpellChecker
import re

"""### Create a model"""

nlp = spacy.load('en_core_web_md')

"""### Training Input"""

s1="1.I absolutely love this BB cream. I have repurchased multiple bottles over the years. It’s a lovely formula which easily blends into the skin. It has a medium coverage and mattifies the skin. My skin looks good all day with this product and it improves my skins condition with use also! Great bonus that it has SPF 20. I have knocked a star off as the shade “light” must have recently been changed as it’s now too dark for my skin tone. I would say it’s more of a medium shade which is a shame."
s1=s1.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s1)
print(matches.start(),matches.end())

s2="2.I always use the garnier bb cream medium but the last one I bought the box and tube had changed. It’s much darker as well. Think might have to go lighter."
s2=s2.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s2)
print(matches.start(),matches.end())

s3="3.I picked this up today because it was on sale and was extremely disappointed. I have pale skin and the BB cream just looked straight up orange on me. Not at all what I was expecting given it's called light. It also goes on very streaky and patchy and has a very strong fragrance. Needless to say, I couldn't even leave the house with it on and removed it straight away, so I can't attest to the product's longevity. Worst base product I've ever tried."
s3=s3.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s3)
print(matches.start(),matches.end())

s4="4.I have bought several bb creams over the years and always been disappointed so wasn't expecting much from this. It does everything it promises, and I absolutely love it. I don't like wearing heavy makeup but don't have the best skin and this gives the perfect amount of coverage. Unlike many products that promise to mattify this actually does without drying out my skin and gives a lovely glow. A little goes a long way so I can tell this is going to last for ages. I have never felt so confident in how my skin looks and I will not be changing from this cream! Outperforms much more expensive formulas I've tried, absolute winner for me."
s4=s4.lower()
s2.find("bb cream")

s5="5.this is my first time using a bb cream and honestly it’s great! i have slightly oily/combination skin and it mattifies my skin, but almost too much it looks quite dry. It evens my skin tone really really well as i have quite red face and it covers it well! Also, I’ve found that when applying with a damp beauty blender it becomes a tad patchy due to the water, but it blends really easily! I could only find the shades light and medium and being a fair/warm toned , blonde/brown hair, I’ve found that even the light shade hasn’t an orange undertone. I usually brighten it with a concealer, but it adds to the dryness."
s5=s5.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s5)
print(matches.start(),matches.end())

s6="6.My absolute favourite foundation/BB Cream! I have been using this for 3 years and have never strayed! It is the perfect natural base for your face - applied with a beauty blender gives a flawless look without being heavy and stays on all day with a primer and a bit of setting powder, light contour and blusher also sit nicely on top. It has a medium buildable coverage, honestly feel like it covers better than any other drugstore foundation I’ve used! Only negative is the shade range, however I have shades light and medium and mix them accordingly throughout the year to get my perfect colour! My skin has also improved since using this as it is non-clogging and has plenty of skin benefits, so you don't need to feel guilty about wearing it every day. The tube also lasts for ages (9+ months). Definitely recommend for oily/combination/blemish prone skin."
s6=s6.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s6)
print(matches.start(),matches.end())

s7="7.I switched a few months ago from the original garner BB cream to this version as my T-zone seems to have decided to be greasy and I was getting a few break-outs. This gives just enough coverage to tone down my red cheeks a bit but without looking like I have too heavy a face of make up on. Easy to use (and easy to remove at the end of the day) this has earned a permanent spot in my makeup bag!"
s7=s7.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s7)
print(matches.start(),matches.end())

s8="8.Have been using this product for several weeks now and I love it. 47yrs old and was looking for something lighter for the summer and thought I would try a BB cream. I can't rate this product highly enough, I tend to use pricey foundation just because of my age and I don't have great skin but this BB cream gives me an even better finish, goes on smoothly, doesn't settle in lines (I do use a primer tho) last's all day with no shine and I just love the finish it gives. Don't be put off by the way it looks when first applied it's one of these products that takes about 10-15mins to settle but perfect after that. Buy it!"
s8=s8.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s8)
print(matches.start(),matches.end())

s9="9.I bought this two days ago and I have used it twice and I am so, so pleased with it. I have combination skin but not many bb creams that are made for this skin type work very well - either they make me really oily or dry certain areas out. But this is perfect for me! I got it in medium even though I'm quite pale and it's wonderful. Doesn't dry my skin out or make my T-zone excessively oily like others. It gives a lovely, natural, even coverage and I have already had one compliment on my skin with using it. Because it is a bb cream it doesn't cover blemishes, so have a concealer at hand, but for a light, even coverage (gets rid of my redness) definitely give it a try!!!"
s9=s9.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s9)
print(matches.start(),matches.end())

s10="10.Like many people I am constantly on the hunt for the perfect base. I spent years wearing really heavy foundation every day and now being 25 I want to look after my skin more and embrace being a little more natural. So, I was on the hunt for lighter coverage foundation/base. On a bit of a whim I bought this as its oil free and I get quite oily. I was sceptical as it's a bb cream and I thought that would be too light coverage to be honest. But it's amazing. I literally couldn't believe how nice my skin looked when I put this on. Even my boyfriend commented on it. It's a runny texture and I use a buffing brush to put it on and it's so quick and easy. It's not thick but it has good coverage. Definitely build-able and actually has a lot more coverage than expected. If you just want a tinted moisturiser type product I wouldn't say this is that, it's a little more coverage than that (which I love). It's a really good middle ground for me as not wearing a base isn't an option for me sadly. My only one negative is that it does rub off my nose quite easily as that's where I am most oily. I would like it to be a little more long lasting but honestly I'm okay with it because it makes me skin feel like it can breathe and I love the overall look far more than a thick foundation which also always rubs off my nose but looks worse! I just use the remains of the product on the brush to top up in the day and that's enough!"
s10=s10.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s10)
print(matches.start(),matches.end())

s11="11.I usually use the Maybelline bb cream, but I decided to get this one instead. great coverage and it actually reduced my acne. would recommend it"
s11=s11.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s11)
print(matches.start(),matches.end())

s12="12.I love this BB cream for combination skin, but with my pale complexion it only really suits me when I've got a tan (which just doesn't happen that often when you live in the UK!). Please introduce the extra light shade for this one as well!"
s12=s12.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s12)
print(matches.start(),matches.end())

s13="13.This product does what it says on the box to be fair, it does make your skin that little bit better without having to trowel foundation all over your face."
s13=s13.lower()
s13.find("bb cream")

s14="14.It does control oil for about 4 hours, after which I find I have to remove my oil with blotting papers and then use Rimmel Stay Matte to take a bit of the shine off my face."
s14=s14.lower()
s14.find("bb cream")

s15="15.What I'm really disappointed with is the colour. This product is, unusually, on the yellow toned side, which normally complements my neutral undertones a lot better than standard pink based BB creams, but it's about 3 shades too dark for me, and there are no lighter shades than this available. I look like I've been tangoed when I wear it, and there's no way of blending it in around my chin line. As your face gets more oily, the colour does lighten up to complement your natural skin, but this can take all morning, and then by lunchtime, when it looks a normal colour, your face has become oily, so you feel like taking it off and reapplying. All of that hassle, and it doesn't completely hide your blemishes because it's only a BB cream anyway.... I'd rather get out a trusty foundation :( And I really wanted to make this work for me, as on the box it seemed too good to be true."
s15=s15.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s15)
print(matches.start(),matches.end())

s16="16.I thought that a BB Cream specifically for combination skin would work miracles. I am sad to say that it didn't. The colour of the product is good as my skin is quite tanned and the coverage was reasonable. However, this is where the good points end. The product is extremely runny so is messy to apply and it's difficult to keep a clean make up bag with this in it. It also transfers very easily from your face to your hands throughout the day, so pretty much everything I handled would end up with the product clinging to it. I have typical combination skin, but this product seems to have aggravated the worst traits. It clings to dry patches, and has created more patches where I wouldn't normally get dry skin e.g. around my nose and between my eyebrows. I have also experienced a lot more breakouts of spots than normal. The spots have been awful. They are big, angry and very sore and whereas if I don't touch or squeeze spots they will usually disappear on their own after a couple of days, when using this they lasted much longer and instead of covering the problem this product just seemed to make things much worse. It has also done nothing to prevent shine as my skin looked oily after just a couple of hours. I've given up on this BB Cream after less than a month and have had to go completely make up free for the past week to give my skin chance to calm down. I'm sure that this product suits lots of people but if you have combination skin that is also quite sensitive my advice would be to avoid it at all costs."
s16=s16.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s16)
print(matches.start(),matches.end())

s17="17.I've tried loads of BB creams trying to find one that actually works and does what it says! Every other one I've found says light but is actually orange. This Garnier one is actually a light colour! Yellow undertones so perfect for me. Great coverage for a BB cream, I'd even say better than some foundation's I've had in the past. And...... It's matte!!! No shine and no stickiness! The only thing I don't like about it is that the box says to apply it like you would a moisturiser. I'd advise to use a brush, it's a little bit hard to blend around the edges of your face and I find fingers make the cheeks look blotchy."
s17=s17.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s17)
print(matches.start(),matches.end())

s18="18.Quite disappointing, it doesn't blend well, it leaves my face looking waxy and orange and it makes my foundation look weird. Definitely not a good buy. I tried a little trick since I didn't want this to go to waste. I mixed some of my foundation in a little pot along with some of this BB cream and once applied, it looked a little better than on it's own, but still, If you are thinking about buying it, think twice. I wouldn't recommend it."
s18=s18.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s18)
print(matches.start(),matches.end())

s19="19.I normally use my Loreal True Match foundation every day, but it's safe to say I'll be switching to this! It has the same coverage as a foundation and evens out skin tone, but it feels just like skin on your face as if nothing's there! It hardly ever creases and lasts hours without fading away! Sometimes redness can show through after a few hours but if you use a good concealer there'll be no problem! I have normal skin but I'm oily in my t-zone, so this bb cream is perfect as it stays matte all day, and even longer if you use some powder"
s19=s19.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s19)
print(matches.start(),matches.end())

s20="20.I've bought this bb cream several times as I love the dewy finish it gives me. The coverage isn't brilliant, but I use concealer too. Unfortunately, I'm looking for another bb cream next time though as I'm sick of it leaking all over my makeup bag. I'm not sure why it does that, I can only assume it's the screw top lid. If Garnier change it for a pump applicator I might consider buying it again."
s20=s20.lower()
s=r"\b(bb cream)\b"
matches = re.search(s, s20)
print(matches.start(),matches.end())

"""### Training Data"""

TRAIN_DATA = [
    (s1, {
        'entities': [(25, 33, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
     (s2, {
        'entities': [(27, 35, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s3, {
        'entities': [(105, 113, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s4, {
        'entities': [(27, 35, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s5, {
        'entities': [(32, 40, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s6, {
        'entities': [(35, 43, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s7, {
        'entities': [(55, 63, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s8, {
        'entities': [(157, 165, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s9, {
        'entities': [(530, 538, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s10, {
        'entities': [(375, 383, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s11, {
        'entities': [(32, 40, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s12, {
        'entities': [(15, 23, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s13, {
        'entities': []
    }),
    (s14, {
        'entities': []
    }),
    (s15, {
        'entities': [(736, 744, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s16, {
        'entities': [(20, 28, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s17, {
        'entities': [(260, 268, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s18, {
        'entities': [(289, 297, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s19, {
        'entities': [(462, 470, 'Garnier BB Cream Miracle Skin Perfector')]
    }),
    (s20, {
        'entities': [(20, 28, 'Garnier BB Cream Miracle Skin Perfector')]
    })
]

"""### Define our variables"""

model = None
output_dir=Path("C:\\BB Cream NER")
n_iter=100

"""### Load the model"""

if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")

"""### Set-up the NER pipeline"""

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe('ner')

"""### Train the recognizer"""

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

"""### Test the trained model"""

for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])

"""### Save the Model"""

if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)

"""### Testing the saved model"""

nlp2=spacy.load(output_dir)

def find(s):
    doc = nlp2(s.lower())
    res=s.lower().find("bb cream")
    if(res>0):
        print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])
    else:
        print("Unable to identify the Product from the review!")
s="1.Having used a BB cream by a different brand I had to change as it was making my skin so shiny and greasy looking within hours of application. This one by Garnier is fab! It definitely blurs blemishes I have and makes my skin look healthy without using heavy foundation. It blends really easily into my skin and is my go to product every day for natural looking perfected skin."
find(s)

def find(s):
    doc = nlp2(s.lower())
    res=[(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents]
    if(len(res)>0):
        print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])
    else:
        print("Unable to identify the Product from the review!")
s="2.This bb cream is amazeballs I've always wanted to buy the Revlon photo ready bb cream but heard that it's very light coverage so I bought this one and never looked back. I first started using it with fingers but found it better to use with the real techniques expert face brush as it looked flawless and the coverage was just perfect. The finish of it is matte which is good as I'm an oily skin gal and the coverage is beautiful and not too heavy so definitely one to invest in, and an amazing price."
find(s)

def find(s):
    doc = nlp2(s.lower())
    res=s.lower().find("bb cream")
    if(res>0):
        print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])
    else:
        print("Unable to identify the Product from the review!")
s="3.I have used the original of this product but didn't like it at all! This version is fantastic it covers as well as a foundation and makes your skin look flawless!"
find(s)

def find(s):
    doc = nlp2(s.lower())
    res=s.lower().find("bb cream")
    if(res>0):
        print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])
    else:
        print("Unable to identify the Product from the review!")
s="4.I really wanted to like this product; however, it was not as promised. I have oily skin and when applied the product made my skin seem oilier and even more shine. The packaging is poor meaning the cream goes everywhere. It does have a nice colour when first out on but that is the only advantage. "
find(s)

def find(s):
    doc = nlp2(s.lower())
    res=s.lower().find("bb cream")
    if(res>0):
        print('Entities', [(ent.text, ent.label_,ent.start_char,ent.end_char) for ent in doc.ents])
    else:
        print("Unable to identify the Product from the review!")
s="5.Bought this today and wanted to try it out straight away. It is sooooooo light on the skin and after about 5 mins it doesn't even feel like your wearing foundation! I have dry and oily skin but you couldn't tell when wearing this. It's coverage is amazing even with the tiniest amount. Will definatly be buying this again!!! Very happy! :D"
find(s)

