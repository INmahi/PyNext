from wordcloud import WordCloud
import numpy as np
from PIL import Image

# Load the mask image (text "Outliers" written in black on white)
mask = np.array(Image.open("outliers_mask.png"))

# Student names (repeat them for weighting)
names = [
    "Efath", "Mahi", "Ariyan", "Farin", "Taif", "Sajid", "Nadman", "Dhrubo",
    "Papon", "Prince", "Emtiaz", "Musfiq", "Prodeepta", "Ayon", "Showmik",
    "Samiul", "Tanvir", "Supti", "Ilham", "Mashrafe", "Amiya", "Prionty",
    "Zihad", "Jayed", "Tushan", "Faiza", "Shihab", "Ikfat", "Abir", "Kusum",
    "Shajida", "Nomro", "Dola", "Ragib", "Ratul", "Jerin", "Farhan", "Rahat",
    "Akib", "Shahrin", "Araf", "Shanat", "Rifat", "Jarif", "Muslim", "Authoi",
    "Sadman", "Mimi", "Nahim", "Rishta", "Abid", "Jahirul", "Arnob", "Tanisha",
    "Abrar", "Junayed", "Shomu", "Simanta", "Shanto", "Mueed", "Nabil",
    "Rizwanur", "Likhon", "Neon", "Ishmam", "Zunaid", "Mostafizur", "Rifat",
    "Tanisha", "Sami", "Ramim", "Tanusree", "Mashrur","Efath", "Mahi", "Ariyan", "Farin", "Taif", "Sajid", "Nadman", "Dhrubo",
    "Papon", "Prince", "Emtiaz", "Musfiq", "Prodeepta", "Ayon", "Showmik",
    "Samiul", "Tanvir", "Supti", "Ilham", "Mashrafe", "Amiya", "Prionty",
    "Zihad", "Jayed", "Tushan", "Faiza", "Shihab", "Ikfat", "Abir", "Kusum",
    "Shajida", "Nomro", "Dola", "Ragib", "Ratul", "Jerin", "Farhan", "Rahat",
    "Akib", "Shahrin", "Araf", "Shanat", "Rifat", "Jarif", "Muslim", "Authoi",
    "Sadman", "Mimi", "Nahim", "Rishta", "Abid", "Jahirul", "Arnob", "Tanisha",
    "Abrar", "Junayed", "Shomu", "Simanta", "Shanto", "Mueed", "Nabil",
    "Rizwanur", "Likhon", "Neon", "Ishmam", "Zunaid", "Mostafizur", "Rifat",
    "Tanisha", "Sami", "Ramim", "Tanusree", "Mashrur"
]

text = " ".join(names)

# Generate word cloud
wc = WordCloud(background_color="black", mask=mask,
               contour_color="black", contour_width=2,
               colormap="cool").generate(text)

# Save output
wc.to_file("outliers_names.png")
