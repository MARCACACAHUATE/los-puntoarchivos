
categorias = {
    "elfinanciero": [
        "https://www.elfinanciero.com.mx/tv/",
        "https://www.elfinanciero.com.mx/economia/",
        "https://www.elfinanciero.com.mx/empresas/",
        "https://www.elfinanciero.com.mx/nacional/",
        "https://www.elfinanciero.com.mx/FoxSports/",
        "https://www.elfinanciero.com.mx/bloomberg-businessweek/",
        "https://www.elfinanciero.com.mx/salud/",
        "https://www.elfinanciero.com.mx/suplementos/",
        "https://www.elfinanciero.com.mx/mundo-empresa/",
        "https://www.elfinanciero.com.mx/mundo/",
        "https://www.elfinanciero.com.mx/tech/",
    ],
    "eluniversal": [],
    "larepublica": [],
    "jornada": [],
}


xpath_paginas = {
    "elfinanciero": {
        "pagina_principal": {
            "noticias_populares": '//section[@id="main"]//section[2]//a[contains(@class, "headline")]/@href',
            "noticias_principales": "//section[@id='main']//section[1]//a/@href",    
        },
        "categorias": {

        },
        "noticias": {

        }
    },
    "eluniversal": {},
    "larepublica": {},
    "jornada": {},
}