#cell1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/reverse1999_history_clean.csv", parse_dates=["summon_time"])
df.head()
#cell2
print("จำนวนทั้งหมดของ pulls:", len(df))
print("\nจำนวนครั้งต่อ banner:\n")
print(df["banner"].value_counts())
#cell3
plt.figure(figsize=(12,4))
df['summon_time'].value_counts().sort_index().plot()
plt.title("Reverse 1999 Pull Timeline")
plt.xlabel("Date")
plt.ylabel("Number of pulls")
plt.show()
#cell4
plt.figure(figsize=(10,8))
df['unit_name'].value_counts().plot(kind='bar')
plt.title("จำนวนตัวละครที่ออกทั้งหมด")
plt.show()
#cell5
# สร้าง rarity column แบบง่าย
six_star_ids = [3030, 3018]  # ตัวอย่าง: ให้เธอบอกว่าอันไหนเป็น 6★

df["rarity"] = df["unit_id"].apply(lambda x: 6 if x in six_star_ids else 5)

df["rarity"].value_counts()
#cell6
df = df.sort_values("summon_time").reset_index(drop=True)

pity_count = 0
pity_list = []

six = [3030, 3018]  # บอกฉันได้นะ เดี๋ยวฉันใส่ให้ครบทุกตัว

for _, row in df.iterrows():
    pity_count += 1
    if row["unit_id"] in six:
        pity_list.append(pity_count)
        pity_count = 0  # reset

pity_list
#result
sns.histplot(pity_list, bins=range(1, max(pity_list)+2))
plt.title("Distribution จนกว่าจะออก 6★")
plt.xlabel("จำนวน pulls")
plt.show()

