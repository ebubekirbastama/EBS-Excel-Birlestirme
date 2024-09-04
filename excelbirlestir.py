import pandas as pd
import glob
import os

# Mevcut çalışma dizinini alın
current_directory = os.getcwd()

# Excel dosyalarının bulunduğu dizinde çalıştığınızdan emin olun
dosyalar = glob.glob(os.path.join(current_directory, '*.xlsx'))

# Dosyaları okuyun ve birleştirin
df_listesi = [pd.read_excel(dosya) for dosya in dosyalar]
birlesik_df = pd.concat(df_listesi, ignore_index=True)

# Birleştirilmiş veriyi yeni bir dosyaya kaydedin
birlesik_df.to_excel(os.path.join(current_directory, 'birlesik_dosya.xlsx'), index=False)
