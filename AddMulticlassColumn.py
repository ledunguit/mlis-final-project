import pandas as pd

# Định nghĩa danh mục và nhãn
categories = {
    "DDoS": [
        "DDoS-TCP_Flood", "DDoS-ICMP_Fragmentation", "DDoS-SYN_Flood",
        "DDoS-PSHACK_Flood", "DDoS-SynonymousIP_Flood", "DDoS-ACK_Fragmentation",
        "DDoS-RSTFINFlood", "DDoS-UDP_Flood", "DDoS-UDP_Fragmentation",
        "DDoS-ICMP_Flood", "DDoS-HTTP_Flood", "DDoS-SlowLoris"
    ],
    "DoS": [
        "DoS-UDP_Flood", "DoS-TCP_Flood", "DoS-SYN_Flood", "DoS-HTTP_Flood"
    ],
    "Mirai": [
        "Mirai-greip_flood", "Mirai-greeth_flood", "Mirai-udpplain"
    ],
    "Benign": [
        "BenignTraffic"
    ],
    "Spoofing": [
        "MITM-ArpSpoofing", "DNS_Spoofing"
    ],
    "Recon": [
        "Recon-HostDiscovery", "Recon-OSScan", "Recon-PortScan",
        "Recon-PingSweep", "VulnerabilityScan"
    ],
    "Web": [
        "CommandInjection", "SqlInjection", "XSS",
        "BrowserHijacking", "Uploading_Attack"
    ],
    "BruteForce": [
        "DictionaryBruteForce"
    ],
    "Malware": [
        "Backdoor_Malware"
    ]
}

# Đọc file CSV
input_file = "data/train.csv"  # Tên file CSV dataset gốc
output_file = "data/train_multiclass.csv"  # Tên file CSV dataset kết quả

# Load file CSV
df = pd.read_csv(input_file)

# Hàm xác dịnh Multiclass
def get_multiclass(label):
    for category, labels in categories.items():
        if label in labels:
            return category
    return "Unknown"

# Thêm cột Multiclass dựa trên Label
df['Multiclass'] = df['Label'].apply(get_multiclass)

df.to_csv(output_file, index=False)

print(f"File đã được lưu vào: {output_file}")
