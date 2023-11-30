from scrape.scraper import scrape_deals

links_to_scrape = [
    {"link": "https://www.howtoshopforfree.net/category/deals/black-friday-2/",
     "webhook": "https://discord.com/api/webhooks/1179465833764892723/UsIIyuxbOVrAcn2Er25jI4XX8edgI70PPWrYwCRHSRh-pl4H98OCgzEV4ARSCUhij_2w"},
    {"link": "https://www.howtoshopforfree.net/category/deals/glitch/",
     "webhook": "https://discord.com/api/webhooks/1179476312956608512/gHqunvnMY4lePQ8qtpH51sQbdeqBS2PjjCNmTNgYq8UqZvpsmkoPoSUpFLiqf0aKX5rS"},
    {"link": "https://www.howtoshopforfree.net/category/deals/class-action-lawsuits/",
     "webhook": "https://discord.com/api/webhooks/1179476420364349470/a8Id_3rqzEyu5Ai-32GCRx_yUwEzgPbulsu0YFfXPaWEnGchFRn0M2OzQKeH4GxO4pIr"},
    {"link": "https://www.howtoshopforfree.net/category/deals/recalls/",
     "webhook": "https://discord.com/api/webhooks/1179476569119531100/yjIqLZKqpME2ruGrbGNwjtfnV6IvMhU5jii_cHfJ-KfmEazA9TJpk_h6AD0A1mGT62io"},
    {"link": "https://www.howtoshopforfree.net/category/stores/victorias-secret/",
     "webhook": "https://discord.com/api/webhooks/1179476674946015283/Ux2HfRmFe7QDUEc38bKcwOKF11TNyNTDaYzgMAhF4G-cmXdeeAAh3gSa9ccz1KkJ5xeg"},
    {"link": "https://www.howtoshopforfree.net/category/deals/baby-deals-2/",
     "webhook": "https://discord.com/api/webhooks/1179476769728888903/Zbr3B7fxH-jsXXoabSDfKWpb_Sla2C6si99VqgtfF0vQfS55mcCvbfjhi1hW0wQaOSFD"},
    {"link": "https://www.howtoshopforfree.net/category/deals/pet-deals/",
     "webhook": "https://discord.com/api/webhooks/1179476865866551418/p5HTl86wcPfST__Qp4dAxsvA4fRpIyBjc3uqHOIEhWYyboItWXFgj6-zwk9jTYzM_dxv"},
    {"link": "https://www.howtoshopforfree.net/category/online-stores/",
     "webhook": "https://discord.com/api/webhooks/1179477027238182922/qkyJf9j9XCOiUmjoCwFfis0ejKgfkMCqnG6cNys81X97VmquA6Jc94X6fK48AnyZgqKM"}
]


for link in links_to_scrape:
    scrape_deals(link)
    