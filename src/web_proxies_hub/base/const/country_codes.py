"""
    Country codes in ISO 3166-1 alpha-2 format.
    Source: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
    Accept accross all this project.
"""


COUNTRY_CODES = [
    "AF",  # Afeganistão
    "AL",  # Albânia
    "DZ",  # Argélia
    "AD",  # Andorra
    "AO",  # Angola
    "AI",  # Anguila
    "AQ",  # Antártida
    "AG",  # Antígua e Barbuda
    "AR",  # Argentina
    "AM",  # Armênia
    "AW",  # Aruba
    "AU",  # Austrália
    "AT",  # Áustria
    "AZ",  # Azerbaijão
    "BS",  # Bahamas
    "BH",  # Barein
    "BD",  # Bangladesh
    "BB",  # Barbados
    "BY",  # Bielorrússia
    "BE",  # Bélgica
    "BZ",  # Belize
    "BJ",  # Benin
    "BM",  # Bermudas
    "BT",  # Butão
    "BO",  # Bolívia
    "BA",  # Bósnia e Herzegovina
    "BW",  # Botsuana
    "BR",  # Brasil
    "BN",  # Brunei
    "BG",  # Bulgária
    "BF",  # Burquina Faso
    "BI",  # Burundi
    "BV",  # Ilha Bouvet
    "KH",  # Camboja
    "CM",  # Camarões
    "CA",  # Canadá
    "CV",  # Cabo Verde
    "KY",  # Ilhas Cayman
    "CF",  # República Centro-Africana
    "TD",  # Chade
    "CL",  # Chile
    "CN",  # China
    "CX",  # Ilha Christmas
    "CC",  # Ilhas Cocos
    "CO",  # Colômbia
    "KM",  # Comores
    "CG",  # Congo
    "CD",  # República Democrática do Congo
    "CK",  # Ilhas Cook
    "CR",  # Costa Rica
    "CI",  # Costa do Marfim
    "HR",  # Croácia
    "CU",  # Cuba
    "CY",  # Chipre
    "CZ",  # República Tcheca
    "DK",  # Dinamarca
    "DJ",  # Djibuti
    "DM",  # Dominica
    "DO",  # República Dominicana
    "EC",  # Equador
    "EG",  # Egito
    "SV",  # El Salvador
    "AE",  # Emirados Árabes Unidos
    "ER",  # Eritreia
    "EE",  # Estônia
    "ET",  # Etiópia
    "FK",  # Ilhas Malvinas
    "FO",  # Ilhas Faroé
    "FJ",  # Fiji
    "FI",  # Finlândia
    "FR",  # França
    "GF",  # Guiana Francesa
    "PF",  # Polinésia Francesa
    "TF",  # Territórios Franceses do Sul
    "GA",  # Gabão
    "GM",  # Gâmbia
    "GE",  # Geórgia
    "DE",  # Alemanha
    "GH",  # Gana
    "GI",  # Gibraltar
    "GR",  # Grécia
    "GL",  # Groenlândia
    "GD",  # Granada
    "GP",  # Guadalupe
    "GU",  # Guam
    "GT",  # Guatemala
    "GG",  # Guernsey
    "GN",  # Guiné
    "GW",  # Guiné-Bissau
    "GY",  # Guiana
    "HT",  # Haiti
    "HK",  # Hong Kong
    "HU",  # Hungria
    "IS",  # Islândia
    "IN",  # Índia
    "ID",  # Indonésia
    "IR",  # Irã
    "IQ",  # Iraque
    "IE",  # Irlanda
    "IM",  # Ilha de Man
    "IL",  # Israel
    "IT",  # Itália
    "JM",  # Jamaica
    "JP",  # Japão
    "JE",  # Jersey
    "JO",  # Jordânia
    "KZ",  # Cazaquistão
    "KE",  # Quênia
    "KI",  # Quiribati
    "KP",  # Coreia do Norte
    "KR",  # Coreia do Sul
    "KW",  # Kuwait
    "KG",  # Quirguistão
    "LA",  # Laos
    "LV",  # Letônia
    "LB",  # Líbano
    "LS",  # Lesoto
    "LR",  # Libéria
    "LY",  # Líbia
    "LI",  # Liechtenstein
    "LT",  # Lituânia
    "LU",  # Luxemburgo
    "MO",  # Macau
    "MK",  # Macedônia
    "MG",  # Madagascar
    "MW",  # Malaui
    "MY",  # Malásia
    "MV",  # Maldivas
    "ML",  # Mali
    "MT",  # Malta
    "MH",  # Ilhas Marshall
    "MQ",  # Martinica
    "MR",  # Mauritânia
    "MU",  # Maurício
    "YT",  # Mayotte
    "MX",  # México
    "FM",  # Micronésia
    "MD",  # Moldávia
    "MC",  # Mônaco
    "MN",  # Mongólia
    "ME",  # Montenegro
    "MA",  # Marrocos
    "MZ",  # Moçambique
    "MM",  # Mianmar
    "NA",  # Namíbia
    "NR",  # Nauru
    "NP",  # Nepal
    "NL",  # Holanda
    "AN",  # Antilhas Holandesas
    "NC",  # Nova Caledônia
    "NZ",  # Nova Zelândia
    "NI",  # Nicarágua
    "NE",  # Níger
    "NG",  # Nigéria
    "NU",  # Niue
    "NF",  # Ilha Norfolk
    "MP",  # Ilhas Marianas do Norte
    "NO",  # Noruega
    "OM",  # Omã
    "PK",  # Paquistão
    "PW",  # Palau
    "PS",  # Palestina
    "PA",  # Panamá
    "PG",  # Papua-Nova Guiné
    "PY",  # Paraguai
    "PE",  # Peru
    "PH",  # Filipinas
    "PN",  # Ilhas Pitcairn
    "PL",  # Polônia
    "PT",  # Portugal
    "PR",  # Porto Rico
    "QA",  # Qatar
    "RE",  # Reunião
    "RO",  # Romênia
    "RU",  # Rússia
    "RW",  # Ruanda
    "BL",  # São Bartolomeu
    "SH",  # Santa Helena
    "KN",  # São Cristóvão e Neves
    "LC",  # Santa Lúcia
    "MF",  # São Martim
    "PM",  # Saint Pierre e Miquelon
    "VC",  # São Vicente e Granadinas
    "WS",  # Samoa
    "SM",  # San Marino
    "ST",  # São Tomé e Príncipe
    "SA",  # Arábia Saudita
    "SN",  # Senegal
    "RS",  # Sérvia
    "SC",  # Seicheles
    "SL",  # Serra Leoa
    "SG",  # Singapura
    "SK",  # Eslováquia
    "SI",  # Eslovênia
    "SB",  # Ilhas Salomão
    "SO",  # Somália
    "ZA",  # África do Sul
    "GS",  # Geórgia do Sul e Ilhas Sandwich do Sul
    "ES",  # Espanha
    "LK",  # Sri Lanka
    "SD",  # Sudão
    "SR",  # Surinam
    "SJ",  # Svalbard e Jan Mayen
    "SZ",  # Eswatini
    "SE",  # Suécia
    "CH",  # Suíça
    "SY",  # Síria
    "TW",  # Taiwan
    "TJ",  # Tajiquistão
    "TZ",  # Tanzânia
    "TH",  # Tailândia
    "TL",  # Timor-Leste
    "TG",  # Togo
    "TK",  # Tokelau
    "TO",  # Tonga
    "TT",  # Trinidad e Tobago
    "TN",  # Tunísia
    "TR",  # Turquia
    "TM",  # Turcomenistão
    "TV",  # Tuvalu
    "UG",  # Uganda
    "UA",  # Ucrânia
    "GB",  # Reino Unido
    "US",  # Estados Unidos
    "UY",  # Uruguai
    "UZ",  # Uzbequistão
    "VU",  # Vanuatu
    "VA",  # Vaticano
    "VE",  # Venezuela
    "VN",  # Vietnã
    "VG",  # Ilhas Virgens Britânicas
    "VI",  # Ilhas Virgens dos EUA
    "WF",  # Wallis e Futuna
    "EH",  # Saara Ocidental
    "YE",  # Iêmen
    "ZM",  # Zâmbia
    "ZW",  # Zimbábue
]