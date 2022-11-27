import os
import shutil


root_direct = input(f"Please enter the full path to the folder to sort the files: ")
try:
    dir = os.listdir(root_direct)
except FileNotFoundError:
    print(f"The path '{root_direct}' does not exist, please make sure it is typed correctly.")

try:
    os.mkdir(fr"{root_direct}\video")
except FileExistsError:
    pass
try:
    os.mkdir(fr"{root_direct}\audio")
except FileExistsError:
    pass
try:
    os.mkdir(fr"{root_direct}\archives")
except FileExistsError:
    pass
try:
    os.mkdir(fr"{root_direct}\images")
except FileExistsError:
    pass
try:
    os.mkdir(fr"{root_direct}\documents")
except FileExistsError:
    pass
try:
    os.mkdir(fr"{root_direct}\others")
except FileExistsError:
    pass

docs = (".doc", ".docx", ".txt", ".pdf", ".xlxs", ".xlx", ".pptx", ".ppt", ".csv")
images = (".jpeg", ".png", ".jpg", ".svg")
video = (".avi", ".mp4", ".mov", ".mkv")
audio = (".mp3", ".ogg", ".wav", ".amr")
archives = (".zip", ".rar", ".gz", ".tar")

path_trash = list()



filter_dir = (fr"{root_direct}", fr"{root_direct}\video", fr"{root_direct}\audio", fr"{root_direct}\archives",
              fr"{root_direct}\images", fr"{root_direct}\documents", fr"{root_direct}\others")

translation = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i',
               'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
               'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
               'э': 'e', 'ю': 'yu', 'я': 'ya', 'є': 'je', 'і': 'i', 'ї': 'ji', 'ґ': 'g', 'А': 'A', 'Б': 'B', 'В': 'V',
               'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L',
               'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
               'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
               'Є': 'Je', 'І': 'I', 'Ї': 'Ji', 'Ґ': 'G'}

punct_symbols = "!#$%&'\"()*+,№-/:;<=>?@[\]^_`{|}~"


def normalize(text):
    for c in punct_symbols:
        if c in text:
            text = text.replace(c, '_')

    for c in translation.keys():
        text = text.replace(c, translation[c])
    return text


for path, direct, files in os.walk(root_direct):
    path_trash.append(path)

    for file in files:

        if file.endswith(docs):
            try:
                shutil.move(os.path.join(f"{path}", f"{file}"), os.path.join(f"{root_direct}",
                                                                             "documents", f"{normalize(file)}"))
            except shutil.Error:
                pass

        elif file.endswith(images):
            try:
                shutil.move(os.path.join(f"{path}", f"{file}"), os.path.join(f"{root_direct}", "images",
                                                                             f"{normalize(file)}"))
            except shutil.Error:
                pass

        elif file.endswith(video):
            try:
                shutil.move(os.path.join(f"{path}", f"{file}"), os.path.join(f"{root_direct}", "video",
                                                                             f"{normalize(file)}"))
            except shutil.Error:
                pass

        elif file.endswith(audio):
            try:
                shutil.move(os.path.join(f"{path}", f"{file}"), os.path.join(f"{root_direct}", "audio",
                                                                             f"{normalize(file)}"))
            except shutil.Error:
                pass
        elif file.endswith(archives):

            old_file = os.path.join(path, file)
            new_file = os.path.join(path, normalize(file))
            os.rename(old_file, new_file)
            archive_dir = os.path.basename(new_file).split('.')[0]
            archive_rormat = new_file.split('.')[-1]
            archive_files = list()
            archive_files.append(new_file)
            print(archive_files)
            print(archive_dir)

            if archive_rormat == "rar":
                try:
                    shutil.move(new_file, os.path.join(f"{root_direct}", "archives"))
                except shutil.Error:
                    pass

            else:
                shutil.unpack_archive(new_file, os.path.join(f"{root_direct}","archives", f"{archive_dir}"),
                                      format=archive_rormat)

        # elif file.endswith(archives):
        #     old_file = os.path.join(path, file)
        #     new_file = os.path.join(path, normalize(file))
        #     os.rename(old_file, new_file)
        #     archive_dir = os.path.basename(new_file).split('.')[0]
        #     archive_rormat = new_file.split('.')[-1]
        #     archive_files = list()
        #     archive_files.append(new_file)
        #     print(archive_files)
        #     for new_file in archive_files:
        #         try:
        #             shutil.unpack_archive(new_file, fr"{root_direct}\archives\{archive_dir}", format=archive_rormat)
        #         except:
        #             try:
        #                 shutil.move(new_file, fr"{root_direct}\archives")
        #             except:
        #                 continue
        else:
            try:
                shutil.move(os.path.join(f"{path}", f"{file}"), os.path.join(f"{root_direct}", "others"))
            except shutil.Error:
                pass

for path, direct, files in os.walk(root_direct):
    dir_del = list(set(path_trash) - set(filter_dir))

    for dir_path in dir_del:
        shutil.rmtree(dir_path, ignore_errors=True)

