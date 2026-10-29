import os, shutil

base_dir = r'c:\Users\welcome\Documents\@MY PROJECTS@\AI JOB FINDER\LUCKY'
www_dir = os.path.join(base_dir, 'www')

os.makedirs(www_dir, exist_ok=True)

files_to_copy = [
    'index.html', 'jobs.json', 'manifest.json', 'sw.js', 'home-screen-reference.svg',
    'icon-192.png', 'icon-512.png', 'screenshot-mobile.png', 'screenshot-desktop.png'
]

for f in files_to_copy:
    src = os.path.join(base_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(www_dir, f))
        print(f"Copied {f} to www/")

print("www/ folder prepared successfully for Android packaging!")
