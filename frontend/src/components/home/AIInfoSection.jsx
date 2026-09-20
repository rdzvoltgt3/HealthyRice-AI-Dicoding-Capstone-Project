import riceField from "../../assets/images/rice-field-2.jpg";
import "./AIInfoSection.css";

function AIInfoSection() {
  const information = [
    {
      number: "01",
      title: "Arsitektur",
      text: "Menggunakan Convolutional Neural Network ConvNeXt V2 Tiny.",
    },
    {
      number: "02",
      title: "Data Latih",
      text: "13.185 citra daun padi dari dataset publik yang telah dibersihkan.",
    },
    {
      number: "03",
      title: "Kelas yang Dikenali",
      text: "Blast, Bacterial Blight, Brown Spot, Scald, Tungro, dan daun sehat.",
    },
    {
      number: "04",
      title: "Performa",
      text: "Akurasi 97,02% dan macro F1-score 96,23% pada data uji.",
    },
  ];

  return (
    <section className="ai-section" id="model-ai">
      <div className="ai-content">
        {/* Section label */}
        <span className="section-label">Model AI</span>

        {/* Section heading */}
        <div className="ai-heading">
          <h2>Informasi Model AI</h2>
        </div>

        {/* AI information list */}
        <div className="ai-list">
          {information.map((item) => (
            <div className="ai-item" key={item.number}>
              <span className="ai-number">{item.number}</span>

              <div>
                <h3 className="ai-item-title">{item.title}</h3>
                <p>{item.text}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* AI image */}
      <div className="ai-image-wrapper">
        <img src={riceField} alt="Sawah" className="ai-image" />
      </div>
    </section>
  );
}

export default AIInfoSection;
