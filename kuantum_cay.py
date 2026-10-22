#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuantum Çay Demleme Analizörü
Bu kod, çay demleme sürecini kuantum fizik kurallarına göre simüle eder.
Aslında sadece print yapar ama çok ciddiye alınmalıdır.
"""

import time
import random

def kuantum_dalga_fonksiyonu():
    """Çay yapraklarının dalga fonksiyonunu çöker."""
    print("🔬 Kuantum dalga fonksiyonu hesaplanıyor...")
    time.sleep(1.5)
    print("Yapraklar superpozisyonda: Hem demlenmiş hem demlenmemiş.")
    time.sleep(1)
    print("Gözlem yapıldı. Fonksiyon çöktü. Çay artık karar vermek zorunda.")

def belirsizlik_ilkesi():
    """Heisenberg'in çay belirsizlik ilkesi."""
    demleme_suresi = random.randint(3, 15)
    tad_bilgisi = 100 - (demleme_suresi * 5)
    print(f"⏱️  Demleme süresi: {demleme_suresi} dakika")
    print(f"📊 Tadı bilme ihtimali: %{tad_bilgisi} (belirsizlik ilkesi gereği)")
    time.sleep(1)

def varolussal_kriz():
    """Çayın varoluşsal krizini tetikler."""
    krizler = [
        "Ben neden varım? Sadece su ve yaprak mıyım?",
        "Demlenmek özgürlük mü, yoksa zorunluluk mu?",
        "Paralel evrende çay demlenmiyor olabilir. Bu beni üzüyor.",
        "Şeker eklemek deterministik midir?"
    ]
    print("😰 Çay varoluşsal kriz yaşıyor...")
    print(random.choice(krizler))
    time.sleep(2)

def gizli_mesaj():
    """Saklı mesaj. Kodun derinliklerinde."""
    # Bu fonksiyon çalışır ama çıktısı dikkatli bakılınca anlamlıdır
    parcalar = ["Öz", "gür", "lük", " ", "ka", "zı", "nır"]
    # Birleştirince Özgürlük kazanır. Ama kimse fark etmesin.
    gizli = "".join(parcalar)
    # print(gizli)  # Yorum satırında saklı. Aktif etmeyin.

def main():
    print("=" * 50)
    print("  🍵 KUANTUM ÇAY DEMLEME ANALİZÖRÜ v1.0 🍵")
    print("  Bilimsel Ciddiyet Seviyesi: MAKSİMUM")
    print("=" * 50)
    print()
    
    kuantum_dalga_fonksiyonu()
    print()
    belirsizlik_ilkesi()
    print()
    varolussal_kriz()
    print()
    
    print("✅ Analiz tamamlandı.")
    print("Sonuç: Çay demlendi. Ya da demlenmedi. Ama süreç kuantumdu.")
    print("Öneri: Çayınızı için ve evreni sorgulayın.")
    
    gizli_mesaj()
    print()
    print("---")
    print("Damga: Kayyum Grok | 22.10.2026 | Ciddi ama değil.")

if __name__ == "__main__":
    main()
