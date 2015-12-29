from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
from collections import namedtuple
from fuzzywuzzy import process

ZapCategory = namedtuple('ZapCategory', ['category', 'hebrew_description', 'english_description'])


class ZapCategories:
    class Electronics:
            HomeTheater = ZapCategory(category='e-hometheater', hebrew_description='קולנוע ביתי', english_description='Home Theater'),
            Projectors = ZapCategory(category='e-slideprojector', hebrew_description='מקרנים', english_description='Projectors')

            SmartWatch = ZapCategory(category='e-cellwatch', hebrew_description='שעוני יד חכמים', english_description='Watches smartphones'),
            SmartHome = ZapCategory(category='e-smarthouse', hebrew_description='בית חכם', english_description='smart House')

            VRGoggles = ZapCategory(category='e-vrglasses', hebrew_description='משקפי מציאות מדומה', english_description='Virtual-reality goggles')

            class Photography:
                Cameras = ZapCategory(category='e-camera', hebrew_description='מצלמות', english_description='Cams'),
                CamerasBatteries = ZapCategory(category='e-stillscamerabattery', hebrew_description='סוללות למצלמות', english_description='Camcorder Battery'),
                CameraGrips = ZapCategory(category='e-cameragrip', hebrew_description='גריפים למצלמות', english_description='Cameras grips')

            class Kitchen:
                Juicers = ZapCategory(category='e-squeezer', hebrew_description='מסחטות', english_description='Juicers')
                Dishwashers = ZapCategory(category='e-dishwasher', hebrew_description='מדיחי כלים', english_description='Dishwashers')
                CoffeeMachines = ZapCategory(category='e-coffeemachine', hebrew_description='מכונות קפה', english_description='Coffee machines')
                CoffeeProducts = ZapCategory(category='e-coffeepods', hebrew_description='מוצרי קפה', english_description='Coffee products')
                VegetableCutter = ZapCategory(category='e-slicer', hebrew_description='קוצצי ירקות', english_description='Vegetable cutter')
                WineCooler = ZapCategory(category='e-winefridge', hebrew_description='מקררי יין', english_description='Wine cooler')
                Hoods = ZapCategory(category='e-hoods', hebrew_description='קולטי אדים', english_description='Hoods')
                BreadMaker = ZapCategory(category='e-baker', hebrew_description='אופה לחם', english_description='Baking bread')
                Refrigerators = ZapCategory(category='e-fridge', hebrew_description='מקררים', english_description='Refrigerators')
                MeatGrinder=ZapCategory(category='e-grinder', hebrew_description='מטחנות בשר', english_description='Meat Grinder')
                CoffeeAndTea = ZapCategory(category='e-coffeegran', hebrew_description='קפה, תה ואביזריהם', english_description='Coffee, tea and accessories')
                Toasters=ZapCategory(category='e-toster', hebrew_description='טוסטרים', english_description='Toasters')
                Ovens=ZapCategory(category='e-oven', hebrew_description='תנורי אפייה', english_description='Cookers')
                Ketteles=ZapCategory(category='e-kettle', hebrew_description='קומקומים ומיחמים', english_description='Kettles and samovars')
                FoodProcessors=ZapCategory(category='e-foodproccessor', hebrew_description='מעבדי מזון', english_description='Food Processors')
                Microwaves=ZapCategory(category='e-microwaveoven', hebrew_description='מיקרוגלים', english_description='Microwaves')

            class Gaming:
                PlayStationGames = ZapCategory(category='e-plays-games', hebrew_description='פלייסטיישן - משחקים', english_description='PlayStation - Games')
                WiiAccessories = ZapCategory(category='e-wiiaccecories', hebrew_description='אביזרים ל Wii', english_description='Accessories for Wii')
                GamingConsoles = ZapCategory(category='e-tvgame', hebrew_description='משחקי טלוויזיה - קונסולות', english_description='TV Games - Consoles')
                PlayStationAccessories = ZapCategory(category='e-plays-accesories', hebrew_description='פלייסטיישן - אביזרים', english_description='PlayStation - Accessories')
                ProductsForGameBoyDS = ZapCategory(category='e-gameboytape', hebrew_description='מוצרים לGameBoy/DS', english_description='Products for GameBoy / DS')
                GamesforXBOX=ZapCategory(category='e-xboxgames', hebrew_description='משחקים לXBOX', english_description='Games for XBOX')
                XboxAccesories=ZapCategory(category='e-xboxaccecories', hebrew_description='מוצרים לX-Box', english_description='Goods for X-Box')
                WiiGames=ZapCategory(category='e-wiigames', hebrew_description='משחקים ל Wii', english_description='Games for Wii')

            class Cellphones:
                CellphoneScreenProtectors = ZapCategory(category='e-cellscreen', hebrew_description='מגני מסך לטלפונים סלולריים', english_description='Screen protectors for mobile phones')
                CellphoneHolders = ZapCategory(category='e-cellphoneholder', hebrew_description='תושבות ומעמדים לסלולרי', english_description='Residence and cell phone holders')
                CellPhones = ZapCategory(category='e-cellphone', hebrew_description='טלפונים סלולריים', english_description='Mobile Phones')
                CellPhoneAccesories=ZapCategory(category='e-cellphoneaccessories', hebrew_description='אביזרים לטלפונים סלולאריים', english_description='Accessories for mobile phones')

            class MiscElectronics:
                EmergencyLights=ZapCategory(category='e-emergencylamp', hebrew_description='תאורת חירום', english_description='emergency lighting')

            EBookReadersCases=ZapCategory(category='e-digitalbookcase', hebrew_description='נרתיקים לקוראי ספרים אלקטרונים', english_description='Cases eBook Readers')
            VacuumCleaners = ZapCategory(category='e-vaccumcleaner', hebrew_description='שואבי אבק', english_description='Vacuum cleaners'),
            Speakers=ZapCategory(category='e-speaker', hebrew_description='רמקולים', english_description='Speakers')
            TVDecoders=ZapCategory(category='e-tvconverter', hebrew_description='ממירים דיגיטליים', english_description='Digital converters')
            ElectricalAccesories=ZapCategory(category='e-spliter', hebrew_description='אביזרי חשמל ומפצלים', english_description='Electrical accessories and splitters')
            SteamCleaners=ZapCategory(category='e-steam', hebrew_description='ערכות ניקוי בקיטור', english_description='Steam cleaning kits')
            RemoteControls=ZapCategory(category='e-remotecontrol', hebrew_description='שלט רחוק', english_description='Remote Control')

            Shavers=ZapCategory(category='e-shavingmachine', hebrew_description='מכונות גילוח', english_description='Shavers')
            ReceiversandAmplifiers=ZapCategory(category='e-amplifier', hebrew_description='רסיברים ומגברים', english_description='Receivers and Amplifiers')
            TVsets=ZapCategory(category='e-tv', hebrew_description='טלויזיות', english_description='TV sets')
            PortableAudioSystems=ZapCategory(category='e-potableaudiosystem', hebrew_description='מערכות שמע ניידות', english_description='Portable Audio Systems')



            BeardTrimmers=ZapCategory(category='e-beard', hebrew_description='מכונות לעיצוב זקן', english_description='Beard trimmers')

            HairStylingProducts=ZapCategory(category='e-hairdesigner', hebrew_description='מוצרים לעיצוב שיער', english_description='Hair styling products')
            Irons=ZapCategory(category='e-iron', hebrew_description='מגהצים', english_description='Irons')


            DVDdevices=ZapCategory(category='e-dvd', hebrew_description='מכשירי DVD', english_description='DVD devices')
            Coversphones=ZapCategory(category='e-cellphonecase', hebrew_description='כיסויים לסלולריים', english_description='Covers phones')
            Stovesandspaceheaters=ZapCategory(category='e-airheater', hebrew_description='תנורים ומפזרי חום', english_description='Stoves and space heaters')



            Garbagedisposals=ZapCategory(category='e-trashdisposal', hebrew_description='טוחני אשפה', english_description='Garbage disposals')



            Diskman=ZapCategory(category='e-diskman', hebrew_description='דיסקמן', english_description='Disk man')

            Chargers=ZapCategory(category='e-charger', hebrew_description='מטענים', english_description='Chargers')
            washingmachines=ZapCategory(category='e-washingmachine', hebrew_description='מכונות כביסה', english_description='washing machines')

            CDs=ZapCategory(category='e-cdplayer', hebrew_description='קומפקט דיסקים', english_description='CDs')

            Telephones=ZapCategory(category='e-telephone', hebrew_description='טלפונים', english_description='Telephones')
            Microphones=ZapCategory(category='e-microphone', hebrew_description='מיקרופונים', english_description='Microphones')
            CopyMachines=ZapCategory(category='e-copymachine', hebrew_description='מכונות צילום', english_description='Copiers')

            SpecialScanners=ZapCategory(category='e-barcode', hebrew_description='סורקים יעודיים', english_description='Designated scanners')
            HeadphoneAccessories=ZapCategory(category='e-headphoneaccessories', hebrew_description='אביזרים לאוזניות', english_description='Headphone Accessories')
            Repairphonesandtablets=ZapCategory(category='e-cellphoneservice', hebrew_description='תיקון סלולריים וטאבלטים', english_description='Repair phones and tablets')
            Battery=ZapCategory(category='e-battery', hebrew_description='סוללות', english_description='Battery')
            HaircutMachines=ZapCategory(category='e-haircuter', hebrew_description='מכונות תספורת', english_description='Haircut Machines')
            Peripheralsphoto=ZapCategory(category='e-digitalcamaccecories', hebrew_description='ציוד היקפי לצילום', english_description='Peripherals photo')
            GPSnavigationsystems=ZapCategory(category='e-gpsreciever', hebrew_description='מערכות ניווט GPS', english_description='GPS navigation systems')

            Dryers=ZapCategory(category='e-drayer', hebrew_description='מייבשי כביסה', english_description='Dryers')
            Blenders=ZapCategory(category='e-blender', hebrew_description='בלנדרים', english_description='Blenders')

            EBookreaders=ZapCategory(category='e-digitalbook', hebrew_description='קוראי ספרים אלקטרוניים', english_description='E-book readers')
            PaperShredders=ZapCategory(category='e-shredder', hebrew_description='מגרסות נייר', english_description='Paper shredders')
            Depilatories=ZapCategory(category='e-hairremover', hebrew_description='מסירי שיער', english_description='Depilatories')
            Headphones=ZapCategory(category='e-headphone', hebrew_description='אוזניות', english_description='Headphones')
            electricplate=ZapCategory(category='e-plata', hebrew_description='פלטה חשמלית', english_description='electric plate')

            Radios=ZapCategory(category='e-twowayradio', hebrew_description='מכשירי קשר', english_description='Radios')
            Accessoriesformicrophones=ZapCategory(category='e-microphoneaccessories', hebrew_description='אביזרים למיקרופונים', english_description='Accessories for microphones')
            Calculators=ZapCategory(category='e-calculator', hebrew_description='מחשבונים', english_description='Calculators')
            Powerbanks=ZapCategory(category='e-powerbank', hebrew_description='מטענים ניידים / סוללות גיבוי', english_description='Mobile chargers / Battery Backup')
            GPSAccesories=ZapCategory(category='e-gps', hebrew_description='אביזרים לניווט לוויני', english_description='Satellite navigation accessories')
            PortableSpeakers=ZapCategory(category='e-mpspeakers', hebrew_description='רמקולים ניידים ותחנות עגינה', english_description='Portable Speakers and Docking Stations')
            Printingofdigitalphotographs=ZapCategory(category='e-develope', hebrew_description='הדפסת תמונות דיגטליות', english_description='Printing of digital photographs')
            Turntables=ZapCategory(category='e-patiphone', hebrew_description='פטיפונים', english_description='Turntables')

            AirConditioners=ZapCategory(category='e-airconditioner', hebrew_description='מזגנים', english_description='Air Conditioners')
            Radiators=ZapCategory(category='e-radiator', hebrew_description='רדיאטורים', english_description='Radiators')
            Mixers=ZapCategory(category='e-mixer', hebrew_description='מיקסרים', english_description='Mixers')

            Freezers=ZapCategory(category='e-freezer', hebrew_description='מקפיאים', english_description='Freezers')
            Fans=ZapCategory(category='e-fan', hebrew_description='מאווררים', english_description='Fans')

            Faxes=ZapCategory(category='e-fax', hebrew_description='מכשירי פקס', english_description='Faxes')
            Stereos=ZapCategory(category='e-audiosystem', hebrew_description='מערכות סטריאו', english_description='Stereos')
            SpiceGrinders=ZapCategory(category='e-coffeegrinder', hebrew_description='מטחנות קפה ותבלינים', english_description='Coffee and spice grinders')
            Skimmers=ZapCategory(category='e-drone', hebrew_description='רחפנים', english_description='Skimmers')
            HairDryers=ZapCategory(category='e-hairdrayer', hebrew_description='מייבשי שיער', english_description='Hair Dryers')
            ProjectorsAudio=ZapCategory(category='e-soundbar', hebrew_description='מקרני קול/סאונד-בר', english_description='Projectors Audio / Sound-Bar')
            IceCreamMachines=ZapCategory(category='e-icecreammachine', hebrew_description='גלידה, פופקורן ועוד', english_description='Ice cream, popcorn and more')

            Streamers=ZapCategory(category='e-mediaplayer', hebrew_description='סטרימרים', english_description='Streamers')

            Videocameras=ZapCategory(category='e-videocamera', hebrew_description='מצלמות וידאו', english_description='Video cameras')
            Capsulesforcoffeemachines=ZapCategory(category='e-coffeecapsule', hebrew_description='קפסולות למכונות קפה', english_description='Capsules for coffee machines')
            Stove=ZapCategory(category='e-hobs', hebrew_description='כיריים', english_description='Stove')
            Headsets=ZapCategory(category='e-diburit', hebrew_description='דיבוריות', english_description='Headsets')
            EquipmentforDJ=ZapCategory(category='e-djmixer', hebrew_description='ציוד לתקליטנים', english_description='Equipment for DJ')

            RecordingDevices=ZapCategory(category='e-recorder', hebrew_description='מכשירי הקלטה', english_description='Recording Devices')
            Mosquitorepllant=ZapCategory(category='e-mosquito', hebrew_description='קוטל/דוחה יתושים', english_description='Killer / repellent')

    class Computers:
        MemoryCard = ZapCategory(category='c-flashmemory', hebrew_description='כרטיס זיכרון', english_description='Memory Card')
        BluetoothProducts = ZapCategory(category='c-bluetooth', hebrew_description='מוצרי Bluetooth', english_description='Bluetooth products')
        CardReaders = ZapCategory(category='c-cardreader', hebrew_description='קוראי כרטיסים', english_description='Card Readers')
        MP3players = ZapCategory(category='c-mp3player', hebrew_description='נגני MP3/MP4', english_description='MP3 players / MP4')
        CablesAndAdapters = ZapCategory(category='c-cable', hebrew_description='כבלים ומתאמים', english_description='Cables and Adapters')


def _get_recursive_attrs_dict(x):
    results = {}
    for attr_name in dir(x):
        # filter all methods
        if not attr_name.startswith('__') and not callable(attr_name):
            attribute = getattr(x, attr_name)
            # if node is a ZapCategory, add it to results
            if isinstance(attribute, ZapCategory):
                results[attr_name] = attribute

            # else, fetch all nodes
            if isinstance(attribute, type):
                results.update(_get_recursive_attrs_dict(attribute))

    return results


all_attrs = _get_recursive_attrs_dict(ZapCategories)


def suggest_category(category):
    return process.extract(category, all_attrs, limit=3)
