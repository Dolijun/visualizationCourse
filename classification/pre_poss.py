import os
import cv2

root = "dataset_delete_test"
for fruit in os.listdir(root):
    for file in os.listdir(os.path.join(root, fruit)):
        file_path = os.path.join(root, fruit, file)
        img = cv2.imread(file_path)
        if img is None:
            print(file_path, "read error")
            os.remove(file_path)
        else:
            try:
                channel = img.shape[2]
                if channel != 3:
                    print(file_path, "channel != 3")
                    os.remove(file_path)
            except:
                print(file_path, "channel error")
                os.remove(file_path)

