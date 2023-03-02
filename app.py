import requests
import json
import mariadb

page_url = "https://www.ketto.org/api/fundraisers/treatment-754024/donors?search=&limit=&orderBy=donated_amount&sortedBy=desc&showError=false"

page = requests.get(page_url)
data = json.loads(page.text)
x = data['data']['data']

conn = mariadb.connect(
    user="root",
    password="123456789",
    host="localhost",
    port=3306,
    database="FundraiserDatabase")
cur = conn.cursor()

# for row in rows:
#     print(row)

try:
    for i in x:
        sql1 = "SELECT id FROM `fundraisers` WHERE id={}".format(i['id'])
        cur.execute(sql1)
        rows = cur.fetchall()
    
        if len(rows) == 0:
            sql = "INSERT INTO `fundraisers` (`id`,`donated_amount`,`donated_amount_usd`,`donated_amount_local`,`name`,`iso_currency`,`donor_entity_details_id`,`is_anonymous`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (i['id'],i['donated_amount'],i['donated_amount_usd'],i['donated_amount_local'],i['name'],i['iso_currency'],i['donor_entity_details_id'],i['is_anonymous'])
            cur.execute(sql, val)
            conn.commit()
            print("id={}\ndonated_amount={}\ndonated_amount_usd={}\ndonated_amount_local={}\nname={}\niso_currency={}\ndonor_entity_details_id={}\nis_anonymous={}\n\n".format(i['id'],i['donated_amount'],i['donated_amount_usd'],i['donated_amount_local'],i['name'],i['iso_currency'],i['donor_entity_details_id'],i['is_anonymous']))


except mariadb.Error as e:
    print(f"Error: {e}")
cur.close()




