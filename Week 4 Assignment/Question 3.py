# Date Converter By Sarjyant

bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]


def convert_date(date_str, from_cal, to_cal):
    if from_cal == to_cal:
        return date_str

    year = int(date_str[0:4])
    month = date_str[5:7]
    day = date_str[8:10]

    if from_cal == "AD" and to_cal == "BS":
        year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        year = year - 56

    return str(year) + "-" + month + "-" + day


for customer in customers:
    converted = convert_date(customer["date"], customer["cal"], customer["need"])
    year, month, day = converted.split("-")

    if customer["style"] == "iso":
        display = converted + " " + customer["need"]
    else:
        month_name = bs_months[int(month) - 1] if customer["need"] == "BS" else month
        display = day + " " + month_name + ", " + year + " " + customer["need"]

    print(customer["name"], "| Original:", customer["date"], customer["cal"], "| Converted:", display)