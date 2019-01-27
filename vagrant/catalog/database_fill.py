# this code is modeled afer "lotsofmenus.py" frpm the REstaurant Menu app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Instrument

# connect to the database
engine = create_engine('sqlite:///orchestra.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


####################### Woodwind Category ############################

category1 = Category(name='Woodwinds',
	description='Woodwind instruments are a family of musical instruments within the more general category of wind instruments. There are two main types of woodwind instruments: flutes and reed instruments (otherwise called reed pipes). What differentiates these instruments from other wind instruments is the way in which they produce their sound.All woodwinds produce sound by splitting an exhaled air stream on a sharp edge, such as a reed or a fipple. A woodwind may be made of any material, not just wood. Common examples include brass, silver, cane, as well as other metals such as gold and platinum. Occasionally woodwinds are made out of earthen materials, especially ocarinas. Common examples include flute, oboe, clarinet, bassoon, and saxophone.')
session.add(category1)
session.commit()

instrument1 = Instrument(name='Piccolo',
	description='The piccolo is a half-size flute, and a member of the woodwind family of musical instruments. The modern piccolo has most of the same fingerings as its larger sibling, the standard transverse flute, but the sound it produces is an octave higher than written. This gave rise to the name ottavino (Italian for "little octave"), which the instrument is called in the scores of Italian composers. It is also called flauto piccolo or flautino, Vivaldi making use of the latter term. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/0/0c/Yamaha_Piccolo_YPC-81.png',
	picture_attr='Yamaha Corporation [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons')
session.add(instrument1)
session.commit()

instrument2 = Instrument(name='Flute',
	description='The flute is a family of musical instruments in the woodwind group. Unlike woodwind instruments with reeds, a flute is an aerophone or reedless wind instrument that produces its sound from the flow of air across an opening. According to the instrument classification of Hornbostel Sachs, flutes are categorized as edge-blown aerophones. A musician who plays the flute can be referred to as a flute player, flautist, flutist or, less commonly, fluter or flutenist. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/e/ef/Western_concert_flute.png',
	picture_attr='https://upload.wikimedia.org/wikipedia/commons/e/ef/Western_concert_flute.png')
session.add(instrument2)
session.commit()

instrument3 = Instrument(name='Oboe',
	description='Oboes are a family of double reed woodwind instruments. The most common oboe plays in the treble or soprano range. Oboes are usually made of wood, but there are also oboes made of synthetic materials. A soprano oboe measures roughly 65 cm (25 1/2 in) long, with metal keys, a conical bore and a flared bell. Sound is produced by blowing into the reed at a sufficient air pressure, causing it to vibrate with the air column. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/4/4f/Oboe_modern.jpg',
	picture_attr='Hustvedt [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons')
session.add(instrument3)
session.commit()

instrument4 = Instrument(name='English Horn',
	description='The cor anglais, or English horn in North America, is a double-reed woodwind instrument in the oboe family. It is approximately one and a half times the length of an oboe. The cor anglais is a transposing instrument pitched in F, a perfect fifth lower than the oboe (a C instrument). This means that music for the cor anglais is written a perfect fifth higher than the instrument actually sounds. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/8/80/English_Horn_picture.jpg',
	picture_attr='Hustvedt [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) or GFDL (http://www.gnu.org/copyleft/fdl.html)], from Wikimedia Commons')
session.add(instrument4)
session.commit()

instrument5 = Instrument(name='Clarinet',
	description='The clarinet is a musical-instrument family belonging to the group known as the woodwind instruments. It has a single-reed mouthpiece, a straight cylindrical tube with an almost cylindrical bore, and a flared bell. A person who plays a clarinet is called a clarinetist (sometimes spelled clarinettist). [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/0/0d/Yamaha_Clarinet_YCL-457II-22.png',
	picture_attr='Yamaha Clarinet YCL-457II-22.tiff: Yamaha Corporation;remove backround: Habitator terrae (https://commons.wikimedia.org/wiki/User:Habitator_terrae) [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons')
session.add(instrument5)
session.commit()

instrument6 = Instrument(name='Bass Clarinet',
	description='The bass clarinet is a musical instrument of the clarinet family. Like the more common soprano Bb clarinet, it is usually pitched in Bb (meaning it is a transposing instrument on which a written C sounds as Bb), but it plays notes an octave below the soprano Bb clarinet. Bass clarinets in other keys, notably C and A, also exist, but are very rare (in contrast to the regular A clarinet, which is quite common in classical music). Bass clarinets regularly perform in orchestras, wind ensembles/concert bands, occasionally in marching bands, and play an occasional solo role in contemporary music and jazz in particular. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/3/39/Yamaha_Bass_Clarinet_YCL-622II.jpg',
	picture_attr='Yamaha Corporation [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons')
session.add(instrument6)
session.commit()

instrument7 = Instrument(name='Bassoon',
	description='The bassoon is a woodwind instrument in the double-reed family that typically plays music written in the bass and tenor clefs, and occasionally the treble. Appearing in its modern form in the 19th century, the bassoon figures prominently in orchestral, concert band, and chamber music literature. The bassoon is a non-transposing instrument known for its distinctive tone colour, wide range, variety of character and agility. Someone who plays the bassoon is called a bassoonist. [wikipedia.org]',
	category_id=category1.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/6/6f/FoxBassoon.png',
	picture_attr='Gregory F. Maxwell <gmaxwell@gmail.com> PGP:0xB0413BFA [GFDL 1.2 (http://www.gnu.org/licenses/old-licenses/fdl-1.2.html)], via Wikimedia Commons')
session.add(instrument7)
session.commit()


####################### Brass Category ############################

category2 = Category(name='Brass',
	description='A brass instrument is a musical instrument that produces sound by sympathetic vibration of air in a tubular resonator in sympathy with the vibration of the lips. Brass instruments are also called labrosones, literally meaning "lip-vibrated instruments". There are several factors involved in producing different pitches on a brass instrument. Slides, valves, crooks (though they are rarely used today), or keys are used to change vibratory length of tubing, thus changing the available harmonic series, while the embouchure, lip tension and air flow serve to select the specific harmonic produced from the available series. The view of most scholars is that the term "brass instrument" should be defined by the way the sound is made, as above, and not by whether the instrument is actually made of brass. Thus one finds brass instruments made of wood, like the alphorn, the cornett, the serpent and the didgeridoo, while some woodwind instruments are made of brass, like the saxophone.')
session.add(category2)
session.commit()

instrument11 = Instrument(name='Horn',
	description='The French horn (since the 1930s known simply as the "horn" in most professional music circles) is a brass instrument made of tubing wrapped into a coil with a flared bell. The double horn in F/Bb (technically a variety of German horn) is the horn most often used by players in professional orchestras and bands. A musician who plays a French horn is known as a horn player or hornist. [wikipedia.org]',
	category_id=category2.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/6/63/French_horn_front.png',
	picture_attr='BenP [CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons')
session.add(instrument11)
session.commit()

instrument12 = Instrument(name='Trumpet',
	description='A trumpet is a brass instrument commonly used in classical and jazz ensembles. The trumpet group contains the instruments with the highest register in the brass family. Trumpet-like instruments have historically been used as signaling devices in battle or hunting, with examples dating back to at least 1500 BC; they began to be used as musical instruments only in the late 14th or early 15th century. Trumpets are used in art music styles, for instance in orchestras, concert bands, and jazz ensembles, as well as in popular music. [wikipedia.org]',
	category_id=category2.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/3/30/Trumpet_1.png',
	picture_attr='PJ, background cropped by EWikist [CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons')
session.add(instrument12)
session.commit()

instrument13 = Instrument(name='Trombone',
	description='The trombone is a musical instrument in the brass family. As on all brass instruments, sound is produced when the vibrating lips (embouchure) of the player cause the air column inside the instrument to vibrate. Nearly all trombones have a telescoping slide mechanism that varies the length of the instrument to change the pitch. Many modern trombone models also use a valve attachment to lower the pitch of the instrument. Variants such as the valve trombone and superbone have three valves similar to those on the trumpet. [wikipedia.org]',
	category_id=category2.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/6/6d/Posaune.jpg',
	picture_attr='w:user:Esolomon [Copyrighted free use], via Wikimedia Commons')
session.add(instrument13)
session.commit()

instrument14 = Instrument(name='Tuba',
	description='The tuba is the largest and lowest-pitched musical instrument in the brass family. As with all brass instruments, the sound is produced by lip vibration into a large mouthpiece. It first appeared in the mid-19th century, making it one of the newer instruments in the modern orchestra and concert band. The tuba largely replaced the ophicleide. In America, a person who plays the tuba is known as a tubaist or tubist. In the United Kingdom, a person who plays the tuba in an orchestra is known simply as a tuba player; in a brass band or military band, they are known as bass players. [wikipedia.org]',
	category_id=category2.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/d/d7/Riverside_Stompers_-_Martin_Stanzel_solo_-_Dieter_Bietak_2007.jpg',
	picture_attr='I, I.R. Annie IP. [CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)]')
session.add(instrument14)
session.commit()


####################### Strings Category ############################

category3 = Category(name='Strings',
	description='String instruments, stringed instruments, or chordophones are musical instruments that produce sound from vibrating strings when the performer plays or sounds the strings in some manner. Musicians play some string instruments by plucking the strings with their fingers or a plectrum -- and others by hitting the strings with a light wooden hammer or by rubbing the strings with a bow. In some keyboard instruments, such as the harpsichord, the musician presses a key that plucks the string. With bowed instruments, the player rubs the strings with a horsehair bow, causing them to vibrate. With a hurdy-gurdy, the musician operates a mechanical wheel that rubs the strings.')
session.add(category3)
session.commit()

instrument21 = Instrument(name='Violin',
	description='The violin, also known informally as a fiddle, is a wooden string instrument in the violin family. Most violins have a hollow wooden body. It is the smallest and highest-pitched instrument in the family in regular use. Smaller violin-type instruments exist, including the violino piccolo and the kit violin, but these are virtually unused. The violin typically has four strings tuned in perfect fifths, and is most commonly played by drawing a bow across its strings, though it can also be played by plucking the strings with the fingers (pizzicato) and by striking the strings with the wooden side of the bow (col legno). [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/1/1b/Violin_VL100.png',
	picture_attr='Just plain Bill [CC0], via Wikimedia Commons')
session.add(instrument21)
session.commit()

instrument22 = Instrument(name='Viola',
	description='The viola is a string instrument that is bowed or played with varying techniques. It is slightly larger than a violin and has a lower and deeper sound. Since the 18th century, it has been the middle or alto voice of the violin family, between the violin (which is tuned a perfect fifth above) and the cello (which is tuned an octave below). The strings from low to high are typically tuned to C3, G3, D4, and A4. In the past, the viola varied in size and style, as did its names. The word viola originates from Italian. The Italians often used the term: "viola da braccio" meaning literally: "of the arm". "Brazzo" was another Italian word for the viola, which the Germans adopted as Bratsche. The French had their own names: cinquiesme was a small viola, haute contre was a large viola, and taile was a tenor. Today, the French use the term alto, a reference to its range. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/c/cd/Bratsche.jpg',
	picture_attr='Just plain Bill [Public domain], from Wikimedia Commons')
session.add(instrument22)
session.commit()

instrument23 = Instrument(name='Cello',
	description='The cello (plural cellos or celli) or violoncello is a string instrument. It is played by bowing or plucking its four strings, which are usually tuned in perfect fifths an octave lower than the viola: from low to high, C2, G2, D3 and A3. It is the bass member of the violin family, which also includes the violin, viola and the double bass, which doubles the bass line an octave lower than the cello in much of the orchestral repertoire. After the double bass, it is the second-largest and second lowest (in pitch) bowed string instrument in the modern symphony orchestra. The cello is used as a solo instrument, as well as in chamber music ensembles (e.g., string quartet), string orchestras, as a member of the string section of symphony orchestras, most modern Chinese orchestras, and some types of rock bands. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/5/5f/Cello_front_side.png',
	picture_attr='Georg Feitscher [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY 3.0 (https://creativecommons.org/licenses')
session.add(instrument23)
session.commit()

instrument24 = Instrument(name='Double Bass',
	description='The double bass, or simply the bass (and numerous other names), is the largest and lowest-pitched bowed string instrument in the modern symphony orchestra. It is a standard member of the string section, as well as the concert band, and is featured in concertos, solo and chamber music in Western classical music. the bass is used in a range of other genres, such as jazz, 1950s-style blues and rock and roll, rockabilly, psychobilly, traditional country music, bluegrass, tango and many types of folk music. The bass is a transposing instrument and is typically notated one octave higher than tuned to avoid excessive ledger lines below the staff. The double bass is the only modern bowed string instrument that is tuned in fourths (like a viol), rather than fifths, with strings usually tuned to E1, A1, D2 and G2. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/d/d3/AGK_bass1_full.jpg',
	picture_attr='User:AndrewKepert [CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)], via Wikimedia Commons')
session.add(instrument24)
session.commit()

instrument25 = Instrument(name='Piano',
	description='The piano is an acoustic, stringed musical instrument invented in Italy by Bartolomeo Cristofori around the year 1700 (the exact year is uncertain), in which the strings are struck by hammers. It is played using a keyboard, which is a row of keys (small levers) that the performer presses down or strikes with the fingers and thumbs of both hands to cause the hammers to strike the strings. The word piano is a shortened form of pianoforte, the Italian term for the early 1700s versions of the instrument, which in turn derives from gravicembalo col piano e forte and fortepiano. The Italian musical terms piano and forte indicate "soft" and "loud" respectively, in this context referring to the variations in volume (i.e., loudness) produced in response to a touch or pressure on the keys: the greater the velocity of a key press, the greater the force of the hammer hitting the strings, and the louder the sound of the note produced. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/c/c8/Grand_piano_and_upright_piano.jpg',
	picture_attr='User:Gryffindor and User:Megodenas [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons')
session.add(instrument25)
session.commit()

instrument26 = Instrument(name='Celeste',
	description='The celesta or celeste is a struck idiophone operated by a keyboard. It looks similar to an upright piano (four- or five-octave), albeit with smaller keys and a much smaller cabinet, or a large wooden music box (three-octave). The keys connect to hammers that strike a graduated set of metal (usually steel) plates or bars suspended over wooden resonators. Four- or five-octave models usually have a damper pedal that sustains or damps the sound. The three-octave instruments do not have a pedal because of their small "table-top" design. One of the best-known works that uses the celesta is "Dance of the Sugar Plum Fairy" from The Nutcracker. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/4/46/Celesta_Schiedmayer_Studio.jpg',
	picture_attr='Schiedmayer Celesta GmbH [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons')
session.add(instrument26)
session.commit()

instrument27 = Instrument(name='Harp',
	description='The harp is a stringed musical instrument that has a number of individual strings running at an angle to its soundboard; the strings are plucked with the fingers. Harps have been known since antiquity in Asia, Africa and Europe, dating back at least as early as 3500 BC. The instrument had great popularity in Europe during the Middle Ages and Renaissance, where it evolved into a wide range of variants with new technologies, and was disseminated to the colonies, finding particular popularity in Latin America. Although some ancient members of the harp family died out in the Near East and South Asia, descendants of early harps are still played in Myanmar and parts of Africa, and other defunct variants in Europe and Asia have been utilized by musicians in the modern era. [wikipedia.org]',
	category_id=category3.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/9/94/Harp.svg',
	picture_attr='Martin Kraft [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], from Wikimedia Commons')
session.add(instrument27)
session.commit()

####################### Precussion Category ############################

category4 = Category(name='Percussion',
	description='A percussion instrument is a musical instrument that is sounded by being struck or scraped by a beater (including attached or enclosed beaters or rattles); struck, scraped or rubbed by hand; or struck against another similar instrument. The percussion family is believed to include the oldest musical instruments, following the human voice. The percussion section of an orchestra most commonly contains instruments such as timpani, snare drum, bass drum, cymbals, triangle and tambourine. However, the section can also contain non-percussive instruments, such as whistles and sirens, or a blown conch shell. Percussive techniques can also be applied to the human body, as in body percussion. On the other hand, keyboard instruments, such as the celesta, are not normally part of the percussion section, but keyboard percussion instruments such as the glockenspiel and xylophone (which do not have piano keyboards) are included. Percussion instruments are most commonly divided into two classes: Pitched percussion instruments, which produce notes with an identifiable pitch, and unpitched percussion instruments, which produce notes or sounds without an identifiable pitch.')
session.add(category4)
session.commit()

instrument31 = Instrument(name='Timpani',
	description='Timpani or kettledrums (also informally called timps) are musical instruments in the percussion family. A type of drum, they consist of a membrane called a head stretched over a large bowl traditionally made of copper. Most modern timpani are pedal timpani and can be tuned quickly and accurately to specific pitches by skilled players through the use of a movable foot-pedal. They are played by striking the head with a specialized drum stick called a timpani stick or timpani mallet. Timpani evolved from military drums to become a staple of the classical orchestra by the last third of the 18th century. Today, they are used in many types of ensembles, including concert bands, marching bands, orchestras, and even in some rock bands. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/0/02/USAFE_Band_timpanist.jpg',
	picture_attr='See page for author [Public domain], via Wikimedia Commons')
session.add(instrument31)
session.commit()

instrument32 = Instrument(name='Bass Drum',
	description='A bass drum, or kick drum, is a large drum that produces a note of low definite or indefinite pitch. Bass drums are percussion instruments and vary in size and are used in several musical genres. Three major types of bass drums can be distinguished. The type usually seen or heard in orchestral, ensemble or concert band music is the orchestral, or concert bass drum (in Italian: gran cassa, gran tamburo). It is the largest drum of the orchestra. The kick drum, a term for a bass drum associated with a drum kit. It is struck with a beater attached to a pedal, usually seen on drum kits. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/9/92/Mounted_concert_bass_drum.jpg',
	picture_attr='Yooperz [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons')
session.add(instrument32)
session.commit()

instrument33 = Instrument(name='Snare Drum',
	description='A snare drum or side drum is a percussion instrument that produces a sharp staccato sound when the head is struck with a drum stick, due to the use of a series of stiff wires held under tension against the lower skin. Snare drums are often used in orchestras, concert bands, marching bands, parades, drumlines, drum corps, and more. It is one of the central pieces in a drum set, a collection of percussion instruments designed to be played by a seated drummer, which is used in many genres of music. Snare drums are usually played with drum sticks, but other beaters such as the brush or the rute can be used to achieve very different sounds. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/4/46/2006-07-06_snare_14.jpg',
	picture_attr='Stephan Czuratis (Jazz-face) [CC BY-SA 2.5 (https://creativecommons.org/licenses/by-sa/2.5)], from Wikimedia Commons')
session.add(instrument33)
session.commit()

instrument34 = Instrument(name='Claves',
	description='Claves are a percussion instrument, consisting of a pair of short (about 20-30 cm), thick dowels. Traditionally they are made of wood, typically rosewood, ebony or grenadilla. In modern times they are also made of fibreglass or plastics. When struck they produce a bright clicking noise. Claves are sometimes hollow and carved in the middle to amplify the sound. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/5/51/Playingclaves.jpg',
	picture_attr='Freddythehat at English Wikipedia [Public domain], via Wikimedia Commons')
session.add(instrument34)
session.commit()

instrument35 = Instrument(name='Cymbal',
	description='A cymbal is a common percussion instrument. Often used in pairs, cymbals consist of thin, normally round plates of various alloys. The majority of cymbals are of indefinite pitch, although small disc-shaped cymbals based on ancient designs sound a definite note. Cymbals are used in many ensembles ranging from the orchestra, percussion ensembles, jazz bands, heavy metal bands, and marching groups. Drum kits usually incorporate at least a crash, ride, or crash/ride, and a pair of hi-hat cymbals. A player of cymbals is known as a cymbalist. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/7/70/2006-07-06_Crash_Zildjian_14.jpg',
	picture_attr='Stephan Czuratis (Jazz-face) [CC BY-SA 2.5 (https://creativecommons.org/licenses/by-sa/2.5)], from Wikimedia Commons')
session.add(instrument35)
session.commit()

instrument36 = Instrument(name='Gong',
	description='A gong is an East and Southeast Asian musical percussion instrument that takes the form of a flat, circular metal disc which is hit with a mallet. The gong traces its roots back to the Bronze Age around 3500 BC. The term "gong" traces its origins in Java and scientific and archaeological research has established that Burma, China, Java and Annam were the four main gong manufacturing centres of the ancient world. The gong later found its way into the Western World in the 18th century when it was also used in the percussion section of a Western-style symphony orchestra. A form of bronze cauldron gong known as a resting bell was widely used in ancient Greece and Rome, for instance in the famous Oracle of Dodona, where disc gongs were also used. [wikipedia.org]',
	category_id=category4.id,
	picture_url='https://upload.wikimedia.org/wikipedia/commons/7/76/COLLECTIE_TROPENMUSEUM_Gong_hangend_in_een_standaard_onderdeel_van_gamelan_Semar_Pagulingan_TMnr_1340-13.jpg',
	picture_attr='Tropenmuseum, part of the National Museum of World Cultures [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)]')
session.add(instrument36)
session.commit()


print "added categories and instruments!"
