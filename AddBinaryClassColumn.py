import pandas as pd

# Đọc file CSV
input_file = "data/train.csv"  # Tên file CSV dataset gốc
output_file = "data/train_binary.csv"  # Tên file CSV dataset kết quả

# Load file CSV
df = pd.read_csv(input_file)

# Hàm xác dịnh Binary class dựa trên Label
def get_binary_class(label):
   if label == 'BenignTraffic':
      return 'Benign'
   return 'Attack'

# Thêm cột Binary class dựa trên Label
df['Binary Class'] = df['Label'].apply(get_binary_class)

df.to_csv(output_file, index=False)

print(f"File đã được lưu vào: {output_file}")
