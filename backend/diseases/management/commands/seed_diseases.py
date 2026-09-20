from django.core.management.base import BaseCommand

from diseases.models import Disease

DISEASES = [
    dict(
        slug="brown-spot", name="Brown Spot", scientific_name="Bipolaris oryzae",
        risk_level=Disease.RiskLevel.MEDIUM,
        short_description="Bercak coklat oval pada permukaan daun, disebabkan jamur Bipolaris oryzae.",
        description=(
            "Brown Spot atau bercak cokelat adalah penyakit pada tanaman padi yang disebabkan oleh jamur "
            "Bipolaris oryzae. Penyakit ini dapat menyerang bibit, daun, pelepah, dan bagian gabah. Pada daun "
            "tanaman dewasa, gejala utamanya berupa bercak berbentuk bulat hingga oval dengan bagian tengah "
            "berwarna cokelat muda hingga abu-abu dan tepi berwarna cokelat kemerahan.\u00b9"
        ),
        cause=(
            "Penyakit ini disebabkan oleh jamur Bipolaris oryzae. Jamur dapat menyerang tanaman sejak fase "
            "bibit hingga tanaman dewasa dan juga dapat menginfeksi bagian glume serta gabah.\u00b9 Kondisi "
            "tanaman yang lemah dan kualitas benih yang buruk dapat meningkatkan risiko masalah penyakit "
            "pada pertanaman.\u00b2"
        ),
        symptoms="\n".join([
            "Bercak kecil berbentuk bulat dan berwarna cokelat pada bibit.\u00b9",
            "Bercak berbentuk bulat hingga oval pada daun tanaman dewasa.\u00b9",
            "Bagian tengah bercak dapat berwarna cokelat muda hingga abu-abu.\u00b9",
            "Bagian tepi bercak dapat berwarna cokelat kemerahan.\u00b9",
            "Bercak dapat membesar dan menyatu sehingga menyebabkan sebagian besar daun mati.\u00b9",
            "Bibit dapat mengalami pertumbuhan terhambat atau bahkan mati akibat infeksi berat.\u00b9",
            "Glume dapat mengalami bercak berwarna cokelat tua hingga hitam.\u00b9",
            "Gabah dapat mengalami perubahan warna menjadi hitam akibat infeksi.\u00b9",
        ]),
        details=(
            "Brown Spot dapat muncul sebagai penyakit pada bibit maupun sebagai penyakit daun dan gabah pada "
            "tanaman dewasa. Pada bibit, jamur dapat menghasilkan bercak kecil berbentuk bulat yang dapat "
            "menyebabkan bibit menjadi kerdil atau mati. Pada tanaman yang lebih tua, bercak pada daun umumnya "
            "berbentuk bulat hingga oval dengan bagian tengah berwarna cokelat muda sampai abu-abu dan tepi "
            "berwarna cokelat kemerahan. Jika infeksi cukup berat, bercak dapat menyatu dan menyebabkan area "
            "daun yang luas mengalami kematian.\u00b9"
        ),
        treatment_steps="\n".join([
            "Periksa tanaman secara rutin untuk mengetahui perkembangan bercak.\u00b2",
            "Gunakan benih yang sehat dan berkualitas untuk mengurangi risiko penyakit yang terbawa benih.\u00b2",
            "Lakukan pemupukan secara seimbang agar tanaman dapat tumbuh dengan baik.\u00b2",
            "Jaga kondisi tanaman agar tidak mengalami stres lingkungan yang berat.\u00b2",
            "Kelola sisa tanaman dan kebersihan lahan untuk mengurangi sumber penyakit antar-musim.\u00b2",
            "Jika diperlukan, gunakan produk pengendali penyakit yang terdaftar untuk tanaman padi dan ikuti petunjuk label serta rekomendasi petugas pertanian.\u00b2",
        ]),
        prevention_steps="\n".join([
            "Gunakan benih yang sehat dan berkualitas.\u00b2",
            "Gunakan benih dari sumber yang terpercaya atau bersertifikat jika tersedia.\u00b2",
            "Pilih varietas yang sesuai dengan kondisi lingkungan setempat dan memiliki ketahanan terhadap penyakit utama jika tersedia.\u00b3",
            "Lakukan pemupukan secara seimbang.\u00b2",
            "Jaga kebersihan lahan dan peralatan pertanian.\u00b2",
            "Lakukan pemantauan tanaman sejak fase awal pertumbuhan.\u00b2",
        ]),
        sources=[
            {"title": "IRRI \u2014 Diagnosis of Common Diseases of Rice",
             "url": "http://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf"},
            {"title": "IRRI \u2014 Pests and Diseases: How to manage pests and diseases",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/growth/pests-and-diseases"},
            {"title": "IRRI \u2014 How to Select Rice Varieties",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/rice-varieties"},
        ],
    ),

    dict(
        slug="blast", name="Blast", scientific_name="Magnaporthe oryzae",
        risk_level=Disease.RiskLevel.HIGH,
        short_description="Lesi berbentuk belah ketupat dengan pusat abu-abu, disebabkan jamur Magnaporthe oryzae.",
        description=(
            "Blast atau penyakit blas adalah penyakit jamur pada tanaman padi yang disebabkan oleh Magnaporthe "
            "oryzae. Penyakit ini dapat menyerang berbagai bagian tanaman di atas permukaan tanah, termasuk "
            "daun, collar, buku, leher malai, dan bagian malai.\u00b9"
        ),
        cause=(
            "Penyakit ini disebabkan oleh jamur Magnaporthe oryzae. Blast lebih mudah berkembang pada kondisi "
            "kelembapan yang mendukung, tanah dengan kelembapan rendah, hujan yang sering dan berkepanjangan, "
            "serta suhu siang yang relatif sejuk. Penggunaan pupuk nitrogen secara berlebihan juga dapat "
            "meningkatkan intensitas penyakit.\u00b9"
        ),
        symptoms="\n".join([
            "Muncul bercak berwarna putih hingga hijau keabu-abuan pada awal infeksi.\u00b9",
            "Bercak yang lebih tua berbentuk lonjong atau spindle.\u00b9",
            "Bagian tengah bercak berwarna putih hingga abu-abu.\u00b9",
            "Bagian tepi bercak berwarna cokelat kemerahan atau mengalami nekrosis.\u00b9",
            "Bercak dapat berbentuk seperti berlian atau belah ketupat.\u00b9",
            "Bercak dapat membesar dan menyatu sehingga daun dapat mati.\u00b9",
            "Infeksi pada buku dapat menyebabkan bagian batang menjadi lemah dan patah.\u00b2",
            "Infeksi leher malai dapat menyebabkan malai roboh dan menghasilkan sedikit atau tidak ada gabah.\u00b2",
            "Infeksi sebelum fase pengisian susu dapat menyebabkan gabah tidak terbentuk.\u00b2",
        ]),
        details=(
            "Blast dapat menyerang tanaman padi pada berbagai fase pertumbuhan. Pada daun, gejala yang umum "
            "adalah bercak berbentuk spindle atau belah ketupat dengan bagian tengah berwarna putih hingga "
            "abu-abu dan tepi berwarna cokelat atau nekrotik.\u00b9 Blast pada buku dan leher malai dapat "
            "menjadi lebih serius karena bagian tersebut berhubungan langsung dengan penyangga malai. Infeksi "
            "pada leher dapat menyebabkan malai roboh dan, apabila terjadi sebelum fase pengisian susu, dapat "
            "menyebabkan tidak terbentuknya gabah.\u00b2"
        ),
        treatment_steps="\n".join([
            "Pantau daun, buku, dan leher malai secara rutin untuk mengetahui perkembangan penyakit.\u00b9",
            "Hindari penggunaan pupuk nitrogen secara berlebihan karena dapat meningkatkan intensitas blast.\u00b9",
            "Gunakan pemupukan nitrogen secara terbagi sesuai kebutuhan tanaman.\u00b9",
            "Jaga pengelolaan air agar tanaman tidak mengalami kondisi yang mendukung perkembangan penyakit.\u00b9",
            "Kelola sisa jerami atau tanaman yang terinfeksi karena jamur dapat bertahan pada jerami padi.\u00b9",
            "Jika diperlukan, fungisida sistemik seperti kelompok triazole atau strobilurin dapat digunakan secara bijaksana sesuai rekomendasi dan label.\u00b9",
        ]),
        prevention_steps="\n".join([
            "Gunakan varietas padi yang tahan terhadap blast jika tersedia.\u00b9",
            "Gunakan benih yang sehat dan berkualitas.\u00b3",
            "Hindari penggunaan nitrogen secara berlebihan.\u00b9",
            "Bagi aplikasi nitrogen menjadi beberapa kali sesuai kebutuhan tanaman.\u00b9",
            "Atur waktu tanam sesuai kondisi setempat.\u00b9",
            "Lakukan pemantauan sejak fase awal pertumbuhan.\u00b9",
            "Pastikan jerami atau sisa tanaman yang digunakan tidak berasal dari tanaman yang terinfeksi blast.\u00b9",
        ]),
        sources=[
            {"title": "IRRI \u2014 Blast (leaf and collar)",
             "url": "http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases/item/blast-leaf-collar"},
            {"title": "IRRI \u2014 Blast (node and neck)",
             "url": "http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases/item/blast-node-neck"},
            {"title": "IRRI \u2014 Seed Quality",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/seed-quality"},
        ],
    ),
    dict(
        slug="blight", name="Bacterial Leaf Blight", scientific_name="Xanthomonas oryzae pv. oryzae",
        risk_level=Disease.RiskLevel.HIGH,
        short_description="Hawar daun bakteri, disebabkan oleh bakteri Xanthomonas oryzae.",
        description=(
            "Bacterial Leaf Blight atau Hawar Daun Bakteri adalah penyakit penting pada tanaman padi yang "
            "disebabkan oleh bakteri Xanthomonas oryzae pv. oryzae. Penyakit ini dapat menyerang tanaman sejak "
            "fase persemaian hingga panen dan menyebabkan gejala hawar pada daun serta kelayuan pada fase "
            "tertentu.\u00b9"
        ),
        cause=(
            "Penyakit ini disebabkan oleh bakteri Xanthomonas oryzae pv. oryzae. Bakteri tersebut dapat "
            "menyerang tanaman padi pada berbagai tahap pertumbuhan. Di Indonesia, penyakit ini merupakan "
            "salah satu penyakit penting pada padi.\u00b9"
        ),
        symptoms="\n".join([
            "Muncul garis atau bercak seperti terkena air pada bagian daun.\u00b9",
            "Gejala dapat dimulai beberapa sentimeter dari ujung daun atau pada tepi helaian daun.\u00b9",
            "Bagian yang terinfeksi kemudian berubah menjadi kuning.\u00b9",
            "Lesi dapat semakin panjang dan melebar.\u00b9",
            "Daun dapat berubah menjadi kuning hingga putih ketika penyakit berkembang.\u00b9",
            "Tanaman muda dapat mengalami kelayuan atau gejala kresek.\u00b9",
            "Pada fase generatif, penyakit dapat mengganggu proses pengisian gabah.\u00b2",
        ]),
        details=(
            "Bacterial Leaf Blight dapat menyerang tanaman padi pada seluruh fase pertumbuhan, mulai dari "
            "persemaian hingga panen. Pada fase vegetatif, gejala berat dapat muncul sebagai kelayuan yang "
            "dikenal sebagai kresek. Pada tanaman yang lebih tua, gejala berupa hawar yang berkembang pada "
            "helaian daun. Jika penyakit menyerang pada fase generatif, proses pengisian gabah dapat "
            "terganggu sehingga kualitas dan hasil panen dapat menurun.\u00b2"
        ),
        treatment_steps="\n".join([
            "Periksa tanaman secara rutin dan pisahkan area yang menunjukkan gejala penyakit.\u00b3",
            "Hindari penyebaran air dari area yang terinfeksi ke area tanaman sehat.\u00b3",
            "Hindari aktivitas yang dapat menyebabkan luka pada tanaman ketika kondisi penyakit sedang berkembang.\u00b3",
            "Hindari penggunaan pupuk nitrogen secara berlebihan.\u00b2",
            "Kelola sisa tanaman yang terinfeksi setelah panen untuk mengurangi sumber penyakit antar-musim.\u00b3",
            "Gunakan varietas tahan sebagai bagian dari strategi pengendalian penyakit.\u00b2",
        ]),
        prevention_steps="\n".join([
            "Gunakan benih yang sehat dan berkualitas.\u00b3",
            "Gunakan varietas yang memiliki ketahanan terhadap hawar daun bakteri jika tersedia.\u00b2",
            "Hindari penggunaan nitrogen secara berlebihan.\u00b2",
            "Lakukan pemupukan secara seimbang.\u00b3",
            "Jaga kebersihan lahan dan peralatan pertanian.\u00b3",
            "Hindari perpindahan bahan tanaman atau sisa tanaman yang terinfeksi ke area sehat.\u00b3",
            "Lakukan pemantauan tanaman secara rutin.\u00b3",
        ]),
        sources=[
            {"title": "IRRI \u2014 Bacterial blight",
             "url": "http://www.knowledgebank.irri.org/decision-tools/rice-doctor/rice-doctor-fact-sheets/item/bacterial-blight"},
            {"title": "Kementerian Pertanian RI \u2014 Penyakit Hawar Daun Bakteri pada Padi Sawah",
             "url": "https://pustaka.bppsdmp.pertanian.go.id/info-literasi/info-literasi-kendalikan-penyakit-padi-dengan-tepat-kunci-sukses-cegah-gagal-panen"},
            {"title": "IRRI \u2014 Pests and Diseases: How to manage pests and diseases",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/growth/pests-and-diseases"},
        ],
    ),

    dict(
        slug="tungro", name="Tungro",
        scientific_name="Rice tungro bacilliform virus (RTBV) + Rice tungro spherical virus (RTSV)",
        risk_level=Disease.RiskLevel.MEDIUM,
        short_description="Daun menguning dari pangkal dan tampak layu pada ujungnya.",
        description=(
            "Tungro adalah penyakit virus pada tanaman padi yang disebabkan oleh kombinasi dua virus, yaitu "
            "Rice tungro bacilliform virus (RTBV) dan Rice tungro spherical virus (RTSV). Penyakit ini "
            "ditularkan oleh wereng hijau dan menyebabkan perubahan warna daun, pertumbuhan kerdil, "
            "berkurangnya jumlah anakan, serta gabah yang steril atau tidak terisi sempurna.\u00b9"
        ),
        cause=(
            "Tungro disebabkan oleh kombinasi dua virus yang ditularkan oleh wereng hijau. Wereng hijau "
            "memperoleh virus ketika mengisap tanaman yang terinfeksi dan kemudian dapat menularkannya ke "
            "tanaman lain. Tanaman padi paling rentan terhadap tungro pada fase anakan.\u00b9"
        ),
        symptoms="\n".join([
            "Daun berubah menjadi kuning atau kuning-oranye.\u00b9",
            "Perubahan warna biasanya dimulai dari ujung daun dan dapat menyebar ke bagian bawah daun.\u00b9",
            "Daun dapat memiliki pola belang atau bergaris.\u00b9",
            "Daun dapat memiliki bercak berwarna seperti karat.\u00b9",
            "Tanaman menjadi kerdil.\u00b9",
            "Jumlah anakan berkurang.\u00b9",
            "Pembungaan menjadi terlambat.\u00b9",
            "Malai berukuran kecil dan tidak keluar secara sempurna.\u00b9",
            "Jumlah gabah steril atau gabah yang terisi sebagian meningkat.\u00b9",
            "Dapat ditemukan wereng hijau di sekitar tanaman.\u00b9",
        ]),
        details=(
            "Tungro merupakan penyakit virus yang penularannya bergantung pada serangga vektor, terutama "
            "wereng hijau. Penyakit dapat menyerang pada semua fase pertumbuhan, tetapi paling sering terlihat "
            "pada fase vegetatif dan tanaman paling rentan ketika berada pada fase anakan. Tanaman yang "
            "terinfeksi dapat menjadi kerdil, menghasilkan lebih sedikit anakan, mengalami keterlambatan "
            "pembungaan, serta menghasilkan malai kecil dengan gabah yang steril atau hanya terisi "
            "sebagian.\u00b9"
        ),
        treatment_steps="\n".join([
            "Tanaman padi yang sudah terinfeksi tungro tidak dapat disembuhkan.\u00b9",
            "Cabut dan kelola tanaman yang terinfeksi sesuai praktik sanitasi setempat untuk mengurangi sumber virus.\u00b9",
            "Pantau tanaman di sekitar area yang terinfeksi.\u00b9",
            "Kendalikan sumber virus seperti tanaman padi sisa dan volunteer rice.\u00b9",
            "Kelola sisa tanaman setelah panen untuk mengurangi sumber virus dan tempat berkembang biak wereng hijau.\u00b9",
            "Jangan menggunakan bibit dari area yang diketahui terinfeksi tungro.\u00b9",
        ]),
        prevention_steps="\n".join([
            "Gunakan varietas yang tahan terhadap tungro atau wereng hijau jika tersedia.\u00b9",
            "Gunakan bibit dan benih yang sehat.\u00b3",
            "Lakukan penanaman secara serempak dengan area sekitar jika memungkinkan.\u00b9",
            "Sesuaikan waktu tanam agar tidak bertepatan dengan periode populasi wereng hijau yang tinggi jika informasi tersebut tersedia.\u00b9",
            "Kelola sisa tanaman yang terinfeksi setelah panen.\u00b9",
            "Pantau keberadaan wereng hijau sejak fase awal pertumbuhan.\u00b9",
            "Hindari menggunakan bibit dari persemaian yang berada di daerah endemis tungro.\u00b9",
        ]),
        sources=[
            {"title": "IRRI \u2014 Tungro",
             "url": "http://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases/item/tungro"},
            {"title": "IRRI \u2014 Diagnosis of Common Diseases of Rice",
             "url": "http://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf"},
            {"title": "IRRI \u2014 Seed Quality",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/seed-quality"},
        ],
    ),

    dict(
        slug="scald", name="Leaf Scald", scientific_name="Microdochium oryzae",
        risk_level=Disease.RiskLevel.LOW,
        short_description="Lesi memanjang dengan pola bergelombang seperti terbakar pada ujung daun.",
        description=(
            "Leaf Scald atau hawar daun adalah penyakit jamur pada tanaman padi yang menyebabkan munculnya "
            "bercak memanjang dan berzona pada daun. Gejalanya berupa zona warna cokelat muda dan cokelat tua "
            "yang biasanya dimulai dari tepi atau ujung daun.\u00b9"
        ),
        cause=(
            "Penyakit ini disebabkan oleh jamur Microdochium oryzae. Jamur membentuk struktur dan spora pada "
            "bagian jaringan daun yang mengalami lesi.\u00b9"
        ),
        symptoms="\n".join([
            "Bercak biasanya muncul pada tepi atau ujung daun.\u00b9",
            "Bercak memiliki pola berzona dengan warna cokelat muda dan cokelat tua.\u00b9",
            "Lesi umumnya berbentuk lonjong atau memanjang.\u00b9",
            "Bercak dapat memiliki bagian tepi atau halo berwarna cokelat muda.\u00b9",
            "Bercak dapat memiliki panjang beberapa sentimeter dan terus berkembang.\u00b9",
            "Beberapa bercak dapat membesar dan menyatu.\u00b9",
            "Sebagian besar helaian daun dapat mengalami hawar.\u00b9",
            "Bagian yang terinfeksi akhirnya mengering sehingga daun terlihat seperti terkena panas atau tersiram air panas.\u00b9",
        ]),
        details=(
            "Leaf Scald memiliki gejala yang khas berupa lesi berzona dengan pola warna cokelat muda dan "
            "cokelat tua. Lesi biasanya dimulai dari tepi atau ujung daun yang sudah dewasa dan berbentuk "
            "kurang lebih lonjong. Lesi dapat terus membesar dan menyatu sehingga sebagian besar helaian daun "
            "mengalami hawar. Ketika jaringan yang terkena penyakit mengering, daun menghasilkan tampilan "
            "seperti terkena panas atau tersiram air panas.\u00b9"
        ),
        treatment_steps="\n".join([
            "Periksa daun secara rutin untuk mengetahui perkembangan lesi.\u00b2",
            "Kelola bagian tanaman yang sudah mati dan sisa tanaman yang terinfeksi sebagai bagian dari sanitasi lahan.\u00b2",
            "Jaga kondisi tanaman agar tumbuh dengan baik melalui pengelolaan air dan nutrisi yang sesuai.\u00b2",
            "Lakukan pemupukan secara seimbang.\u00b2",
            "Jika penyakit berkembang berat, konsultasikan penggunaan fungisida yang terdaftar untuk padi kepada petugas pertanian dan ikuti petunjuk label.\u00b2",
        ]),
        prevention_steps="\n".join([
            "Gunakan benih yang sehat dan berkualitas.\u00b3",
            "Gunakan varietas yang sesuai dengan kondisi lingkungan setempat.\u2074",
            "Jaga kebersihan lahan dan peralatan pertanian.\u00b2",
            "Kelola sisa tanaman setelah panen dengan baik.\u00b2",
            "Lakukan pemupukan secara seimbang.\u00b2",
            "Lakukan pemantauan daun secara rutin sejak tanaman masih muda.\u00b2",
        ]),
        sources=[
            {"title": "IRRI \u2014 Diagnosis of Common Diseases of Rice",
             "url": "http://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf"},
            {"title": "IRRI \u2014 Pests and Diseases: How to manage pests and diseases",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/growth/pests-and-diseases"},
            {"title": "IRRI \u2014 Seed Quality",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/seed-quality"},
            {"title": "IRRI \u2014 How to Select Rice Varieties",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/rice-varieties"},
        ],
    ),

    dict(
        slug="healthy", name="Healthy Rice", scientific_name="Oryza sativa L.",
        risk_level=Disease.RiskLevel.NONE,
        short_description="Daun padi dalam kondisi sehat, tidak menunjukkan tanda penyakit.",
        description=(
            "Padi sehat adalah tanaman Oryza sativa L. yang tumbuh dan berkembang secara normal tanpa "
            "menunjukkan gejala penyakit atau kerusakan berat akibat hama maupun stres lingkungan. Kondisi "
            "tanaman sehat dipengaruhi oleh kualitas benih, varietas yang sesuai, pengelolaan air dan nutrisi, "
            "serta pengelolaan hama dan penyakit yang baik.\u00b9"
        ),
        cause=(
            "Kondisi padi sehat tidak disebabkan oleh satu faktor saja. Pertumbuhan sehat dipengaruhi oleh "
            "penggunaan benih berkualitas, varietas yang sesuai dengan lingkungan, ketersediaan nutrisi yang "
            "cukup dan seimbang, pengelolaan air yang baik, jarak tanam yang sesuai, serta pengendalian hama "
            "dan penyakit.\u00b9 \u00b2"
        ),
        symptoms="\n".join([
            "Daun berwarna hijau dan terlihat segar.\u00b9",
            "Warna daun relatif seragam sesuai karakter varietas.\u00b9",
            "Tidak menunjukkan bercak penyakit yang mencurigakan.",
            "Tanaman tumbuh dan berkembang secara normal.",
            "Pertumbuhan tanaman relatif seragam.",
            "Batang berkembang dengan baik dan mampu menopang tanaman.",
            "Jumlah anakan berkembang secara normal.",
            "Tidak menunjukkan gejala layu yang tidak normal.",
            "Tidak mengalami kerusakan berat akibat hama.",
            "Malai berkembang secara normal.",
            "Gabah berkembang dan terisi dengan baik.",
        ]),
        details=(
            "Padi sehat memiliki pertumbuhan yang baik sejak fase persemaian hingga fase generatif. Penggunaan "
            "benih berkualitas membantu menghasilkan kemunculan tanaman yang lebih seragam, pertumbuhan awal "
            "yang lebih kuat, dan vigor yang lebih baik.\u00b9 Varietas yang sesuai dengan lingkungan juga "
            "penting karena varietas dapat memiliki ketahanan atau toleransi berbeda terhadap penyakit, "
            "serangga, kekeringan, banjir, dan tekanan lingkungan lainnya.\u00b2"
        ),
        treatment_steps="\n".join([
            "Pantau kondisi tanaman secara rutin untuk mendeteksi hama dan penyakit sejak awal.\u00b3",
            "Pastikan kebutuhan air tanaman terpenuhi dan lakukan pengelolaan air yang sesuai.\u00b3",
            "Lakukan pemupukan berdasarkan kebutuhan tanaman dan kondisi lahan.\u00b3",
            "Hindari penggunaan nitrogen secara berlebihan karena nitrogen yang terlalu tinggi dapat meningkatkan kerentanan terhadap beberapa hama dan penyakit.\u00b3",
            "Kendalikan gulma yang bersaing dengan tanaman dalam memperoleh nutrisi.\u00b3",
            "Jaga kebersihan lahan dan peralatan pertanian antar-musim.\u00b3",
            "Gunakan prinsip pengelolaan hama dan penyakit secara terpadu.\u00b3",
            "Segera periksa tanaman apabila mulai menunjukkan gejala penyakit atau serangan hama.\u00b3",
        ]),
        prevention_steps="\n".join([
            "Gunakan benih yang sehat dan berkualitas.\u00b9",
            "Gunakan benih bersertifikat jika tersedia.\u00b9",
            "Pastikan benih memiliki daya kecambah dan vigor yang baik.\u00b9",
            "Pilih varietas yang sesuai dengan kondisi lingkungan setempat.\u00b2",
            "Pilih varietas yang memiliki ketahanan atau toleransi terhadap penyakit dan hama utama di daerah tersebut jika tersedia.\u00b2",
            "Gunakan jarak tanam yang sesuai dengan varietas dan sistem budidaya.\u00b2",
            "Lakukan pemupukan secara tepat dan hindari pemberian nitrogen secara berlebihan.\u00b3",
            "Kelola air dengan baik.\u00b3",
            "Jaga kebersihan lahan dan peralatan pertanian.\u00b3",
            "Lakukan penanaman secara serempak dengan area sekitar jika kondisi setempat memungkinkan.\u00b3",
            "Lakukan pemantauan sejak fase persemaian.\u00b3",
        ]),
        sources=[
            {"title": "IRRI \u2014 Seed Quality",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/seed-quality"},
            {"title": "IRRI \u2014 How to Select Rice Varieties",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/pre-planting/rice-varieties"},
            {"title": "IRRI \u2014 Pests and Diseases: How to manage pests and diseases",
             "url": "http://www.knowledgebank.irri.org/step-by-step-production/growth/pests-and-diseases"},
        ],
    ),
]

class Command(BaseCommand):
    help = "Seed the disease classes used by the RiceCareAI/HealthyRiceAI detection model."

    def handle(self, *args, **options):
        created, updated = 0, 0
        for data in DISEASES:
            obj, was_created = Disease.objects.update_or_create(slug=data["slug"], defaults=data)
            created += was_created
            updated += not was_created
        self.stdout.write(self.style.SUCCESS(f"Seeded diseases: {created} created, {updated} updated."))
