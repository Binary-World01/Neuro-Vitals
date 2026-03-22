file = r'c:\Users\Parth\OneDrive\Desktop\PuneHack\neuro-vitals\frontend-app\index.html'
content = open(file, 'r', encoding='utf-8').read()
content = content.replace(' rounded px-3 py-1.5 text-xs cursor', ' rounded-lg px-3 py-1.5 text-xs cursor')
open(file, 'w', encoding='utf-8').write(content)
print('Dropdown updated to rounded-lg!')
