import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save():
    url = entry_url.get().strip()
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL.")
        return

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        titles = []
        prices = []
        ratings = []

        products = soup.find_all("article", class_="product_pod")

        for product in products:
            title = product.h3.a["title"]
            price = product.find("p", class_="price_color").text.strip()
            rating_class = product.find("p")["class"]
            rating = rating_class[1]

            titles.append(title)
            prices.append(price)
            ratings.append(rating)

        df = pd.DataFrame({
            "Title": titles,
            "Price": prices,
            "Rating": ratings
        })

        df.to_csv("products.csv", index=False)
        messagebox.showinfo("Success", "Scraping complete! Data saved to products.csv")
        print("File saved as products.csv")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("E-commerce Scraper")
root.geometry("400x200")

label = tk.Label(root, text="Enter E-commerce Page URL:", font=("Arial", 12))
label.pack(pady=10)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

scrape_button = tk.Button(root, text="Scrape & Save", command=scrape_and_save)
scrape_button.pack(pady=20)

root.mainloop()
