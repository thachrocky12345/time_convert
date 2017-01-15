import time
from datetime import datetime, timedelta

TIME_DIFF = {'ULAST': 540, 'FNT': -120, 'AKDT': -480, 'CCT': 480, 'BORT': 480, 'BOT': -240, 'TRUT': 600, 'EGT': -60, 'CLT': -180, 'DAVT': 420, 'WDT': 540, 'AWST': 480, 'MUST': 300, 'WAT': 60, 'PETT': 720, 'IOT': 360, 'NZDT': 780, 'MYT': 480, 'CHAST': 765, 'KGST': 360, 'HST': -600, 'PMDT': -120, 'NOVST': 420, 'AMST': 300, 'PMST': -180, 'METDST': 120, 'MAWT': 300, 'FJST': 780, 'LINT': 840, 'ALMST': 420, 'JAYT': 540, 'BNT': 480, 'LIGT': 600, 'WET': 0, 'KRAT': 420, 'NZST': 720, 'OMSST': 420, 'ACDT': 630, 'BRST': -120, 'ANAT': 720, 'CXT': 420, 'UYT': -180, 'CKT': -600, 'VLAST': 660, 'PYT': -240, 'VUT': 660, 'ALMT': 360, 'XJT': 360, 'IRKST': 540, 'NPT': 345, 'PHT': 480, 'KST': 540, 'EETDST': 180, 'YEKST': 360, 'EET': 120, 'LHDT': 660, 'VLAT': 600, 'LHST': 630, 'AZST': 300, 'LKT': 360, 'WFT': 720, 'CETDST': 120, 'MART': -570, 'PHOT': 780, 'PKT': 300, 'GET': 240, 'PETST': 720, 'YEKT': 300, 'EGST': 0, 'TKT': 780, 'CET': 60, 'EEST': 180, 'SCT': 240, 'AMT': 240, 'ZULU': 0, 'MAGT': 600, 'BDT': 360, 'CHUT': 600, 'NFT': -210, 'WGST': -120, 'AFT': 270, 'CST': -360, 'MHT': 720, 'AESST': 660, 'WGT': -180, 'UT': 0, 'Z': 0, 'UZST': 360, 'MPT': 600, 'YAKST': 600, 'TJT': 300, 'TVT': 720, 'GEST': 240, 'PST': -480, 'MUT': 240, 'GAMT': -540, 'TMT': 300, 'COT': -300, 'PET': -300, 'IDT': 180, 'AZOST': 0, 'RET': 240, 'IST': 120, 'ULAT': 480, 'AEDT': 660, 'HKT': 480, 'ACT': -300, 'FJT': 720, 'IRKT': 480, 'SAST': 120, 'AST': -240, 'BST': 60, 'FKT': -240, 'NUT': -660, 'ACSST': 630, 'JST': 540, 'CAST': 570, 'ANAST': 720, 'UYST': -120, 'MAGST': 720, 'KDT': 600, 'YAPT': 600, 'EAST': -300, 'TAHT': -600, 'MDT': -360, 'GALT': -360, 'ADT': -180, 'MST': -420, 'CLST': -180, 'PKST': 360, 'BTT': 360, 'OMST': 360, 'PDT': -420, 'WAST': 420, 'FET': 180, 'GILT': 720, 'KOST': 660, 'NDT': -150, 'GMT': 0, 'WETDST': 60, 'PYST': -180, 'MMT': 390, 'BRT': -180, 'YAKT': 540, 'CDT': -300, 'MET': 60, 'EDT': -240, 'NOVT': 360, 'BRA': -180, 'MEZ': 60, 'KRAST': 480, 'TFT': 300, 'CADT': 630, 'FNST': -60, 'WADT': 480, 'PONT': 660, 'AWSST': 540, 'VET': -270, 'TOT': 780, 'AEST': 600, 'MSK': 180, 'MVT': 300, 'MSD': 240, 'AZT': 240, 'UCT': 0, 'ACST': 570, 'SGT': 480, 'AKST': -540, 'PGT': 600, 'GYT': -240, 'CEST': 120, 'UZT': 300, 'NST': -210, 'EAT': 180, 'UTC': 0, 'EST': -300, 'WAKT': 720, 'NZT': 720, 'IRT': 210, 'MEST': 120, 'VOLT': 240, 'ACWST': 525, 'SADT': 630, 'CHADT': 825, 'FKST': -180, 'AZOT': -60, 'ICT': 420, 'PWT': 540, 'ART': -180, 'KGT': 360, 'GFT': -180, 'BDST': 120, 'ARST': -120, 'DDUT': 600, 'EASST': -300}
ABBREV = {'FNT': 'posix/Brazil/DeNoronha', 'AKDT': 'posix/US/Alaska', 'GST': 'posix/Atlantic/South_Georgia', 'PMDT': 'posix/America/Miquelon', 'LINT': 'posix/Pacific/Kiritimati', 'BOT': 'posix/America/La_Paz', 'EGT': 'posix/America/Scoresbysund', 'XJT': 'posix/Asia/Urumqi', 'GAMT': 'posix/Pacific/Gambier', 'WITA': 'posix/Asia/Ujung_Pandang', 'AWST': 'posix/Australia/West', 'KOST': 'posix/Pacific/Kosrae', 'IOT': 'posix/Indian/Chagos', 'NZDT': 'NZ', 'MYT': 'posix/Asia/Kuching', 'HKT': 'Hongkong', 'SYOT': 'posix/Antarctica/Syowa', 'IRST': 'Iran', 'HST': 'posix/US/Hawaii', 'CCT': 'posix/Indian/Cocos', 'GMT-10': 'posix/Etc/GMT-10', 'GMT-11': 'posix/Etc/GMT-11', 'GMT-12': 'posix/Etc/GMT-12', 'AMST': 'posix/America/Cuiaba', 'GMT-14': 'posix/Etc/GMT-14', 'MAWT': 'posix/Antarctica/Mawson', 'WSDT': 'posix/Pacific/Apia', 'BNT': 'posix/Asia/Brunei', 'WET': 'Portugal', 'KRAT': 'posix/Asia/Novokuznetsk', 'ACDT': 'posix/Australia/Yancowinna', 'BRST': 'posix/Brazil/East', 'ANAT': 'posix/Asia/Anadyr', 'CXT': 'posix/Indian/Christmas', 'UYT': 'posix/America/Montevideo', 'CKT': 'posix/Pacific/Rarotonga', 'HOVT': 'posix/Asia/Hovd', 'VUT': 'posix/Pacific/Efate', 'ALMT': 'posix/Asia/Almaty', 'NPT': 'posix/Asia/Katmandu', 'QYZT': 'posix/Asia/Qyzylorda', 'PHT': 'posix/Asia/Manila', 'KST': 'ROK', 'HDT': 'posix/US/Aleutian', 'EET': 'Libya', 'LHDT': 'posix/Australia/Lord_Howe', 'VLAT': 'posix/Asia/Vladivostok', 'SRET': 'posix/Asia/Srednekolymsk', 'WFT': 'posix/Pacific/Wallis', 'MART': 'posix/Pacific/Marquesas', 'PHOT': 'posix/Pacific/Enderbury', 'PKT': 'posix/Asia/Karachi', 'GET': 'posix/Asia/Tbilisi', 'TKT': 'posix/Pacific/Fakaofo', 'CET': 'Poland', 'EEST': 'Turkey', 'SCT': 'posix/Indian/Mahe', 'AMT': 'posix/Brazil/West', 'ChST': 'posix/Pacific/Saipan', 'MAGT': 'posix/Asia/Magadan', 'GMT+12': 'posix/Etc/GMT+12', 'WGT': 'posix/America/Godthab', 'GMT+10': 'posix/Etc/GMT+10', 'GMT+11': 'posix/Etc/GMT+11', 'AFT': 'posix/Asia/Kabul', 'CST': 'ROC', 'MHT': 'Kwajalein', 'MIST': 'posix/Antarctica/Macquarie', 'BTT': 'posix/Asia/Thimphu', 'BDT': 'posix/Asia/Dacca', 'SST': 'posix/US/Samoa', 'CHUT': 'posix/Pacific/Yap', 'NFT': 'posix/Pacific/Norfolk', 'TJT': 'posix/Asia/Dushanbe', 'TVT': 'posix/Pacific/Funafuti', 'ADT': 'posix/Canada/Atlantic', 'PST': 'posix/Pacific/Pitcairn', 'MUT': 'posix/Indian/Mauritius', 'DAVT': 'posix/Antarctica/Davis', 'TMT': 'posix/Asia/Ashkhabad', 'COT': 'posix/America/Bogota', 'PET': 'posix/America/Lima', 'CHADT': 'NZ-CHAT', 'RET': 'posix/Indian/Reunion', 'IST': 'Israel', 'GILT': 'posix/Pacific/Tarawa', 'FKST': 'posix/Atlantic/Stanley', 'AEDT': 'posix/Australia/Victoria', 'ACT': 'posix/Brazil/Acre', 'FJT': 'posix/Pacific/Fiji', 'IRKT': 'posix/Asia/Irkutsk', 'SAST': 'posix/Africa/Mbabane', 'ORAT': 'posix/Asia/Oral', 'AST': 'posix/Asia/Qatar', 'BST': 'posix/Pacific/Bougainville', 'GMT-2': 'posix/Etc/GMT-2', 'NUT': 'posix/Pacific/Niue', 'JST': 'Japan', 'ECT': 'posix/America/Guayaquil', 'AQTT': 'posix/Asia/Aqtobe', 'EAST': 'posix/Pacific/Easter', 'TAHT': 'posix/Pacific/Tahiti', 'MDT': 'Navajo', 'GMT+8': 'posix/Etc/GMT+8', 'GMT+9': 'posix/Etc/GMT+9', 'VET': 'posix/America/Caracas', 'MVT': 'posix/Indian/Maldives', 'TLT': 'posix/Asia/Dili', 'OMST': 'posix/Asia/Omsk', 'GMT+2': 'posix/Etc/GMT+2', 'PDT': 'posix/US/Pacific-New', 'GMT+4': 'posix/Etc/GMT+4', 'GMT+5': 'posix/Etc/GMT+5', 'GMT+6': 'posix/Etc/GMT+6', 'GMT+7': 'posix/Etc/GMT+7', 'SRT': 'posix/America/Paramaribo', 'CLT': 'posix/Chile/Continental', 'WAT': 'posix/Africa/Porto-Novo', 'NDT': 'posix/Canada/Newfoundland', 'GMT': 'GB-Eire', 'GMT-13': 'posix/Etc/GMT-13', 'WIB': 'posix/Asia/Pontianak', 'SBT': 'posix/Pacific/Guadalcanal', 'PYST': 'posix/America/Asuncion', 'MMT': 'posix/Asia/Rangoon', 'BRT': 'posix/America/Maceio', 'YAKT': 'posix/Asia/Yakutsk', 'CDT': 'Cuba', 'MET': 'posix/MET', 'WIT': 'posix/Asia/Jayapura', 'EDT': 'posixrules', 'SAKT': 'posix/Asia/Sakhalin', 'NOVT': 'posix/Asia/Novosibirsk', 'GALT': 'posix/Pacific/Galapagos', 'TFT': 'posix/Indian/Kerguelen', 'PONT': 'posix/Pacific/Ponape', 'CVT': 'posix/Atlantic/Cape_Verde', 'MST': 'posix/US/Arizona', 'VOST': 'posix/Antarctica/Vostok', 'WAST': 'posix/Africa/Windhoek', 'TOT': 'posix/Pacific/Tongatapu', 'CAT': 'posix/Africa/Maputo', 'GMT-1': 'posix/Etc/GMT-1', 'AEST': 'posix/Australia/Queensland', 'MSK': 'W-SU', 'AZT': 'posix/Asia/Baku', 'UCT': 'UCT', 'ACST': 'posix/Australia/North', 'ROTT': 'posix/Antarctica/Rothera', 'PETT': 'posix/Asia/Kamchatka', 'PGT': 'posix/Pacific/Port_Moresby', 'GYT': 'posix/America/Guyana', 'CHOT': 'posix/Asia/Choibalsan', 'GMT+1': 'posix/Etc/GMT+1', 'UZT': 'posix/Asia/Tashkent', 'GMT+3': 'posix/Etc/GMT+3', 'EAT': 'posix/Indian/Mayotte', 'UTC': 'Zulu', 'EST': 'Jamaica', 'WAKT': 'posix/Pacific/Wake', 'SGT': 'Singapore', 'ACWST': 'posix/Australia/Eucla', 'GMT-6': 'posix/Etc/GMT-6', 'GMT-8': 'posix/Etc/GMT-8', 'GMT-9': 'posix/Etc/GMT-9', 'ULAT': 'posix/Asia/Ulan_Bator', 'GMT-7': 'posix/Etc/GMT-7', 'GMT-4': 'posix/Etc/GMT-4', 'GMT-5': 'posix/Etc/GMT-5', 'AZOT': 'posix/Atlantic/Azores', 'GMT-3': 'posix/Etc/GMT-3', 'ICT': 'posix/Asia/Saigon', 'PWT': 'posix/Pacific/Palau', 'ART': 'posix/America/Mendoza', 'KGT': 'posix/Asia/Bishkek', 'NCT': 'posix/Pacific/Noumea', 'GFT': 'posix/America/Cayenne', 'DDUT': 'posix/Antarctica/DumontDUrville', 'YEKT': 'posix/Asia/Yekaterinburg', 'NRT': 'posix/Pacific/Nauru', 'SAMT': 'posix/Europe/Samara'}


class TimeConvertor(object):
    def __init__(self):
        self.machn_timezone = time.tzname[0]
        print self.machn_timezone

    @property
    def UTC_time(self):
        minutes_diff = TIME_DIFF.get(self.machn_timezone, 0)
        return datetime.now() - timedelta(minutes=minutes_diff)


    @staticmethod
    def process_time_input(time_input):
        """
        process timeinput to datetime
        :param time_input: str, datetime
        :return: datetime
        """
        if type(time_input) == datetime:
            ts = time_input
        elif type(time_input) == str:
            time_input = time_input.strip()
            if len(time_input) == 10:
                time_input += " 00:00:00"
            ts = datetime.strptime(time_input, '%Y-%m-%d %H:%M:%S')
        else:
            raise ValueError("time input must be str or datetime")

        return ts

    def convert_current_to_timezone(self, timezone_abbrev):
        """
        Convert current time on the machn to timezone
        :param timezone_abbrev: str
        :return: time_converted

        """
        minutes_diff = TIME_DIFF.get(timezone_abbrev.strip().upper(), None)

        if minutes_diff is None:
            raise ValueError("Could not recognize timezone {}".format(timezone_abbrev))
        return self.UTC_time + timedelta(minutes=minutes_diff)

    def convert_tztime_to_timezone(self, time_input, from_timezone, to_timezone):

        time_cal = self.process_time_input(time_input)

        from_tz_diff = TIME_DIFF.get(from_timezone.strip().upper(), 0)
        to_tz_diff = TIME_DIFF.get(to_timezone.strip().upper(), 0)

        return time_cal + timedelta(minutes=to_tz_diff - from_tz_diff)




