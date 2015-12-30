from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
from collections import namedtuple
from fuzzywuzzy import process

from pies.overrides import *

ZapCategory = namedtuple('ZapCategory', ['category', 'hebrew_description', 'english_description'])


class ZapCategories:
    class Electronics:
            class Photography:
                Cameras=ZapCategory(category='e-camera', hebrew_description='מצלמות', english_description='Cams')
                VideoCameras=ZapCategory(category='e-videocamera', hebrew_description='מצלמות וידאו', english_description='Video cameras')
                CamerasExtreme=ZapCategory(category='s-extremecamera', hebrew_description='מצלמות אקסטרים', english_description='Cameras Extreme')
                CameraLenses=ZapCategory(category='h-cameralens', hebrew_description='עדשות מצלמה', english_description='Camera Lenses')
                CameraFlashes=ZapCategory(category='h-cameraflash', hebrew_description='פלאשים למצלמות', english_description='Camera Flashes')
                FiltersHoods=ZapCategory(category='h-lensfilter', hebrew_description='פילטרים לעדשות', english_description='Filters Hoods')
                Grifimcameras=ZapCategory(category='e-cameragrip', hebrew_description='גריפים למצלמות', english_description='Grifim cameras')
                SunProtectiveLenses=ZapCategory(category='h-lenshood', hebrew_description='מגני שמש לעדשות', english_description='Sun-protective lenses')
                MemoryCard=ZapCategory(category='c-flashmemory', hebrew_description='כרטיס זיכרון', english_description='Memory Card')
                CardReaders=ZapCategory(category='c-cardreader', hebrew_description='קוראי כרטיסים', english_description='Card Readers')
                Tripods=ZapCategory(category='h-tripod', hebrew_description='חצובות', english_description='Tripods')
                VehicleCameras=ZapCategory(category='t-dashcam', hebrew_description='מצלמות לרכב', english_description='Vehicle Cameras')
                CamcorderBattery=ZapCategory(category='e-stillscamerabattery', hebrew_description='סוללות למצלמות', english_description='Camcorder Battery')
                PhotoBackgrounds=ZapCategory(category='h-photobackground', hebrew_description='רקעי צילום', english_description='Photo backgrounds')
                Peripheralsphoto=ZapCategory(category='e-digitalcamaccecories', hebrew_description='ציוד היקפי לצילום', english_description='Peripherals photo')
                CameraBags=ZapCategory(category='h-camerabag', hebrew_description='תיקים למצלמות', english_description='Bags for cameras')
                PhotosFrames=ZapCategory(category='h-frame', hebrew_description='מסגרות ואלבומים לתמונות', english_description='Frames and albums for photos')
                Printingofdigitalphotographs=ZapCategory(category='e-develope', hebrew_description='הדפסת תמונות דיגטליות', english_description='Printing of digital photographs')
                Hovercrafts=ZapCategory(category='e-drone', hebrew_description='רחפנים', english_description='Skimmers')
                Film=ZapCategory(category='h-film', hebrew_description='סרטי צילום', english_description='Film')

            class Communications:
                MobilePhones=ZapCategory(category='e-cellphone', hebrew_description='טלפונים סלולריים', english_description='Mobile Phones')
                Telephones=ZapCategory(category='e-telephone', hebrew_description='טלפונים', english_description='Telephones')
                CellphoneCovers=ZapCategory(category='e-cellphonecase', hebrew_description='כיסויים לסלולריים', english_description='Covers phones')
                CellPhoneMounts=ZapCategory(category='e-cellphoneholder', hebrew_description='תושבות ומעמדים לסלולרי', english_description='Residence and cell phone holders')
                MobilePhonesScreenProtectors=ZapCategory(category='e-cellscreen', hebrew_description='מגני מסך לטלפונים סלולריים', english_description='Screen protectors for mobile phones')
                GPS=ZapCategory(category='e-gpsreciever', hebrew_description='מערכות ניווט GPS', english_description='GPS navigation systems')
                CellphoneAccesories=ZapCategory(category='e-cellphoneaccessories', hebrew_description='אביזרים לטלפונים סלולאריים', english_description='Accessories for mobile phones')
                Satellitenavigationaccessories=ZapCategory(category='e-gps', hebrew_description='אביזרים לניווט לוויני', english_description='Satellite navigation accessories')
                Headsets=ZapCategory(category='e-diburit', hebrew_description='דיבוריות', english_description='Headsets')
                Radios=ZapCategory(category='e-twowayradio', hebrew_description='מכשירי קשר', english_description='Radios')
                Intercom=ZapCategory(category='h-intercom', hebrew_description='אינטרקום', english_description='Intercom')
                SmartWatches=ZapCategory(category='e-cellwatch', hebrew_description='שעוני יד חכמים', english_description='Watches smartphones')
                Chargers=ZapCategory(category='e-powerbank', hebrew_description='מטענים ניידים / סוללות גיבוי', english_description='Mobile chargers / Battery Backup')
                Bluetooth=ZapCategory(category='c-bluetooth', hebrew_description='מוצרי Bluetooth', english_description='Bluetooth products')
                RepairServices=ZapCategory(category='e-cellphoneservice', hebrew_description='תיקון סלולריים וטאבלטים', english_description='Repair phones and tablets')

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

            class IronsAndLaundry:
                Irons=ZapCategory(category='e-iron', hebrew_description='מגהצים', english_description='Irons')
                Dryers=ZapCategory(category='e-drayer', hebrew_description='מייבשי כביסה', english_description='Dryers')
                WashingMachines=ZapCategory(category='e-washingmachine', hebrew_description='מכונות כביסה', english_description='washing machines')
                SteamCleaning=ZapCategory(category='e-steam', hebrew_description='ערכות ניקוי בקיטור', english_description='Steam cleaning kits')
                Vacuumcleaners=ZapCategory(category='e-vaccumcleaner', hebrew_description='שואבי אבק', english_description='Vacuum cleaners')

            class TemperatureControl:
                AirConditioners=ZapCategory(category='e-airconditioner', hebrew_description='מזגנים', english_description='Air Conditioners')
                Radiators=ZapCategory(category='e-radiator', hebrew_description='רדיאטורים', english_description='Radiators')
                Stovesandspaceheaters=ZapCategory(category='e-airheater', hebrew_description='תנורים ומפזרי חום', english_description='Stoves and space heaters')
                Solarwaterheatersandaccessories=ZapCategory(category='h-boiler', hebrew_description='דודי שמש ואביזריהם', english_description='Solar water heaters and accessories')
                Fans=ZapCategory(category='e-fan', hebrew_description='מאווררים', english_description='Fans')

            class CarStereo:
                CD=ZapCategory(category='t-mp3', hebrew_description='רדיו דיסק לרכב', english_description='Car CD')
                Screens=ZapCategory(category='t-monitordvd', hebrew_description='מסכים לרכב', english_description='Vehicle Screen')
                RadioDisk=ZapCategory(category='t-indashdvd', hebrew_description='רדיו דיסק DVD לרכב', english_description='DVD CD radio car')
                Speakers=ZapCategory(category='t-speakers', hebrew_description='רמקולים לרכב', english_description='Car speakers')
                Amplifiers=ZapCategory(category='t-amplifier', hebrew_description='מגברים לרכב', english_description='Car Amplifiers')

            class HealthAndBeauty:
                HairDryers=ZapCategory(category='e-hairdrayer', hebrew_description='מייבשי שיער', english_description='Hair Dryers')
                Shavers=ZapCategory(category='e-shavingmachine', hebrew_description='מכונות גילוח', english_description='Shavers')
                HaircutMachines=ZapCategory(category='e-haircuter', hebrew_description='מכונות תספורת', english_description='Haircut Machines')
                Depilatories=ZapCategory(category='e-hairremover', hebrew_description='מסירי שיער', english_description='Depilatories')
                Hairstylingproducts=ZapCategory(category='e-hairdesigner', hebrew_description='מוצרים לעיצוב שיער', english_description='Hair styling products')
                Machinesforold=ZapCategory(category='e-beard', hebrew_description='מכונות לעיצוב זקן', english_description='Machines for old')
                Oralhygiene=ZapCategory(category='b-tooth', hebrew_description='הגיינת הפה', english_description='Oral hygiene')
                Airfresheners=ZapCategory(category='b-airrefresher', hebrew_description='מטהרי אויר', english_description='Air fresheners')

            class Miscellaneous:
                SmartHome=ZapCategory(category='e-smarthouse', hebrew_description='בית חכם', english_description='smart House')
                TVStands=ZapCategory(category='h-tvholder', hebrew_description='מתקני תלייה', english_description='Racks')
                RemoteControl=ZapCategory(category='e-remotecontrol', hebrew_description='שלט רחוק', english_description='Remote Control')
                Chargers=ZapCategory(category='e-charger', hebrew_description='מטענים', english_description='Chargers')
                Battery=ZapCategory(category='e-battery', hebrew_description='סוללות', english_description='Battery')
                EmergencyLighting=ZapCategory(category='e-emergencylamp', hebrew_description='תאורת חירום', english_description='emergency lighting')
                MP3playersAccessories=ZapCategory(category='c-mp3accessories', hebrew_description='אביזרים לנגני MP3', english_description='Accessories for MP3 players')
                ProjectorAccessories=ZapCategory(category='h-projection', hebrew_description='אביזרים למקרנים', english_description='Projector Accessories')
                SewingMachineAccessories=ZapCategory(category='h-sewingmachine', hebrew_description='מכונת תפירה ואביזרים', english_description='Sewing Machine Accessories')
                CablesAndAdapters=ZapCategory(category='c-cable', hebrew_description='כבלים ומתאמים', english_description='Cables and Adapters')
                ElectricalOutlets=ZapCategory(category='e-spliter', hebrew_description='אביזרי חשמל ומפצלים', english_description='Electrical accessories and splitters')
                SecurityCameras=ZapCategory(category='g-hiddencam', hebrew_description='מצלמות אבטחה', english_description='Security Cameras')
                DJEquipment=ZapCategory(category='e-djmixer', hebrew_description='ציוד לתקליטנים', english_description='Equipment for DJ')
                MosquitoRepellent=ZapCategory(category='e-mosquito', hebrew_description='קוטל/דוחה יתושים', english_description='Killer / repellent')
                AVTape=ZapCategory(category='h-tape', hebrew_description='קלטות וידאו/אודיו', english_description='Videos / audio')
                EBookreader=ZapCategory(category='e-digitalbook', hebrew_description='קוראי ספרים אלקטרוניים', english_description='E-book readers')
                EBookreaderCases=ZapCategory(category='e-digitalbookcase', hebrew_description='נרתיקים לקוראי ספרים אלקטרונים', english_description='Cases eBook Readers')

            class HomeAudio:
                TVsets=ZapCategory(category='e-tv', hebrew_description='טלויזיות', english_description='TV sets')
                Headphones=ZapCategory(category='e-headphone', hebrew_description='אוזניות', english_description='Headphones')
                Projectors=ZapCategory(category='e-slideprojector', hebrew_description='מקרנים', english_description='Projectors')
                MP3players=ZapCategory(category='c-mp3player', hebrew_description='נגני MP3/MP4', english_description='MP3 players / MP4')
                DigitalConverters=ZapCategory(category='e-tvconverter', hebrew_description='ממירים דיגיטליים', english_description='Digital converters')
                Streamers=ZapCategory(category='e-mediaplayer', hebrew_description='סטרימרים', english_description='Streamers')
                ReceiversAndAmplifiers=ZapCategory(category='e-amplifier', hebrew_description='רסיברים ומגברים', english_description='Receivers and Amplifiers')
                Speakers=ZapCategory(category='e-speaker', hebrew_description='רמקולים', english_description='Speakers')
                HomeTheater=ZapCategory(category='e-hometheater', hebrew_description='קולנוע ביתי', english_description='Home Theater')
                PortableSpeakers=ZapCategory(category='e-mpspeakers', hebrew_description='רמקולים ניידים ותחנות עגינה', english_description='Portable Speakers and Docking Stations')
                Stereos=ZapCategory(category='e-audiosystem', hebrew_description='מערכות סטריאו', english_description='Stereos')
                SoundBar=ZapCategory(category='e-soundbar', hebrew_description='מקרני קול/סאונד-בר', english_description='Projectors Audio / Sound-Bar')
                PortableAudioSystems=ZapCategory(category='e-potableaudiosystem', hebrew_description='מערכות שמע ניידות', english_description='Portable Audio Systems')
                Microphones=ZapCategory(category='e-microphone', hebrew_description='מיקרופונים', english_description='Microphones')
                Entertainment=ZapCategory(category='e-bidurit', hebrew_description='בידוריות', english_description='Entertainment')
                Turntables=ZapCategory(category='e-patiphone', hebrew_description='פטיפונים', english_description='Turntables')
                VRGoggles=ZapCategory(category='e-vrglasses', hebrew_description='משקפי מציאות מדומה', english_description='Virtual-reality goggles')
                DVDDevices=ZapCategory(category='e-dvd', hebrew_description='מכשירי DVD', english_description='DVD devices')
                CDs=ZapCategory(category='e-cdplayer', hebrew_description='קומפקט דיסקים', english_description='CDs')
                MicrophonesAccesories=ZapCategory(category='e-microphoneaccessories', hebrew_description='אביזרים למיקרופונים', english_description='Accessories for microphones')
                HeadphoneAccessories=ZapCategory(category='e-headphoneaccessories', hebrew_description='אביזרים לאוזניות', english_description='Headphone Accessories')
                Diskman=ZapCategory(category='e-diskman', hebrew_description='דיסקמן', english_description='Disk man')

            class OfficeEquipment:
                InkToners=ZapCategory(category='h-ink', hebrew_description='דיו וטונרים', english_description='Ink and Toners')
                PaperShredders=ZapCategory(category='e-shredder', hebrew_description='מגרסות נייר', english_description='Paper shredders')
                Printers=ZapCategory(category='c-printer', hebrew_description='מדפסות', english_description='Printers')
                Copiers=ZapCategory(category='e-copymachine', hebrew_description='מכונות צילום', english_description='Copiers')
                Faxes=ZapCategory(category='e-fax', hebrew_description='מכשירי פקס', english_description='Faxes')
                RecordingDevices=ZapCategory(category='e-recorder', hebrew_description='מכשירי הקלטה', english_description='Recording Devices')
                Calculators=ZapCategory(category='e-calculator', hebrew_description='מחשבונים', english_description='Calculators')
                BindersAndlaminators=ZapCategory(category='h-binding', hebrew_description='מכשירי כריכה ולמינציה', english_description='Binders and laminators')
                SpecialScanners=ZapCategory(category='e-barcode', hebrew_description='סורקים יעודיים', english_description='Designated scanners')
                ElectronicDictionaries=ZapCategory(category='e-translator', hebrew_description='מילונים אלקטרוניים', english_description='Electronic Dictionaries')

    class Computers:

        class WholeComputers:
            MobileComputers=ZapCategory(category='c-pclaptop', hebrew_description='מחשבים ניידים', english_description='mobile computers')
            DesktopComputers=ZapCategory(category='c-pcdesktop', hebrew_description='מחשבים אישיים', english_description='Personal computers')
            Tablets=ZapCategory(category='c-tabletpc', hebrew_description='טאבלטים', english_description='Tablets')
            BrandComputers=ZapCategory(category='c-brandpc', hebrew_description='מחשבי מותג', english_description='Brand computers')
            HTPC=ZapCategory(category='c-htpc', hebrew_description='מחשבים לקולנוע ביתי', english_description='Desktop Computers')
            Laptops=ZapCategory(category='c-allinonepc', hebrew_description='מחשבי All in one', english_description='Laptops All in one')
            ComputerAssemblyKits=ZapCategory(category='c-upgradekit', hebrew_description='ערכות מחשב להרכבה', english_description='Computer kits for assembly')
            Servers=ZapCategory(category='c-server', hebrew_description='שרתים', english_description='Servers')

        class Peripherals:
            Printers=ZapCategory(category='c-printer', hebrew_description='מדפסות', english_description='Printers')
            ComputerScreens=ZapCategory(category='c-monitor', hebrew_description='מסכי מחשב', english_description='computer screens')
            Webcams=ZapCategory(category='c-webcam', hebrew_description='מצלמות רשת', english_description='Webcams')
            Keyboards=ZapCategory(category='c-keyboard', hebrew_description='מקלדות', english_description='Keyboards')
            Mice=ZapCategory(category='c-mouse', hebrew_description='עכברים', english_description='Mice')
            ComputerSpeakers=ZapCategory(category='c-speakers', hebrew_description='רמקולים למחשב', english_description='Computer Speakers')
            SatelliteNavigationAccessories=ZapCategory(category='e-gps', hebrew_description='אביזרים לניווט לוויני', english_description='Satellite navigation accessories')
            Headphones=ZapCategory(category='e-headphone', hebrew_description='אוזניות', english_description='Headphones')
            UPS=ZapCategory(category='c-ups', hebrew_description='אל פסק ומייצבי מתח', english_description='UPS and voltage regulators')
            GameAccesories=ZapCategory(category='c-joystick', hebrew_description="ג'ויסטיקים ואביזרי משחק", english_description='Joysticks and game accessories')
            ElectronicWritingBoards=ZapCategory(category='c-electronicboard', hebrew_description='לוחות כתיבה אלקטרוניים', english_description='Electronic Writing Boards')
            Scanners=ZapCategory(category='c-scanner', hebrew_description='סורקים', english_description='Scanners')
            Comfy=ZapCategory(category='c-komfy', hebrew_description='קומפי', english_description='Comfy')
            Racks=ZapCategory(category='c-communicationcloset', hebrew_description='ארונות תקשורת ואביזרים', english_description='Racks and Accessories')

        class Storage:
            HardDrives=ZapCategory(category='c-harddrive', hebrew_description='כוננים קשיחים', english_description='Hard drives')
            DVDBurners=ZapCategory(category='c-dvdwriter', hebrew_description='צורבי DVD', english_description='DVD burners')
            USBFlashDrives=ZapCategory(category='c-diskonkey', hebrew_description='זכרונות ניידים USB', english_description='USB Flash Drives')
            TapeBackup=ZapCategory(category='c-gibuy', hebrew_description='טייפ גיבוי', english_description='Tape Backup')
            FloppyDrives=ZapCategory(category='c-floppy', hebrew_description='כונני דיסקטים', english_description='Floppy drives')
            CDDrives=ZapCategory(category='c-dvd', hebrew_description='כונני DVD ו-CD', english_description='DVD drives and CD')
            HardDiskEnclosures=ZapCategory(category='c-drivercase', hebrew_description='מארזי כוננים ודיסקים', english_description='Enclosures and disk drives')
            NASs=ZapCategory(category='c-nasserver', hebrew_description='שרתי NAS', english_description='NAS servers')

        class OfficeEquipment:
            InkandToners=ZapCategory(category='h-ink', hebrew_description='דיו וטונרים', english_description='Ink and Toners')
            Computercleaningproducts=ZapCategory(category='c-comutercleaning', hebrew_description='חומרי ניקוי למחשב', english_description='Computer cleaning products')
            Printers=ZapCategory(category='c-printer', hebrew_description='מדפסות', english_description='Printers')
            Mousepadsandkeyboard=ZapCategory(category='c-mousepad', hebrew_description='משטחים לעכבר ולמקלדת', english_description='Mouse pads and keyboard')
            RefillKits=ZapCategory(category='c-refillkit', hebrew_description='ערכות מילוי', english_description='Refill Kits')

        class Accesories:
            NotebookAccessories=ZapCategory(category='c-pclaptopaccessories', hebrew_description='אביזרים למחשבים ניידים', english_description='Notebook Accessories')
            OriginalBatteries=ZapCategory(category='c-originallaptopbattery', hebrew_description='סוללות מקוריות למחשבים ניידים', english_description='The original battery for portable computers')
            ReplacementBatteries=ZapCategory(category='c-replaptopbattery', hebrew_description='סוללות חליפיות למחשבים ניידים', english_description='Replacement batteries for laptops')
            Controllers=ZapCategory(category='c-controller', hebrew_description='בקרים', english_description='Controllers')
            CablesAndAdapters=ZapCategory(category='c-cable', hebrew_description='כבלים ומתאמים', english_description='Cables and Adapters')
            BluetoothProducts=ZapCategory(category='c-bluetooth', hebrew_description='מוצרי Bluetooth', english_description='Bluetooth products')
            FireWireProducts=ZapCategory(category='c-firewire', hebrew_description='מוצרי FireWire', english_description='FireWire products')
            ProductsRAID=ZapCategory(category='c-raid', hebrew_description='מוצרי RAID', english_description='Products RAID')
            PDACases=ZapCategory(category='c-palmcase', hebrew_description='נרתיקים למחשבי כף יד', english_description='PDA Cases')
            PDAAccessories=ZapCategory(category='c-comppalmaccessories', hebrew_description='עזרים למחשבי כף יד', english_description='PDA Accessories')
            LaptopCases=ZapCategory(category='c-compbag', hebrew_description='תיקים למחשב נייד', english_description='Laptop Cases')
            EbookReaders=ZapCategory(category='e-digitalbook', hebrew_description='קוראי ספרים אלקטרוניים', english_description='E-book readers')
            Infrared=ZapCategory(category='c-infraredadaptor', hebrew_description='אינפרא אדום', english_description='Infra red')
            Printers=ZapCategory(category='c-printeraccessories', hebrew_description='אביזרים למדפסות', english_description='Accessories for printers')
            Tables=ZapCategory(category='c-tabletaccessories', hebrew_description='אביזרים לטאבלטים', english_description='Accessories for tablets')
            TabletCovers=ZapCategory(category='c-tabletcase', hebrew_description='נרתיקים לטאבלטים', english_description='Covers for tablets')

        class Networking:
            NetworkCards=ZapCategory(category='c-networkcard', hebrew_description='כרטיסי רשת', english_description='Network Cards')
            Routers=ZapCategory(category='c-router', hebrew_description='נתבים (ראוטרים)', english_description='Routers (routers)')
            RangeExtenders=ZapCategory(category='c-repeater', hebrew_description='מגדילי טווח / Access Points', english_description='Magnifiers term / Access Points')
            Hubs=ZapCategory(category='c-hub', hebrew_description='רכזות רשת/ממתגים', english_description='Network Hubs / Switches')
            Swtiching=ZapCategory(category='c-switching', hebrew_description='קופסאות מיתוג', english_description='Switches')
            PrinertServers=ZapCategory(category='c-printserver', hebrew_description='שרתי מדפסות', english_description='Print servers')
            Wireless=ZapCategory(category='c-wireless', hebrew_description='ציוד משלים לתקשורת', english_description='Supplementary equipment for communication')
            Modems=ZapCategory(category='c-modem', hebrew_description='מודמים', english_description='Modems')

        class Hardware:
            TVCards=ZapCategory(category='c-tvcard', hebrew_description='כרטיסי TV ועריכה', english_description='TV cards and editing')
            GraphicsCards=ZapCategory(category='c-graphiccard', hebrew_description='כרטיסי מסך', english_description='Graphics Cards')
            SoundCards=ZapCategory(category='c-soundblaster', hebrew_description='כרטיסי קול', english_description='Sound Cards')
            Motherboards=ZapCategory(category='c-motherboard', hebrew_description='לוחות אם', english_description='Motherboards')
            Processors=ZapCategory(category='c-cpu', hebrew_description='מעבדים', english_description='Processors')
            DesktopMemory=ZapCategory(category='c-memory', hebrew_description='זיכרונות למחשבים נייחים', english_description='Memories PCs')
            LaptopMemory=ZapCategory(category='c-laptopmemory', hebrew_description='זיכרונות למחשבים ניידים', english_description='Memories for laptops')
            PowerSupplies=ZapCategory(category='c-powersupply', hebrew_description='ספקי כח למחשבים', english_description='Power supplies for computers')
            Cooling=ZapCategory(category='c-fan', hebrew_description='מאווררים ופתרונות קירור', english_description='Cooling')
            ComputerCases=ZapCategory(category='c-tower', hebrew_description='מארזי מחשב', english_description='Computer Cases')
            USBCards=ZapCategory(category='c-usbcard', hebrew_description='כרטיסי USB', english_description='USB cards')

        class Media:
            Recordablediscs=ZapCategory(category='c-cdwdisc', hebrew_description='דיסקים לצריבה', english_description='Recordable discs')
            CDStorageAccesories=ZapCategory(category='c-diskstorage', hebrew_description='אחסון דיסקים ודיסקטים', english_description='Storing CDs and DVDs')
            CleaningMedia=ZapCategory(category='c-cleaningmedia', hebrew_description='מדיות ניקוי', english_description='Cleaning media')
            TapeBackup=ZapCategory(category='c-storagetape', hebrew_description='קלטות גיבוי', english_description='Tape Backup')

        class Software:
            OperatingSystems=ZapCategory(category='c-operatingsystems', hebrew_description='מערכות הפעלה', english_description='Operating Systems')
            VideoGames=ZapCategory(category='c-games', hebrew_description='משחקי מחשב', english_description='Video Games')
            AntiVirus=ZapCategory(category='c-antivirus', hebrew_description='אנטי וירוסים', english_description='Anti-virus')
            OfficeSoftware=ZapCategory(category='c-office', hebrew_description='תוכנות משרדיות', english_description='Office software')
            Educational=ZapCategory(category='c-software', hebrew_description='תוכנות ולומדות', english_description='Software and courseware')

    class PersonalCare:
        class Fashion:
            Sunglasses=ZapCategory(category='b-glasses', hebrew_description='משקפי שמש', english_description='Sunglasses')
            Glasses=ZapCategory(category='b-visionglasses', hebrew_description='משקפי ראייה', english_description='Glasses')
            jewelry=ZapCategory(category='g-jewlery', hebrew_description='תכשיטים', english_description='jewelry')
            Bags=ZapCategory(category='h-bags', hebrew_description='תיקים', english_description='Cases')

        class BodyCare:
            WomenFragrance=ZapCategory(category='b-perfume', hebrew_description='בשמים לאישה', english_description='woman fragrance')
            MenFragrance=ZapCategory(category='b-aftershave', hebrew_description='בשמים לגבר', english_description="Men's fragrance")
            HairCare=ZapCategory(category='b-shampoo', hebrew_description='טיפוח שיער', english_description='Hair Care')
            ChildrenPerfumes=ZapCategory(category='b-kidsperfume', hebrew_description='בשמים לילדים', english_description='Perfumes for Children')
            HairRemovalProduct=ZapCategory(category='b-hairremoving', hebrew_description='מוצרים להסרת שיער', english_description='Hair Removal Product')
            Oils=ZapCategory(category='b-oil', hebrew_description='שמנים', english_description='Oils')
            HairAccessories=ZapCategory(category='b-hairaccessories', hebrew_description='אביזרים לשיער', english_description='Hair Accessories')
            Depilatories=ZapCategory(category='e-hairremover', hebrew_description='מסירי שיער', english_description='Depilatories')
            GreenCareProducts=ZapCategory(category='b-greencare', hebrew_description='מוצרי טיפוח ירוקים', english_description='Green care products')
            BodyCreams=ZapCategory(category='b-creambody', hebrew_description='קרמי גוף', english_description='Body Creams')
            EyeCreams=ZapCategory(category='b-creameye', hebrew_description='קרמי עיניים', english_description='Eye Creams')
            FacialCareproducts=ZapCategory(category='b-creamface', hebrew_description='מוצרים לטיפוח הפנים', english_description='Facial care products')
            HairDye=ZapCategory(category='b-haircolor', hebrew_description='צבעי שיער', english_description='Hair Dye')

        class Cosmetics:
            EyeMakeup=ZapCategory(category='b-eyemakeup', hebrew_description='איפור עיניים', english_description='Eye Makeup')
            Facialmakeup=ZapCategory(category='b-facemakeup', hebrew_description='איפור פנים', english_description='Facial makeup')
            Lipsticks=ZapCategory(category='b-lipstick', hebrew_description='שפתונים', english_description='Lipsticks')
            Cosmetologyequipmentandliterature=ZapCategory(category='b-cosmeticequipment', hebrew_description='ציוד לקוסמטיקאיות ומספרות', english_description='Cosmetology equipment and literature')
            MakeupTool=ZapCategory(category='b-makeupequip', hebrew_description='כלי איפור', english_description='Makeup Tool')
            Nailequipment=ZapCategory(category='b-nail', hebrew_description='ציוד לציפורניים', english_description='Nail equipment')

        class SmokingCessation:
            SmokingCessation=ZapCategory(category='b-smoke', hebrew_description='הפסקת עישון', english_description='Smoking Cessation')
            ECigaretteLiquidFill=ZapCategory(category='b-smokeliquid', hebrew_description='נוזל מילוי לסיגריות אלקטרוניות', english_description='Liquid filling of electronic cigarettes')
            ECigaretteAccesories=ZapCategory(category='b-smokeaccessories', hebrew_description='אביזרים לסיגריות אלקטרוניות', english_description='Accessories for electronic cigarettes')
            ECigarette=ZapCategory(category='b-electroniccigarette', hebrew_description='סיגריות אלקטרוניות', english_description='Electronic cigarettes')

        class Clothing:
            Shirts=ZapCategory(category='p-shirt', hebrew_description='חולצות', english_description='Shirts')
            pants=ZapCategory(category='p-pants', hebrew_description='מכנסיים', english_description='pants')
            Shoes=ZapCategory(category='p-shoe', hebrew_description='נעליים', english_description='Shoes')
            Lingerie=ZapCategory(category='p-underwear', hebrew_description='הלבשה תחתונה', english_description='Lingerie')
            Swimwear=ZapCategory(category='p-swimsuit', hebrew_description='בגדי ים', english_description='Swimwear')
            Hats=ZapCategory(category='p-hat', hebrew_description='כובעים', english_description='Hats')
            Jackets=ZapCategory(category='p-coat', hebrew_description='מעילים', english_description='Jackets')
            Belts=ZapCategory(category='p-belt', hebrew_description='חגורות', english_description='Belts')
            ClothingGeneral=ZapCategory(category='p-clothing', hebrew_description='הלבשה כללי', english_description='Clothing General')

        class Hygiene:
            ShavingAccessories=ZapCategory(category='b-shaving', hebrew_description='גילוח ואביזרים', english_description='Shaving Accessories')
            HygieneWomen=ZapCategory(category='b-hegyena', hebrew_description='היגיינת נשים', english_description='Hygiene Women')
            deodorant=ZapCategory(category='b-deodorant', hebrew_description='דאודורנט', english_description='deodorant')
            Oralhygiene=ZapCategory(category='b-tooth', hebrew_description='הגיינת הפה', english_description='Oral hygiene')
            Wipesandtissues=ZapCategory(category='b-wettowel', hebrew_description='מגבונים וממחטות', english_description='Wipes and tissues')
            Soaps=ZapCategory(category='b-soap', hebrew_description='סבונים', english_description='Soaps')

        class Health:
            Vitamins=ZapCategory(category='b-vitamin', hebrew_description='ויטמינים', english_description='Vitamins')
            Multivitamins=ZapCategory(category='b-multivitamin', hebrew_description='מולטי ויטמינים', english_description='Multivitamins')
            Minerals=ZapCategory(category='b-mineral', hebrew_description='מינרלים', english_description='Minerals')
            Herbs=ZapCategory(category='b-plants', hebrew_description='צמחי מרפא', english_description='medical herbs')
            NutritionalSupplements=ZapCategory(category='b-vitaminnew', hebrew_description='תוספי תזונה ותרופות ללא מרשם', english_description='Nutritional supplements and non-prescription medicines')
            PainRelieve=ZapCategory(category='b-pain', hebrew_description='כאבים וחום', english_description='Pain and fever')
            Cough=ZapCategory(category='b-cough', hebrew_description='נשימה', english_description='breathing')
            Diabetes=ZapCategory(category='b-diabetic', hebrew_description='סכרת', english_description='diabetes')
            BloodPressure=ZapCategory(category='b-bloodpressure', hebrew_description='לחץ דם ודופק', english_description='Blood pressure and pulse')
            NaturalFoodSupplements=ZapCategory(category='b-additive', hebrew_description='תוספי מזון לספורטאים', english_description='Natural Food Supplements')
            ContactLenses=ZapCategory(category='b-contactlens', hebrew_description='עדשות מגע', english_description='Contact Lenses')
            OrthopedicSupplies=ZapCategory(category='b-orthoped', hebrew_description='ציוד אורטופדי', english_description='Orthopedic Supplies')
            WalkingAids=ZapCategory(category='b-walkingaids', hebrew_description='עזרי הליכה', english_description='Walking aids')
            Nursing=ZapCategory(category='b-nursing', hebrew_description='ציוד סיעודי ופיזיותרפיה', english_description='Nursing and physiotherapy equipment')
            Insole=ZapCategory(category='s-footsupport', hebrew_description='מדרסים', english_description='Insole')
            Diapers=ZapCategory(category='b-diapers', hebrew_description='מוצרי ספיגה', english_description='Absorbent products')
            Wheelchairs=ZapCategory(category='b-wheelchair', hebrew_description='כסאות גלגלים', english_description='Wheelchairs')
            Sunscreen=ZapCategory(category='b-tanning', hebrew_description='מקדמי הגנה', english_description='Protection factors')
            BathroomSafety=ZapCategory(category='b-aidbath', hebrew_description='בטיחות באמבטיה ובשירותים', english_description='Safety bathrooms')
            ClinicEquipment=ZapCategory(category='b-medicalequipment', hebrew_description='ציוד למרפאות ומעבדות', english_description='Equipment clinics and laboratories')
            Pregnancy=ZapCategory(category='b-pregnancy', hebrew_description='מוצרי פריון, הריון ולידה', english_description='Products fertility, pregnancy and childbirth')
            Thermometers=ZapCategory(category='b-termometer', hebrew_description='מדי חום', english_description='Thermometers')
            AcneTreatment=ZapCategory(category='b-acne', hebrew_description='טיפול באקנה', english_description='Acne Treatment')
            Contraception=ZapCategory(category='b-condom', hebrew_description='אמצעי מניעה', english_description='Contraception')
            GreenProducts=ZapCategory(category='b-green', hebrew_description='מוצרים ירוקים', english_description='Green Products')
            GreenProductsBaby=ZapCategory(category='b-greenbaby', hebrew_description='מוצרים ירוקים לתינוק', english_description='Green Products baby')
            GreencareProducts=ZapCategory(category='b-greencare', hebrew_description='מוצרי טיפוח ירוקים', english_description='Green care products')
            GreenCleaning=ZapCategory(category='b-greenclean', hebrew_description='חומרי ניקוי ירוקים', english_description='Green Cleaning')

        class FirstAid:
            FirstAidKit=ZapCategory(category='b-firstaid', hebrew_description='ערכות עזרה ראשונה', english_description='First aid kit')
            FirstAidAccessories=ZapCategory(category='b-firstaidsubstance', hebrew_description='אביזרי עזרה ראשונה', english_description='Accessories First Aid')

        class Massage:
            Massagers=ZapCategory(category='e-massage', hebrew_description='מכשירי עיסוי', english_description='Massagers')
            SpaEquipment=ZapCategory(category='b-spaequipment', hebrew_description='ציוד לספא', english_description='Spa equipment')


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
all_categories_strings = [x.category for x in all_attrs.values()]


def suggest_category(category):
    return process.extract(category, all_categories_strings, limit=3)
