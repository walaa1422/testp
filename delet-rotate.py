#شغال يحذف الروتيشن
import os

def delete_images_with_name(folder_path, target_name):
    # قراءة جميع ملفات الصور في المجلد
    image_files = os.listdir(folder_path)

    # حذف الصور التي تحتوي على الاسم المستهدف
    
    for image_file in image_files:
        if target_name in image_file:
            image_path = os.path.join(folder_path, image_file)
            os.remove(image_path)
            print(f" Deleted successfully : {image_file}")
            
 #Specify the target name of the images to be deleted
target_name = "rotated"

#تغير اسم الباث
folder_path = "C:/Users/n67-m/Downloads/not fractured-v"
# حذف الصور التي تحتوي على الاسم المستهدف
delete_images_with_name(folder_path, target_name)