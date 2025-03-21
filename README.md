# QR-code-generator
This python program converts links into qr codes. 

📌 Overview  
This Python script reads a list of links from a file and generates QR codes for each link. The generated QR codes are saved as image files in a specified folder.  

🚀 Features  
- Reads links from a text file  
- Generates QR codes for each link  
- Saves QR codes as `.png` images  
- Easy to use and modify  

🛠️ Requirements  
Make sure you have Python installed along with the required dependency:  

```sh
pip install qrcode[pil]
```  

📂 Setup & Usage  

1. Clone the Repository 
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Prepare Your Links File
   - Create a text file (e.g., `links.txt`) in the specified folder.
   - Add one URL per line.

3. Modify the Script
   - Update the script to include the correct path to your `links.txt` file.
   - Set the destination folder where QR codes should be saved.

4. Run the Script
   ```sh
   python qr_generator.py
   ```

## 📜 Code  

```python
import qrcode

# Load generated links
with open(r"C:\path\to\your\links.txt", "r") as f:
    links = f.readlines()

# Create QR codes for each link
for i, link in enumerate(links):
    qr = qrcode.make(link.strip())  # Generate QR code
    qr.save(f"C:\\Users\\rites\\Desktop\\temp\\QR\\qr_code_{i+1}.png")

print("✅ QR Codes generated for all files!")
```

## 📌 Notes  
- Ensure that `links.txt` exists in the specified directory.  
- Update file paths accordingly before running the script.  
- The generated QR codes will be saved in the defined output folder.  

## 🖼️ Example  
Here’s an example of a generated QR code:  
![QR Code Example](https://dummyimage.com/200x200/000/fff&text=QR+Code)  

## 📜 License  
This project is open-source and available under the [MIT License](LICENSE).  
