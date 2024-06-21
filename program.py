import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk

def normalize_image(image, min_val, max_val):
    normalized_image = np.clip((image - min_val) / (max_val - min_val) * 255, 0, 255)
    return normalized_image.astype(np.uint8)

def apply_colormap(image_path, colormap, min_val, max_val):
    # Load the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Could not read the image.")
    else:
        # Normalize the image dynamically
        normalized_image = normalize_image(image, min_val, max_val)
        
        # Apply the chosen colormap
        colored_image = cv2.applyColorMap(normalized_image, colormap)

        return colored_image

def select_image():
    global input_image_path
    input_image_path = filedialog.askopenfilename()

def apply_colormap_and_display():
    selected_colormap_index = colormap_dropdown.current()  # Get the selected index
    colormap = colormaps[selected_colormap_index]
    min_val = min_slider.get()
    max_val = max_slider.get()
    
    colored_image = apply_colormap(input_image_path, colormap, min_val, max_val)
    cv2.imshow("Colored Image", colored_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = ""  # Placeholder for the selected image path
    
    colormaps = [
        cv2.COLORMAP_JET,
          cv2.COLORMAP_HOT,
        cv2.COLORMAP_PINK,
        cv2.COLORMAP_SUMMER,
        cv2.COLORMAP_INFERNO,
        cv2.COLORMAP_CIVIDIS,
        cv2.COLORMAP_DEEPGREEN,
        cv2.COLORMAP_PARULA,
        cv2.COLORMAP_VIRIDIS,
        cv2.COLORMAP_BONE,
        cv2.COLORMAP_MAGMA,
        cv2.COLORMAP_OCEAN,
        cv2.COLORMAP_WINTER,
        cv2.COLORMAP_PLASMA,
        cv2.COLORMAP_COOL,
        cv2.COLORMAP_SPRING,
        cv2.COLORMAP_AUTUMN,
        # ... add more colormaps as needed ...
    ]
    
    root = tk.Tk()
    root.title("Colormap App")
    
    select_button = tk.Button(root, text="Select Image", command=select_image)
    select_button.pack()
    
    colormap_dropdown = ttk.Combobox(root, values=["Jet","hot","pink","summer","inferno","cividis","Parula","Viridis","Bone","Magma","Ocean","Winter","Plasma","Cool","Spring","Autumn"])
    colormap_dropdown.pack()
    
    min_label = tk.Label(root, text="Min Value:")
    min_label.pack()
    min_slider = tk.Scale(root, from_=0, to=255, orient="horizontal")
    min_slider.pack()
    
    max_label = tk.Label(root, text="Max Value:")
    max_label.pack()
    max_slider = tk.Scale(root, from_=0, to=255, orient="horizontal")
    max_slider.pack()
    
    display_button = tk.Button(root, text="Apply Colormap and Display", command=apply_colormap_and_display)
    display_button.pack()
    
    root.mainloop()
